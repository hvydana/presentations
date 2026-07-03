# LeRobot Setup, SmolVLA Inference, and the RTC Async Control Loop

This document explains, against the **actual** upstream HuggingFace lerobot code
(cloned locally by the Makefile, not a re-implementation), how the SmolVLA
policy runs, how the control loop consumes images and produces action chunks,
how Real-Time Chunking (RTC) works with its background async thread, which
modules/parameters are consumed, and how inference **speed** translates into
robot **performance**.

- **Source of truth**: `https://github.com/huggingface/lerobot.git`
- **Pinned commit**: `c8ce413d738da15a2eed2d0832315779ea28cbf9` (verified `git rev-parse HEAD` matches)
- **Local clone**: `models/smolVLA/lerobot/` (built editable into `venv_gpu` / `venv_cpu`)
- **Patches applied on top** (idempotent, from `lerobot_patches/`):
  `lerobot_full.patch`, `smolvla_halfprecision_dtype_fix.patch`,
  `smolvla_cudagraph_kvcache_clone.patch`

All file paths below are relative to `models/smolVLA/lerobot/src/lerobot/`
unless noted otherwise.

---

## 0. The big picture

There are **three** distinct inference paths in this codebase. It is important
not to confuse them (an earlier analysis apparently mixed them up):

| Path | Where | Threading | Chunk trigger | Latency handling |
|---|---|---|---|---|
| **A. Sync** (`select_action`) | `rollout/inference/sync.py` | main thread, **blocks** | policy-internal `deque` empty | none |
| **B. RTC async** (`predict_action_chunk`) | `rollout/inference/rtc.py` | **background thread** | queue `qsize <= threshold` | explicit delay-skip + prefix guidance |
| **C. gRPC async** (older) | `async_inference/` | 2 processes over gRPC | `qsize/chunk_size <= 0.5` | proactive obs sending |

The AMD/ROCm work in `models/smolVLA/scripts/` and the RTC feature the user
cares about are **path A and path B**. `lerobot-record` itself is *teleoperation
only* — it does not run the policy; policy rollouts use `lerobot-rollout`.

The engine that decides which path to use is the SmolVLA config: if
`policy.config.rtc_config` exists and is `enabled`, the loop must call
`predict_action_chunk` (path B); otherwise it calls `select_action` (path A).
This is enforced inside the policy — `select_action` contains
`assert not self._rtc_enabled()`.

---

## 1. The control loop (fixed-rate timing)

### `lerobot-record` — teleop capture only (no policy)

`scripts/lerobot_record.py` → `record_loop()` (lines ~195–322). One tick:

```python
control_interval = 1 / fps                     # e.g. 1/30 = 0.0333 s
while timestamp < control_time_s:
    start_loop_t = time.perf_counter()
    obs = robot.get_observation()              # read cameras + joints
    act = teleop.get_action()                  # HUMAN action, not a policy
    robot.send_action(...)                     # command the robot
    dataset.add_frame(frame)                   # log the frame
    dt_s = time.perf_counter() - start_loop_t
    precise_sleep(max(control_interval - dt_s, 0.0))   # keep fixed fps
    timestamp = time.perf_counter() - start_episode_t
```

The **fixed frequency** mechanism is universal across every loop in the repo:
measure elapsed `dt`, then `precise_sleep(control_interval - dt)`. If a tick
overruns (`dt > control_interval`), the sleep clamps to 0 and a warning
`"Record loop is running slower ..."` is logged. `precise_sleep` uses a
sleep+spin hybrid on macOS/Windows and plain `time.sleep` on Linux.

### `lerobot-rollout` — the policy loop

`scripts/lerobot_rollout.py` builds a `RolloutContext` and a strategy;
`rollout/strategies/base.py` → `BaseStrategy.run()` (lines ~42–77) is the clean
example:

```python
control_interval = interpolator.get_control_interval(cfg.fps)  # 1/(fps*multiplier)
engine.resume()
while not ctx.runtime.shutdown_event.is_set():
    loop_start = time.perf_counter()
    obs = robot.get_observation()
    obs_processed = self._process_observation_and_notify(ctx.processors, obs)  # → RTC thread
    if self._handle_warmup(cfg.use_torch_compile, loop_start, control_interval):
        continue
    action_dict = send_next_action(obs_processed, obs, ctx, interpolator)
    dt = time.perf_counter() - loop_start
    if (sleep_t := control_interval - dt) > 0:
        precise_sleep(sleep_t)
    else:
        logger.warning("Record loop is running slower ...")
```

Two things flow every tick:
1. **Observation out** → `notify_observation()` publishes the latest obs to the
   inference engine (for RTC, that means to the background thread).
2. **Action in** → `send_next_action()` calls `engine.get_action()` which pops
   the next ready action (or returns `None`).

`send_next_action` (in `rollout/inference/core.py`) also drives the optional
`ActionInterpolator`: with `interpolation_multiplier = N`, each policy action is
linearly interpolated into `N` sub-actions, so the robot runs at `fps*N` Hz while
the policy runs at `fps` Hz.

---

## 2. SmolVLA policy: observation → action chunk

File: `policies/smolvla/modeling_smolvla.py` and `configuration_smolvla.py`.

### 2.1 The two public entry points

**`select_action(batch)`** (lines ~324–350) — path A. Returns ONE action per
call using an internal deque:

```python
def reset(self):
    self._queues = {ACTION: deque(maxlen=self.config.n_action_steps)}   # default 50

def select_action(self, batch, noise=None, **kwargs):
    assert not self._rtc_enabled()                       # RTC must use predict_action_chunk
    self.eval()
    batch = self._prepare_batch(batch)
    self._queues = populate_queues(self._queues, batch, exclude_keys=[ACTION])
    if len(self._queues[ACTION]) == 0:                   # queue drained → re-infer
        actions = self._get_action_chunk(batch, noise)   # (B, chunk_size, action_dim)
        self._queues[ACTION].extend(actions.transpose(0, 1)[: self.config.n_action_steps])
    return self._queues[ACTION].popleft()                # one action (B, action_dim)
```

So a fresh forward pass happens only once per `n_action_steps` control ticks;
the other ticks are a cheap `popleft()`. This is **closed-loop chunked
execution** (a.k.a. receding horizon when `n_action_steps < chunk_size`).

**`predict_action_chunk(batch, ...)`** (lines ~313–322) — path B/RTC. Returns
the **whole chunk** and manages no internal queue (the RTC engine owns the
queue):

```python
def predict_action_chunk(self, batch, noise=None, **kwargs):
    self.eval()
    batch = self._prepare_batch(batch)
    self._queues = populate_queues(self._queues, batch, exclude_keys=[ACTION])
    return self._get_action_chunk(batch, noise, **kwargs)   # (B, chunk_size, action_dim)
```

Output shape: `(B, chunk_size, action_dim)`, e.g. `(B, 50, 7)` for a 7-DoF arm
(model computes on a padded `max_action_dim=32` then unpads to the real dim).

### 2.2 `_get_action_chunk` — the pipeline (lines ~276–304)

```python
images, img_masks = self.prepare_images(batch)     # resize/pad, [-1,1], per-cam masks
state = self.prepare_state(batch)                  # last step, zero-pad to max_state_dim=32
lang_tokens = batch[OBS_LANGUAGE_TOKENS]
lang_masks  = batch[OBS_LANGUAGE_ATTENTION_MASK]
actions = self.model.sample_actions(images, img_masks, lang_tokens, lang_masks,
                                    state, noise=noise, **kwargs)   # flow matching
actions = actions[:, :, :self.config.action_feature.shape[0]]      # unpad action dim
```

### 2.3 Image processing (`prepare_images`, lines ~415–455)

1. **Camera selection**: keys from `config.image_features` (pattern
   `observation.images.<cam>`) that are present in the batch.
2. **Last frame**: if a temporal dim exists `(B,T,C,H,W)`, take `[:, -1]`
   (`n_obs_steps=1` by default → only the current frame is used).
3. **Resize with padding**: `resize_with_pad(img, 512, 512, pad_value=0)`
   (`resize_imgs_with_padding = (512, 512)`) — aspect-preserving bilinear resize,
   then pad top/left with 0. This is SigLIP's expected input geometry.
4. **Pixel range**: `img = img * 2.0 - 1.0` → maps `[0,1] → [-1,1]` (SigLIP range).
   (Note: image normalization mode is `IDENTITY` in the normalizer; this manual
   `*2-1` is the actual pixel normalization.)
5. **Masks**: present camera → `ones` bool mask; absent/`empty_cameras` slots →
   black `-1.0` image + `zeros` mask.
6. **Embedding**: each camera goes through the SigLVM2 vision tower
   (`embed_image` → SigLIP ViT + connector), scaled by `sqrt(hidden_dim)`. Every
   camera's patch tokens are concatenated along the sequence dimension into the
   prefix, so the model sees cam1 tokens, then cam2 tokens, etc.

### 2.4 Prefix / KV-cache and flow-matching denoising

The VLM (SmolVLM2-500M) encodes **[images + language + state]** into a **prefix**
and its **KV cache is computed once** per chunk; the small **action expert** then
runs the denoising loop reading that cache.

**Prefill (once per chunk)** — `_prefill_prefix` (added by `lerobot_full.patch`):

```python
prefix_embs, prefix_pad_masks, prefix_att_masks = self.embed_prefix(images, ..., state)
_, past_key_values = self.vlm_with_expert.forward(
    ..., past_key_values=None, inputs_embeds=[prefix_embs, None],
    use_cache=True, fill_kv_cache=True)          # WRITE K/V into cache
```

`past_key_values` is a dict keyed by `layer_idx` → `{key_states, value_states}`.

**Denoise loop (flow matching)** — `sample_actions` (lines ~903–1038):

```python
x_t = noise                         # (B, chunk_size, max_action_dim=32) ~ N(0,1)
dt  = -1.0 / num_steps              # num_steps default 10 → dt = -0.1
for step in range(num_steps):       # 10 Euler steps
    time = 1.0 + step * dt          # 1.0, 0.9, ..., 0.1
    v_t  = self.denoise_step(x_t, prefix_pad_masks, past_key_values, timestep)
    x_t  = x_t + dt * v_t           # Euler integration toward t=0
```

This is **Conditional Flow Matching**: the expert predicts a velocity field
`v_t`; integrating the ODE from pure noise (`t=1`) to `t=0` yields the action
chunk. Each `denoise_step` (lines ~1040–1080) embeds the noisy actions + a
sinusoidal timestep embedding, runs the expert with `fill_kv_cache=False` (so it
**reads** the frozen prefix cache and appends only the suffix K/V), then
`action_out_proj` maps the last `chunk_size` tokens to `v_t`.

**Why the KV cache matters for speed**: the expensive vision+language encoding
happens **once**; the 10 denoising steps only pay for the small action-expert
attention over the cached prefix. `use_cache=False` would recompute the whole
VLM every denoise step (~10× cost).

### 2.5 Normalization

- Inputs: state uses `MEAN_STD` (z-score) applied by the preprocessor pipeline
  *before* the policy; images use `IDENTITY` (manual `*2-1` inside the model).
- Outputs: actions are `MEAN_STD`, so the postprocessor does `action*std + mean`
  to return to the robot's native units.

---

## 3. RTC: the async background loop (the core of the user's question)

Files: `rollout/inference/rtc.py` (engine), `policies/rtc/action_queue.py`
(queue), `policies/rtc/modeling_rtc.py` (guidance math),
`policies/rtc/configuration_rtc.py` (params).

### 3.1 Architecture

RTC decouples inference from control using **one background thread** plus a
shared, thread-safe `ActionQueue`:

```
 main control loop (fps Hz)          background RTC thread (as fast as GPU allows)
 ---------------------------          --------------------------------------------
 obs = robot.get_observation()
 notify_observation(obs)  ───────────▶  reads latest obs (obs_lock)
 action = queue.get()  ◀────────────┐   if queue.qsize() <= threshold:
 robot.send_action(action)          │       predict_action_chunk(...)   (denoise)
 precise_sleep(...)                 └───    queue.merge(new_chunk, delay)
```

The main loop **never blocks on inference** — it just pops the next ready action.
The background thread continuously refills the queue.

### 3.2 The background loop `_rtc_loop` (rtc.py lines 247–360)

```python
time_per_chunk = 1.0 / self._fps
while not self._shutdown_event.is_set():
    if not self._policy_active.is_set(): time.sleep(0.01); continue   # paused
    obs = self._obs_holder.get("obs")                                 # latest obs
    if queue is None or obs is None:     time.sleep(0.01); continue

    if queue.qsize() <= self._rtc_queue_threshold:      # default 30 → refill
        current_time = time.perf_counter()
        idx_before   = queue.get_action_index()
        prev_actions = queue.get_left_over()            # unexecuted tail (for guidance)

        latency = latency_tracker.max()                 # worst recent inference time
        delay   = math.ceil(latency / time_per_chunk) if latency else 0

        obs_batch    = build_dataset_frame(self._hw_features, obs, prefix="observation")
        obs_batch    = prepare_observation_for_inference(obs_batch, device, task, robot_type)
        preprocessed = self._preprocessor(obs_batch)

        # (relative-action re-anchoring, if enabled, keeps the leftover tail in
        #  the training coordinate frame)
        if prev_actions is not None:
            prev_actions = _normalize_prev_actions_length(
                prev_actions, target_steps=self._rtc_config.execution_horizon)

        actions   = self._policy.predict_action_chunk(
                        preprocessed, inference_delay=delay, prev_chunk_left_over=prev_actions)
        original  = actions.squeeze(0).clone()
        processed = self._postprocessor(actions).squeeze(0)

        new_latency = time.perf_counter() - current_time
        new_delay   = math.ceil(new_latency / time_per_chunk)
        latency_tracker.add(new_latency)
        queue.merge(original, processed, new_delay, idx_before)   # replace queue, skip `delay`
    else:
        time.sleep(0.01)                                # backpressure: queue still full
```

Key points:
- **Trigger**: refill when `qsize <= rtc_queue_threshold` (default **30**). At
  30 fps that is ~1 s of buffered actions — the latency budget before the queue
  can drain.
- **`prev_chunk_left_over`**: the unexecuted tail of the *current* chunk is fed
  into the next prediction so the new chunk is *continuous* with what the robot
  is already doing (this is the RTC "inpainting" idea).
- **`inference_delay`**: computed from the *previous* max latency so the model
  knows how many leading actions to treat as "already executed."

### 3.3 The `ActionQueue` (action_queue.py)

Holds two tensors — `queue` (post-processed, robot-ready) and `original_queue`
(pre-postprocessor, needed for RTC guidance) — plus a `last_index` cursor.

- **`get()`** (line 67): return `queue[last_index]`, `last_index += 1`, else
  `None` if drained. This is what the control loop pops each tick.
- **`get_left_over()`** (line 120): `original_queue[last_index:]` — the
  unexecuted tail passed as `prev_chunk_left_over`.
- **`merge()` / `_replace_actions_queue()`** (RTC mode, lines 147–194):

```python
clamped_delay = max(0, min(real_delay, len(original), len(processed)))
self.original_queue = original[clamped_delay:].clone()   # DROP the first `delay` actions:
self.queue          = processed[clamped_delay:].clone()  # the robot already advanced that far
self.last_index     = 0
```

Example: at 30 fps (33 ms/tick), if inference took 200 ms, `delay = ceil(0.2/0.033) = 7`
— the first 7 actions of the new chunk are discarded because 7 ticks already
elapsed during inference. This is the **latency compensation**: the new chunk is
spliced in exactly where the robot actually is, not where it was when the obs was
captured.

In **non-RTC** mode `merge()` instead *appends* (`_append_actions_queue`) for
continuity.

### 3.4 RTC guidance math (modeling_rtc.py `RTCProcessor.denoise_step`)

RTC does not just concatenate chunks — it **steers the denoiser** so the new
chunk agrees with the leftover prefix on the overlapping timesteps. Inside each
denoising step (lines 126–193, the compile-friendly version added by the patch):

```python
weights = self._get_prefix_weights_tensor(inference_delay, execution_horizon, chunk_size)
v_t   = original_denoise_step_partial(x_t)     # base velocity from the expert
x1_t  = x_t - time * v_t                        # predicted clean action at this step
err   = (prev_chunk_left_over - x1_t) * weights # pull toward the leftover prefix
correction = torch.where(has_prev_chunk, err, 0)
# guidance weight schedule (clamped at max_guidance_weight = 10.0)
guidance_weight = clamp( ((1-tau)/tau) * ((sq + tau^2)/sq), max=10.0 )   # tau = 1-time
return v_t - guidance_weight * correction
```

- `prefix_attention_schedule` (default `LINEAR`) builds `weights`: **1.0** for the
  first `inference_delay` actions (already-committed, strong pull), a **linear
  ramp** down to 0 over `[start, execution_horizon)`, and **0** afterward (the new
  part of the chunk is free).
- `execution_horizon` (default **10**) is how far into the chunk the guidance
  reaches — beyond it the policy is unconstrained.
- `max_guidance_weight` (default **10.0**) caps how hard the correction pulls,
  preventing divergence as `tau → 0`.

The patch replaced the legacy `torch.autograd.grad` implementation
(`denoise_step_legacy`) with the closed-form `correction = err` (valid because
`v_t` is constant w.r.t. `x_t`) so the whole thing is `torch.compile`/CUDA-graph
friendly — no graph breaks from `requires_grad_`/`autograd.grad`.

### 3.5 RTC parameters (configuration_rtc.py)

| Param | Default | Meaning |
|---|---|---|
| `enabled` | `True` | Turns RTC path on (replace-queue + guidance). |
| `prefix_attention_schedule` | `LINEAR` | Shape of the prefix-overlap weight ramp (`ZEROS`/`ONES`/`LINEAR`/`EXP`). |
| `max_guidance_weight` | `10.0` | Ceiling on guidance strength. |
| `execution_horizon` | `10` | How many leading steps the guidance covers / the leftover-tail target length. |
| `rtc_queue_threshold`* | `30` | (engine arg) refill when queue drops to this. |

\* `rtc_queue_threshold` lives on `RTCInferenceEngine.__init__`, not `RTCConfig`.

---

## 4. Which parameters get consumed, and by whom

SmolVLA config (`configuration_smolvla.py`) — the ones that shape the loop:

| Param | Default | Effect |
|---|---|---|
| `chunk_size` | `50` | Actions predicted per forward pass; suffix length for the expert. |
| `n_action_steps` | `50` | How many of the chunk are executed before re-inference (path A). `< chunk_size` ⇒ receding horizon. |
| `num_steps` | `10` | Flow-matching Euler steps = expert forward passes per chunk. Higher = more accurate, slower. |
| `n_obs_steps` | `1` | Obs history kept; only last frame currently used. |
| `resize_imgs_with_padding` | `(512,512)` | SigLIP input size. |
| `max_state_dim` / `max_action_dim` | `32` / `32` | Zero-pad width for state/action projections. |
| `tokenizer_max_length` | `48` | Max language tokens. |
| `vlm_model_name` | `SmolVLM2-500M-Video-Instruct` | Vision (SigLIP) + text backbone. |
| `num_vlm_layers` | `16` | VLM layers actually used. |
| `num_expert_layers` | `-1` | Expert layers (`-1` = same as VLM). |
| `expert_width_multiplier` | `0.75` | Expert hidden size = 0.75 × VLM hidden. |
| `attention_mode` | `cross_attn` | Expert cross-attends to VLM KV cache. |
| `use_cache` | `True` | Build+reuse prefix KV cache (the big speed lever). |
| `compile_model` / `compile_mode` / `compile_full_model` | off / `max-autotune` / off | torch.compile scope (patched flags). |
| `rtc_config` | `None` | If present+enabled ⇒ RTC path. |

Modules consumed per chunk: **SigLIP vision encoder** + **connector** →
**SmolVLM2 backbone** (prefix prefill, once) → **action expert**
(`num_steps` denoise passes over the cached prefix) →
`action_out_proj`/unpad → **postprocessor** (unnormalize).

---

## 5. How speed translates to performance

The robot runs at a fixed **control frequency** `fps`; each tick has a hard
budget `control_interval = 1/fps` (e.g. 33 ms at 30 fps). Whether the robot moves
smoothly depends on whether an action is *ready* every tick.

**Path A (sync, `select_action`)**: inference blocks the main thread. Total per-
chunk cost ≈ `prefill + num_steps × denoise_step`. It is amortized over
`n_action_steps` ticks: the chunk tick is expensive, the other
`n_action_steps-1` ticks are ~free deque pops. If the chunk tick exceeds the
budget, that tick overruns (warning logged) — a visible stutter every
`n_action_steps` frames. Bigger `n_action_steps` = fewer inferences/sec =
smoother but *staler* actions (open-loop for longer). The benchmark reports this
as `inference_calls_per_s_amortised = throughput_steps_per_s / n_action_steps`.

**Path B (RTC async)**: inference is off the critical path. The metric that
matters is: can the background thread produce a fresh chunk before the queue
drains? With `rtc_queue_threshold = 30` at 30 fps you have ~1 s of buffer. As
long as `inference_latency < buffer_time`, the main loop always has an action
and runs at full `fps`. RTC then adds *quality*: `delay`-skip splices the new
chunk in at the robot's true position, and prefix guidance makes consecutive
chunks continuous (no jerk at chunk boundaries). If inference is *too* slow and
the queue empties, `get_action()` returns `None` and the robot holds/stalls that
tick — so **latency sets the floor on control rate you can sustain**, and RTC
buys headroom + smoothness rather than raw speed.

**Where the speed comes from** (and what the AMD patches target):
- **KV cache** (`use_cache=True`): VLM prefill once, expert-only denoising ×`num_steps`.
- **`num_steps`**: linear knob on denoise cost (10 → fewer trades accuracy for latency).
- **True-half precision** (bf16/fp16): `smolvla_halfprecision_dtype_fix.patch`
  makes `action_out_proj` read `self.action_out_proj.weight.dtype` instead of a
  hard-coded fp32 cast, so half-precision weights don't hit a dtype-mismatch.
- **torch.compile**: `lerobot_full.patch` compiles `denoise_step` (the hot inner
  loop) and, with `compile_full_model`, `_prefill_prefix`; it deliberately does
  **not** compile `sample_actions` (dynamic Python control flow ⇒ recompiles).
  The RTC guidance was rewritten to be graph-break-free (closed-form correction,
  Python-float `max_guidance_weight`, tensor-only inputs) so `reduce-overhead`
  CUDA/HIP graphs actually capture.
- **CUDA/HIP graph correctness**: `smolvla_cudagraph_kvcache_clone.patch` clones
  the KV cache out of static graph buffers under `reduce-overhead +
  compile_full_model`, otherwise the graph replay would overwrite the cache and
  corrupt actions silently.

---

## 6. The AMD wrapper scripts (parity with the real loop)

`models/smolVLA/scripts/` reproduces the production inference primitive on real
`LeRobotDataset` frames ("lerobot-record parity", i.e. no synthetic tensors):

- **`pipeline.py`** → `load_policy()` builds `SmolVLAPolicy.from_pretrained`,
  optionally sets `compile_model`/`compile_mode` on the config *before* build
  (the patched `__init__` wires compile at construction), warm-starts the torch
  Mega-Cache (`compile_cache.py`), and casts to true-half for bf16/fp16.
  `ChunkedActionRunner.step()` GPU-syncs around `predict_action_chunk`, buffers
  the chunk, and pops one action per step — exactly the RTC/chunked production
  path.
- **`eval/inference_lerobot.py`** → `run_auto_inference()` dispatches:
  `policy_uses_rtc(policy)` ⇒ chunked `predict_action_chunk` runner, else
  `select_action` per frame. `build_auto_camera_map()` maps dataset camera keys
  to the checkpoint's `image_features` by sorted order.
- **`evaluate_lerobot.py` / `benchmark_lerobot.py`** → drive the above and record
  per-step latency (`torch.cuda.synchronize()` around the model call) →
  mean/median/p95/p99 + `throughput_steps_per_s`.
- **Config**: `config/action_pervedio.yaml` (gesture-mimic) and
  `config/config.yaml` (red-cube) set `device=cuda`, `fps=30`, 3 cameras;
  `chunk_size`/`n_action_steps`/RTC come from the checkpoint's `config.json`
  (CLI can override `--n_action_steps`, `--num_steps`).

---

## 7. End-to-end call graph (RTC path)

```
main loop tick (fps Hz)
├─ robot.get_observation()                      # cameras + joints
├─ notify_observation(obs)  ──────────────▶  RTC thread reads latest obs
└─ action = engine.get_action()  = ActionQueue.get()   # pop 1 ready action
   └─ robot.send_action(action)

RTC background thread (free-running)
└─ if ActionQueue.qsize() <= 30:
   ├─ prev = ActionQueue.get_left_over()        # unexecuted tail
   ├─ delay = ceil(prev_latency / (1/fps))
   ├─ preprocessed = preprocessor(build_dataset_frame(obs))
   └─ predict_action_chunk(preprocessed, inference_delay=delay, prev_chunk_left_over=prev)
      └─ _get_action_chunk
         ├─ prepare_images  → SigLIP ViT + connector (per camera)
         ├─ prepare_state   → state_proj
         ├─ sample_actions
         │  ├─ _prefill_prefix → VLM forward(fill_kv_cache=True)   # ONCE
         │  └─ for step in range(num_steps=10):                     # flow matching
         │     └─ RTCProcessor.denoise_step(x_t, prev, delay, execution_horizon, time)
         │        ├─ v_t = expert.forward(fill_kv_cache=False)      # reads prefix cache
         │        ├─ correction = (prev - (x_t - t*v_t)) * prefix_weights
         │        └─ return v_t - guidance_weight * correction
         └─ unpad → (B, chunk_size, action_dim)
      └─ ActionQueue.merge(original, processed, new_delay)          # drop first `delay`, replace
```

---

### One-line summary

`lerobot-rollout` runs a fixed-`fps` loop; SmolVLA turns
`[images+language+state]` into a `chunk_size` action chunk via a VLM prefix
(KV-cached once) + a flow-matching action expert (`num_steps` Euler steps). RTC
moves that inference onto a background thread feeding a thread-safe
`ActionQueue`: the loop pops one action per tick while the thread refills below a
30-action threshold, dropping the first `delay = ceil(latency/tick)` actions of
each new chunk and steering the denoiser toward the leftover prefix so chunks
splice in seamlessly at the robot's true position. Speed (latency, `num_steps`,
precision, torch.compile, KV cache) determines whether the queue ever drains —
which is what turns raw inference speed into smooth, real-time robot control.

---

## 8. The SmolVLA paper / blog (architecture & design intent)

Source: HuggingFace blog *"SmolVLA: Efficient Vision-Language-Action Model
trained on LeRobot Community Data"* (https://huggingface.co/blog/smolvla). The
numbers below are from the blog and are **cross-checked against the actual code**
in this repo (§9 confirms each one).

### 8.1 What SmolVLA is

- A **compact ~450M-parameter** open Vision-Language-Action (VLA) policy designed
  to train and **run on consumer hardware** (single consumer GPU, even
  CPU/MacBook), in contrast to multi-billion-parameter VLAs (e.g. π₀ ≈ 3.3B).
- Two components: a **Vision-Language Model (VLM)** that fuses
  images+language+state, and a small **action expert (~100M)** that outputs
  action chunks via **flow matching**.
- Trained on **< 30k community episodes** (an order of magnitude less data than
  peer VLAs) yet competitive: e.g. **LIBERO ≈ 87.3%** average success, matching
  or beating much larger models.

### 8.2 VLM backbone: SmolVLM2

- **SmolVLM2** = **SigLIP** vision encoder + **SmolLM2** language decoder,
  optimized for multi-image input.
- **Language** instructions are tokenized and fed to the decoder.
- **State** (proprioception / joint positions) is projected by a **single linear
  layer into one token** aligned with the LM token dimension.
- The decoder processes the **concatenated [image ⊕ language ⊕ state] tokens**;
  the resulting features condition the action expert.

### 8.3 Three efficiency techniques (the reason it's small & fast)

1. **Visual-token reduction → 64 tokens/frame.** A 512×512 frame becomes **64
   tokens instead of ~1024**, via **PixelShuffle** (channel-space pixel
   unshuffling) inside the SmolVLM2 connector. Only the **global image** is used
   at runtime (no image tiling), keeping inference light.
2. **VLM layer skipping.** The action expert only attends to VLM features **up to
   a middle layer N** (set to **half** the VLM's layers). Intermediate-layer
   features are often better for downstream control, and this **halves** the VLM
   *and* expert compute. In code this is `num_vlm_layers = 16`.
3. **Interleaved attention in the expert.** Expert layers **alternate
   cross-attention** (action tokens attend to the VLM's cached features) **and
   self-attention** (action tokens attend causally to past action tokens). This
   is lighter and more effective than all-self or all-cross: cross-attn gives
   grounding, causal self-attn gives temporal smoothness. In code this is
   `attention_mode="cross_attn"` with `self_attn_every_n_layers=2`.

### 8.4 Action expert & flow matching

- ~**100M-param** transformer, trained with **flow matching**: it learns a
  velocity field; at inference it integrates from Gaussian noise to a clean
  **action chunk** with a handful of Euler steps (`num_steps`, default 10).
- **Causal masking** enforces temporal consistency across the chunk.
- Output is a chunk of **continuous** control actions (`chunk_size` steps).

### 8.5 Asynchronous inference (the blog's headline system feature)

- Separates **"acting"** from **"perceiving/thinking"**: a **RobotClient**
  continuously executes actions from a **local queue** while a **PolicyServer**
  asynchronously consumes observations and predicts the next chunk — without
  interrupting the robot.
- Reported gains: **~30% faster response** and **~2× task throughput** vs
  synchronous execution.
- In this repo that idea exists in **two concrete forms**: the process-split
  **gRPC** `async_inference/` (RobotClient + PolicyServer, path C) and the modern
  in-process **`RTCInferenceEngine`** background thread (path B). RTC (§3) adds
  chunk-overlap *guidance* on top of the plain async queue so the seams between
  chunks are continuous.

---

## 9. Network architecture — verified against the code

Files: `policies/smolvla/smolvlm_with_expert.py` (the fused VLM+expert),
`modeling_smolvla.py` (policy wrapper), `configuration_smolvla.py` (dims).

### 9.1 The fused `SmolVLMWithExpert` module

`smolvlm_with_expert.py` loads SmolVLM2, **truncates** its language stack, and
builds a **parallel action-expert stack** that runs *alongside* the VLM layers
sharing the same attention step:

```python
# smolvlm_with_expert.py
if num_vlm_layers > 0:                                             # line 100
    self.get_vlm_model().text_model.layers = \
        self.get_vlm_model().text_model.layers[:num_vlm_layers]    # ← LAYER SKIPPING
self.num_vlm_layers = len(self.get_vlm_model().text_model.layers)  # 16

lm_expert_config.num_hidden_layers = self.num_vlm_layers           # expert mirrors VLM depth
...
self.self_attn_every_n_layers = self_attn_every_n_layers           # 2  (interleave SA)
```

- **Layer skipping** is literal list truncation: only the **first
  `num_vlm_layers=16`** decoder layers are kept (SmolLM2-360M-class backbone has
  32 → half). Confirms blog technique #2.
- **Expert width**: hidden size = `VLM_hidden × expert_width_multiplier` with
  `expert_width_multiplier = 0.75` — a *narrower* expert than the VLM. This is the
  ~100M action expert.
- **Expert depth**: `num_expert_layers = -1` ⇒ same depth as the (truncated) VLM;
  if set positive it must divide `num_vlm_layers` evenly (expert layer *i* maps to
  VLM layer block `i * (num_vlm_layers // num_expert_layers)`).

### 9.2 Per-layer attention routing (interleaving) — `forward` (lines ~435–460)

```python
num_layers = self.num_vlm_layers
for layer_idx in range(num_layers):
    if (attention_mode == "self_attn"
        or (self_attn_every_n_layers > 0 and layer_idx % self_attn_every_n_layers == 0)):
        att_outputs, past_key_values = self.forward_attn_layer(...)      # JOINT self-attn
    else:
        att_outputs, past_key_values = self.forward_cross_attn_layer(...) # expert CROSS-attn
```

- `forward_attn_layer` (line 209): a **joint self-attention** over
  concatenated prefix+suffix (used every `self_attn_every_n_layers=2` layers and
  during prefix prefill).
- `forward_cross_attn_layer` (line 286): the expert's action tokens **cross-attend
  to the VLM's KV cache** (the cheap path used on the other layers). Confirms
  blog technique #3.

### 9.3 The KV cache = the interface between VLM and expert

```python
# smolvlm_with_expert.py (cache handling)
if use_cache and fill_kv_cache:
    past_key_values[layer_idx] = {"key_states": k, "value_states": v}   # prefill writes
elif use_cache:                                                         # denoise reads
    k = torch.cat([past_key_values[layer_idx]["key_states"], k], dim=1)
    v = torch.cat([past_key_values[layer_idx]["value_states"], v], dim=1)
```

The VLM prefix (images+language+state) is encoded **once** (`fill_kv_cache=True`);
every denoising step reads that per-layer `{key_states, value_states}` cache
(`fill_kv_cache=False`) and only computes K/V for the small action suffix. This is
exactly why `num_steps` denoise passes are cheap.

### 9.4 Token budget through the network

```
per camera image (512×512)
  └─ SigLIP ViT → patch tokens ─ connector(PixelShuffle) → 64 tokens/frame
language instruction ── tokenizer (≤ tokenizer_max_length = 48 tokens)
robot state ────────── state_proj (Linear) → 1 token
                       ▼
        PREFIX = [ 64·(#cameras) image tokens ⊕ ≤48 language tokens ⊕ 1 state token ]
                       │  encoded once by 16 VLM layers → per-layer KV cache
                       ▼
        SUFFIX = chunk_size (=50) noisy action tokens  (action_in_proj + sinusoidal time emb)
                       │  16 expert layers, cross/self interleaved, read prefix KV cache
                       ▼
        action_out_proj → v_t → Euler update ×num_steps → chunk (B, 50, action_dim)
```

Concrete dims (defaults, `configuration_smolvla.py`): `chunk_size=50`,
`n_action_steps=50`, `num_steps=10`, `resize_imgs_with_padding=(512,512)`,
`max_state_dim=32`, `max_action_dim=32`, `tokenizer_max_length=48`,
`num_vlm_layers=16`, `expert_width_multiplier=0.75`, `self_attn_every_n_layers=2`,
`attention_mode="cross_attn"`, `use_cache=True`,
`vlm_model_name="HuggingFaceTB/SmolVLM2-500M-Video-Instruct"`.

---

## 10. How the total system works (perception → action → motion)

Putting the network (§8–9) and the async RTC loop (§1–3) together, one full
real-time cycle on the robot:

```
        ┌────────────────────────── PERCEPTION (once per chunk) ──────────────────────────┐
 cameras│  N×RGB 512² ─SigLIP─ connector(PixelShuffle→64 tok) ┐                            │
 joints │  state ─ Linear ─ 1 token                            ├─► SmolVLM2 (16 layers) ─► per-layer KV cache
 task   │  language ─ tokenizer ─ ≤48 tokens                   ┘        (fill_kv_cache=True)
        └───────────────────────────────────────────────────────────────────────────────┘
                                            │  frozen prefix KV cache
        ┌──────────────────────────── ACTION EXPERT (flow matching) ───────────────────────┐
        │  x_t = noise (B,50,32)                                                            │
        │  repeat num_steps=10:  v_t = expert(x_t, KVcache; cross/self interleaved)         │
        │                        [RTC] v_t = v_t − g·(prev_tail − (x_t−t·v_t))·prefix_wts   │
        │                        x_t += (−1/10)·v_t                                         │
        │  → action chunk (B,50,action_dim), unnormalized by postprocessor                  │
        └──────────────────────────────────────────────────────────────────────────────────┘
                                            │  chunk
        ┌──────────────────────────── ASYNC DECOUPLING (RTC engine) ───────────────────────┐
        │  background thread:  when ActionQueue.qsize() ≤ 30 → run PERCEPTION+EXPERT above  │
        │                      merge(): drop first delay=ceil(latency·fps) actions, replace │
        │  main loop @ fps:    obs→notify_observation();  action=ActionQueue.get();         │
        │                      robot.send_action(action);  precise_sleep(1/fps − dt)        │
        └──────────────────────────────────────────────────────────────────────────────────┘
                                            │  1 action / control tick
                                       ROBOT MOTORS
```

**Why each piece exists, end to end:**

1. **Perception is expensive but rare.** The 16-layer VLM + SigLIP is the costly
   part, so it is run **once per chunk** and its output is frozen into a **KV
   cache**. Visual-token reduction (64/frame) and layer-skipping (16 layers) make
   even this once-per-chunk cost fit on consumer hardware.
2. **Action generation is cheap and repeated.** The narrow (0.75×) expert reads
   the cache and denoises `num_steps=10` times. Interleaved cross/self attention
   keeps actions both **grounded** (cross-attn to perception) and **smooth**
   (causal self-attn), and flow matching yields a whole **50-step chunk** in one
   shot — one inference amortized over dozens of control ticks.
3. **Async decoupling keeps the robot real-time.** The chunk fills a
   thread-safe **ActionQueue**; the fixed-`fps` control loop only ever pops one
   ready action, so **inference latency never stalls the motors** as long as the
   queue (≈1 s at 30 fps) doesn't drain. This is the blog's "~30% faster / 2×
   throughput" async stack.
4. **RTC makes the seams invisible.** Because inference takes real time, the
   robot has already moved `delay = ceil(latency·fps)` steps by the time a chunk
   is ready; `merge()` **drops** those leading actions, and the denoiser is
   **guided toward the previous chunk's unexecuted tail** on the overlap window
   (`execution_horizon=10`, `LINEAR` prefix weights, `max_guidance_weight=10`).
   The new chunk therefore continues the old trajectory exactly where the robot
   is — no jerk at chunk boundaries.
5. **Speed → performance, concretely.** Lower latency (bf16/fp16 true-half +
   torch.compile of `denoise_step`/`_prefill_prefix`, smaller `num_steps`, KV
   cache) means the background thread refills the queue with more margin, RTC's
   `delay` skip is smaller (less of each chunk wasted), and the achievable
   control `fps` rises. If latency ever exceeds the queue buffer, `get_action()`
   returns `None` and the robot holds position — so **inference speed sets the
   ceiling on real-time control quality**, and everything in §5–6 + the AMD
   patches exists to raise that ceiling on ROCm.

**Sources:**
- [SmolVLA: Efficient Vision-Language-Action Model trained on LeRobot Community Data (HuggingFace blog)](https://huggingface.co/blog/smolvla)
- [blog/smolvla.md (source)](https://github.com/huggingface/blog/blob/main/smolvla.md)
- [SmolVLA docs (LeRobot)](https://huggingface.co/docs/lerobot/smolvla)