# SmolVLA + RTC — Paper Understanding & Reference Notes

Reference notes for writing our gesture-mimic imitation-learning paper. Covers:
(1) a full understanding of the SmolVLA paper (arXiv **2506.01844v1**, Shukor et
al., Hugging Face), (2) the Real-Time Chunking / asynchronous-inference
algorithm in depth, and (3) how all of this maps onto our AMD gesture-mimic
experiment and results. Three threads are kept visible throughout:
**(A) "speed is the new accuracy"**, **(B) imitation learning**, and
**(C) AMD ROCm / GPK systems optimization**.

> Source note: arXiv 2506.01844v1 *is* the SmolVLA paper itself. Page/table
> references below point into that PDF (`confuence/2506.01844v1.pdf`, 24 pp).
> The RTC code details are cross-checked against the pinned lerobot commit
> `c8ce413d...` (see `lerobot_setup_rtc_loop_explantions.md`).

---

## 1. One-paragraph summary

SmolVLA is a **compact (~450M-param) open Vision-Language-Action (VLA)** policy
built to **train on a single consumer GPU and deploy on consumer GPUs/CPUs**. It
reuses a pretrained VLM (**SmolVLM2**: SigLIP vision encoder + SmolLM2 decoder)
for perception and adds a small **action expert (~100M)** trained with **flow
matching** to output **chunks of `n` continuous actions**. It is pretrained with
**imitation learning** on **~23k community episodes** (481 datasets, ~10.6M
frames) — an order of magnitude less data than peers — yet matches or beats VLAs
that are **10× larger** (e.g. π₀ 3.3B). Its headline systems contribution is an
**asynchronous inference stack** that decouples action *execution* from action
*prediction*, giving **~30% faster task completion and ~2× throughput** while
keeping success rate. Efficiency comes from three architectural cuts
(**64 visual tokens/frame**, **use only the first N=L/2 VLM layers**,
**interleaved cross/self-attention** in the expert) plus **bfloat16 +
torch.compile**.

---

## 2. Problem & motivation (paper §1–2)

- Foundation models transformed NLP/vision, but **robotics policies still fail to
  generalize** across objects, positions, environments, tasks — mainly limited by
  **scarce, heterogeneous, high-quality data**.
- Existing VLAs (RT-2, OpenVLA 7B, π₀ 3.3B) are **massive, often proprietary or
  weights-only**, trained on **academic/industrial datasets**, and require
  **costly robot platforms** — hurting reproducibility and accessibility.
- SmolVLA's thesis: a **small, efficient, fully open** VLA trained on
  **community-collected data** from **affordable robots (SO-100/SO-101)** can be
  competitive — and can be made **fast enough to run in real time on cheap
  hardware**.
- Three stated contributions:
  1. **Lightweight architecture** (layer skipping, few visual tokens, small VLM,
     interleaved SA/CA).
  2. **Community-driven pretraining** (<30k episodes, ~10× less data than prior
     art).
  3. **Asynchronous inference** decoupling execution from prediction → lower
     latency, faster control.

> **(B) Imitation-learning hook for our paper:** SmolVLA is *pretrained with
> imitation learning* on teleoperated demonstrations, and the paper explicitly
> lists "imitation vs. RL" as a limitation (§5.1) — our master/slave teleop
> gesture-mimic dataset is exactly this imitation-learning regime, so we sit
> squarely in SmolVLA's intended use.

---

## 3. Architecture (paper §3.1, Fig. 1) — with all numbers

Two interconnected components: a **VLM (perception)** and an **action expert
(control)**. The VLM encodes `[images ⊕ language ⊕ state]`; its features
condition the expert; the expert outputs actions that change the state fed back
to the VLM.

### 3.1 VLM backbone — SmolVLM2
- **SmolVLM2** = **SigLIP** vision encoder + **SmolLM2** language decoder,
  optimized for multi-image input.
- **Language** instruction → tokenized → decoder.
- **State** (proprioception) → **single token** via a linear projector (matches
  LM token dim).
- **Images** → vision encoder → **token-shuffle (PixelShuffle)** reduces tokens.
- Concatenated visual+language+state tokens go through the decoder; output
  features condition the expert.

### 3.2 Three efficiency techniques (the reason it's small & fast)
1. **Visual-token reduction → 64 tokens/frame.** No image tiling at runtime
   (only the **global image**); a **pixel-shuffle** compresses a 512×512 frame to
   **64 tokens** instead of ~1024. (paper §3.1 "Visual tokens reduction")
2. **VLM layer skipping → N = L/2.** The expert only attends to VLM features up
   to a middle layer **N = half the total layers**. Intermediate features are
   often better for downstream tasks; this **halves** both VLM and expert
   compute. In our code: **first 16 layers** of the LLM. (paper §3.1 "Faster
   inference through layer skipping"; ablation Table 8)
3. **Interleaved cross/self-attention in the expert.** Each expert block is
   **either** a **cross-attention** layer (action tokens attend to the VLM's
   cached KV) **or** a **causal self-attention** layer (action tokens attend to
   past action tokens). Cheaper and better than all-CA or all-SA. (paper §3.1;
   ablation Table 6)

### 3.3 Flow-matching action expert (paper §3.1 "Flow matching action expert")
- Expert `v_θ` predicts an action chunk `A_t = (a_t,…,a_{t+n})` from VLM
  features, using a **conditional Flow-Matching Transformer**.
- Training objective:
  `L(θ) = E[ || v_θ(A_t^τ, o_t) − u(A_t^τ | A_t) ||² ]`, with
  `A_t^τ = τ·A_t + (1−τ)·ε`, `ε ~ N(0, I)`, and target vector field
  `u = ε − A_t`. `τ` sampled from a **Beta distribution** (following π₀).
- **Reduced expert width = 0.75 × VLM hidden dim** for inference efficiency
  (ablation Table 9).
- Interaction with VLM is via attention: CA layers cross-attend to VLM K/V; SA
  layers use a **causal mask** so an action token only sees **past** tokens in
  the chunk (prevents future leakage; ablation Table 7).

### 3.4 Key dimensions (defaults, cross-checked with code)
| Item | Value |
|---|---|
| Total params | ~450M (100M expert, ~350M VLM) |
| VLM backbone | SmolVLM2-500M (SigLIP + SmolLM2) |
| LLM layers used | first **16** (N = L/2) |
| Visual tokens/frame | **64** (pixel shuffle, global image only) |
| Expert width | **0.75×** VLM hidden dim |
| Attention | interleaved **CA + causal SA** |
| Action chunk size `n` | **50** |
| Flow-matching steps (inference) | **10** |
| Image size | 512×512 |
| Precision | **bfloat16** + `torch.compile` |
| State/action pad dim | 32 / 32 |

---

## 4. Pretraining data — community imitation-learning corpus (paper §3.2)

- **481 community datasets** from Hugging Face, filtered by embodiment, episode
  count, quality, frame coverage → **22.9K episodes**, **10.6M frames**
  (Table 1). Still **~10× smaller** than prior VLA corpora (OpenVLA ≈ 1M traj).
- **Task-annotation cleanup:** community task strings are noisy/vague
  (`task desc`, `Hold`, `Up`, or missing). They used an off-the-shelf VLM
  (**Qwen2.5-VL-3B-Instruct**) to auto-generate concise action-oriented task
  descriptions from sampled frames.
- **Camera-viewpoint normalization:** camera naming is inconsistent across
  datasets (`images.laptop` could be top/side/wrist). They **manually mapped**
  each camera to standardized views → **OBS_IMAGE_1 (top), OBS_IMAGE_2 (wrist),
  OBS_IMAGE_3 (side)**; extra views dropped.

> **(B) Imitation-learning hook:** all pretraining data is **teleoperated
> demonstrations** — the same paradigm as our master→slave arm collection. Our
> gesture-mimic dataset (2000 episodes, multi-person, varied backgrounds) is a
> single-embodiment imitation-learning fine-tuning set on top of this.

---

## 5. Asynchronous inference & the RTC algorithm (paper §3.3, Fig. 2–3, Alg. 1)

This is the section most central to our "**speed is accuracy**" story.

### 5.1 The problem with synchronous (chunked) inference
- Modern visuomotor policies output **action chunks** `A_t = π(o_t)` of `n`
  low-level commands queued from **one** observation `o_t`.
- **Sync (open-loop) inference:** robot **executes the entire chunk `A_t`**
  before capturing a new observation `o_{t+n}` and predicting the next chunk.
  - Efficient (one inference per `n` steps) **but**:
    - The robot runs **open-loop for `n` steps** → cannot react to changes.
    - While computing the next chunk the robot is **idle / lagging** ("blind
      lag") → average **E[ℓ_S] idle seconds** per cycle.
- **Fully reactive (`g=1`) inference:** send an observation **every timestep**.
  Maximally reactive **but** needs continuous inference → **prohibitive on
  edge/limited hardware**.

### 5.2 The async solution (Real-Time Chunking)
Decouple **execution** from **prediction** across two roles:
- **RobotClient**: runs the robot, **executes actions from a local queue** at a
  fixed control rate — never blocks on inference.
- **PolicyServer** (can be a remote/more-powerful machine, e.g. a GPU box):
  **asynchronously consumes observations and predicts the next chunk**.

Chunk prediction is **triggered while the current queue is still being
consumed**, and the new chunk is **aggregated** onto the overlap with the old
one → the loop between prediction and execution is tightened without paying the
full cost of `g=1`.

### 5.3 Algorithm 1 — Asynchronous inference control loop (paper p.6)
Inputs: horizon `T`, chunk size `n`, **threshold `g ∈ [0,1]`**.

```
capture o_0; send o_0 to PolicyServer; receive A_0 = π(o_0)
for t = 1..T:
    a_t ← PopFront(A_t)              # execute next action from the queue
    Execute(a_t)
    if |A_t| / n  <  g:             # queue has dropped below the threshold
        capture new observation o_{t+1}
        if NeedsProcessing(o_{t+1}):     # joint-space similarity filter
            async_handle ← AsyncInfer(o_{t+1})   # NON-blocking chunk prediction
            Ã_{t+1} ← π(o_{t+1})                 # new chunk (arrives later)
            A_{t+1} ← f(A_t, Ã_{t+1})            # aggregate over overlap
    if NotCompleted(async_handle):
        A_{t+1} ← A_t               # keep consuming old queue until new one ready
```

Two control knobs:
- **`g` (queue threshold)** — refill when the remaining fraction of the queue
  drops below `g`. Governs the reactivity/compute trade-off.
- **Observation similarity filter (`NeedsProcessing`)** — skip near-duplicate
  observations (joint-space distance below `ε`) to avoid redundant server calls;
  **but** when the queue actually empties, the latest observation is processed
  **regardless** of similarity ("must-go").

### 5.4 The `g` regimes (paper §3.3, Fig. 3) — key for the speed argument
- **`g = 0` (sequential limit):** drain the whole chunk before sending a new
  obs. During round-trip latency the queue is empty → robot **idle** ("incapable
  of acting"), avg **E[ℓ_S] idle seconds**. = worst reactivity (this is basically
  sync).
- **`g = 0.7` (async sweet spot):** consume ~`1−g = 0.3` of a chunk, then trigger
  the next prediction → amortizes compute **and** keeps the queue from emptying.
  Overlap gives a buffer against model error.
- **`g = 1` (compute-intensive limit):** send an obs **every** timestep → queue
  almost always full, maximally reactive, **but** one forward pass per control
  tick → too expensive on limited hardware.
- Analytical result: to **avoid idle queues**, need
  **`g ≥ E[ℓ_S]/Δt / n`**, where `Δt` = control period (33 ms at 30 fps) and
  `E[ℓ_S]` = inference latency. **Lower latency `ℓ_S` ⇒ smaller required `g` ⇒
  cheaper to stay reactive.** This is the formal link between **latency and
  reactivity**.

> **(A) Speed-is-accuracy hook:** the paper proves reactivity depends on
> `latency / (n·Δt)`. Our AMD latency cuts (§8) shrink `ℓ_S`, which either lets
> us lower `g` (fewer inferences) or, at fixed `g`, buys a bigger safety margin
> so the queue never starves — i.e. faster model ⇒ more reactive ⇒ better mimic.

### 5.5 Async results (paper §4.6, Fig. 5)
- Same **success rate** sync vs async, but async is:
  - **~30% faster** task completion (9.7 s vs 13.75 s on Pick-Place).
  - **~2× throughput** in fixed time (**19 vs 9** cubes placed in a fixed window).
  - **More robust** to object-position shifts / disturbances (faster reactions).

### 5.6 Relation to our lerobot RTC engine
Our stack uses the **in-process `RTCInferenceEngine`** variant of this idea (a
background thread + thread-safe `ActionQueue`) rather than the gRPC 2-process
form, plus **chunk-overlap guidance** (steer the denoiser toward the previous
chunk's unexecuted tail) and **latency-based delay skipping** (drop the first
`ceil(latency/Δt)` actions of each new chunk). Full code-level detail is in
`lerobot_setup_rtc_loop_explantions.md`. Map to Algorithm 1:
- `g` ↔ our `rtc_queue_threshold` / `chunk_size_threshold`.
- `f(A_t, Ã_{t+1})` aggregation ↔ RTC prefix-guidance + `merge()`/delay-skip.
- `NeedsProcessing` ↔ observation similarity filter (must-go on empty queue).

---

## 6. Experiments & main results (paper §4)

### 6.1 Setup
- **Framework:** LeRobot (PyTorch). **Pretrain:** 200k steps, global batch 256,
  LR 1e-4 cosine → 2.5e-6, AdamW, 512×512 images, **4 GPUs, ~30k GPU-hours**
  total (but trainable on a single GPU due to small size).
- **Trainable:** only the **action expert** (~100M); **VLM frozen**; first **16**
  LLM layers used. **Fine-tune:** 100k steps (sim) / 200k (real), batch 64.
- **Inference:** flow matching fixed to **10 steps**. Real-world eval uses **sync**
  inference; async studied separately.
- **Efficiency:** bfloat16 + `torch.compile`, fixed sequence length (drop
  excess frames so batches are complete).

### 6.2 Simulation (Table 2)
- **LIBERO:** SmolVLA-0.45B avg **87.3%** (vs π₀ 3.3B 86.0, OpenVLA-7B 76.5,
  Diffusion Policy 72.4). SmolVLA-2.25B → **88.75%**.
- **Meta-World:** SmolVLA-0.45B avg **57.3%**; 2.25B → **68.24%** (beats π₀,
  TinyVLA, Diffusion Policy).
- **~40% faster to train and 6× less memory than π₀.**

### 6.3 Real-world (Tables 3–5)
- **SO-100 multi-task** (Pick-Place / Stacking / Sorting): SmolVLA-0.45B avg
  **78.3%** vs π₀-3.5B 61.7 and ACT (single-task) 48.3 — **beats a 7× larger
  model**.
- **SO-101** (never pretrained on SO-101 data): beats ACT in-distribution
  (90 vs 70) and OOD (50 vs 40) → **cross-embodiment fine-tuning works**.
- **Pretraining + multitask ablation (Table 5):** community pretraining lifts
  avg **51.7 → 78.3**; multitask fine-tuning adds further gains.

### 6.4 Ablations (paper §4.7) — the ones we should cite
| Ablation | Finding | Table |
|---|---|---|
| CA vs SA vs **CA+SA** | interleaved **CA+SA best** (85.5 avg) | 6 |
| Attention mask | **causal** > bidirectional (no future leakage) | 7 |
| VLM layer skipping | **skip to N=L/2** beats downsizing the VLM | 8 |
| Expert width | **0.75×** good speed/accuracy balance | 9 |
| Objective | **flow matching** > L1 regression | 10 |
| State placement | feed state to **VLM (prefix)** > to expert (suffix) | 11 |
| **Action chunk size `n`** | **10–50 best**; `n=1` and `n=100` degrade | **12** |
| **Executed actions before re-obs** | **fewer is better**: 1→80.3, 10→82.8, 30→70.8, **50→51.8** | **13** |

> **(A) The single most important table for our paper is Table 13.** It shows
> that consuming **more actions from a stale chunk before re-observing collapses
> accuracy** (50 steps → 51.8% vs 1 step → 80.3%). This is *exactly* our observed
> behavior (§7): consume 1 action = great, consume all 50 = very bad. Table 12
> (chunk size) and Table 13 (execution horizon) together are the empirical core
> of "speed is the new accuracy."

---

## 7. How this maps to our gesture-mimic experiment

**Task.** A human waves a hand (up/down, left/right, wrist open/close) in front of
a camera; an **SO-101 arm on LeRobot** must **mimic** the gesture in real time.

**Data (imitation learning, master→slave teleop).** 2000 episodes, multiple
people, varied backgrounds. A **master arm** (human-operated, watching the
person) drives a cable-linked **slave arm** whose motors copy the master exactly;
we log **(camera image → slave action vector)** pairs. This is textbook
**imitation learning** — the model learns to reproduce the demonstrator's
control from vision.

**Models fine-tuned.** SmolVLA, ACT, π₀.5. **Metric:** **MAE** between predicted
and ground-truth trajectories (lower = better; usability limit ≈ **3.5**).

**Why speed matters here (task-specific).** Because the target is a *live* human
gesture, **faster inference ⇒ more input frames processed ⇒ more reactive ⇒
tighter operator↔robot sync**. A slow model must predict far into the future from
**stale** frames → long-horizon predictions are unreliable → the robot mimics
what the human did *seconds ago*. This is the applied form of the paper's
`g ≥ E[ℓ_S]/(n·Δt)` result.

**The chunk-consumption effect (our data confirms Table 13).** From `report1.md`
(fp16, ~65 ms latency), MAE vs number of consumed action states:

| Action states consumed | MAE |
|---|---|
| 1 | 3.28 |
| 2 | 3.43 |
| 4 | 4.29 |
| 5 | 4.56 |
| 10 | 4.80 |
| 20 | 6.21 |
| 30 | 12.09 |
| 40 | 23.07 |

→ Same monotonic collapse as SmolVLA Table 13. **Consuming 1 fresh action per
inference is far more accurate than draining the chunk.** In our RTC model the
queue cap is 10, and **if a new prediction lands before the old queue drains, the
stale actions are overwritten** — so **lower latency directly yields lower MAE**
(the "fastest model is the most accurate" observation in `report1.md`).

---

## 8. AMD ROCm / GPK systems optimizations (our contribution — thread C)

The paper ships only **bfloat16 + `torch.compile` on the flow-matching diffusion
loop**. Our work extends the systems side for AMD **Strix/GPK** boards:

| # | Optimization | Effect | Throughput |
|---|---|---|---|
| 1 | **Diffusion steps 30 → 2** (extra steps unnecessary for this task) | fewer expert passes | 2 → 4.5–5 inf/s |
| 2 | **torch.compile of the WHOLE flow** — rewrote LeRobot SmolVLA modules so the **encoder + LLM prefix prefill** also compile (not just `denoise_step`) → single graph | fused kernels, no per-layer Python | → 8.5 inf/s |
| 3 | **fp32 → fp16, cast *before* compile** (critical on ROCm — casting after compile inserts up/down-scale ops around every layer and eats the win) | half memory/compute | → 13–15 inf/s |
| 4 | **RTC on** — camera pipeline + model on parallel threads sharing the GPU | reactive end-to-end | reactivity ↑ |
| 5 | **`chunk_size_threshold` ↓ (refill after 5 consumed)** — fresher images drive predictions | tighter loop | reactivity ↑ |
| 6 | **Action smoothing** — causal moving-average / EMA post-filter on the action stream (see `smooting.md`) | removes jitter/friction, no retraining | smoothness ↑ |
| 7 | **More data + fine-tune (single→3ch→2k data→gradient-bg)** | | MAE 6 → ~3 |
| — | **3-camera → single-camera input** (task uses one camera; other 2 channels wasted) | less compute, better acc | speed ↑ + acc ↑ |

**Net:** ~**7× throughput** (2 → 13–15 inf/s) and ~**50% lower MAE** (6 → ~3,
under the 3.5 usability limit). Best deployable config from `report1.md`:
**`nocg-full` (max-autotune-no-cudagraphs, compile_full=1) + fp16**, ~**65 ms**
standalone latency at 15 fps; fp32 hits 30 fps@~31 ms but isn't real-time on GPK.

**Compile-mode findings (report1.md, action steps=10):**
- fp16: nocg-full 65 ms / MAE 4.80; reduce-overhead 77 ms / 4.60; eager 86 ms / 5.02.
- bf16: reduce-overhead 77 ms / 4.75; eager 91 ms / 5.03; nocg-full 103 ms / 5.01.
- **fp16 + nocg-full = lowest latency**; cold-start full-graph compile is expensive (one-time).

**Version progression (reports 3–6):**
- **v1** — diffusion 30→2, compiled graph, fp16 (1000 eps).
- **v1.1** — + single-channel processing → **~31 ms @ 30 fps**, MAE improvements.
- **v2** — 2000-episode raw data → best MAE (e.g. 10 states 3.94 → **2.78**);
  behavioral eval: "**stable and smooth**", preferred release.
- **v3.0** — + YOLO gradient-background fine-tuning; behaviorally poorer
  (stability/smoothness down) → **v2 recommended**.
- Control-loop FPS (report6): eager control loop ~27 fps; performant inference up
  to ~21.5 fps (v2).

---

## 9. Baselines to compare against (paper §4.4)

- **π₀ (3.3B)** — VLM (Paligemma) + flow matching, pretrained on 10k h
  cross-embodiment data; 3 RGB + state + language. Strong but heavy.
- **ACT (~80M)** — CVAE with ResNet encoder + enc-dec transformer, regression
  objective, action chunks; trained from scratch per task.
- (sim also vs Octo, OpenVLA-7B, Diffusion Policy, TinyVLA.)
- We already fine-tuned **SmolVLA, ACT, π₀.5** on gesture-mimic → direct
  three-way comparison available.

---

## 10. Limitations the paper admits (paper §5.1) — useful framing for our novelty

- Pretraining uses a **single robot type (SO-100)**; cross-embodiment data likely
  needed for broad generalization.
- **Dataset small** (~23k traj vs OpenVLA ~1M) — more data would help.
- **VLM backbone pretrained on doc/OCR** — maybe not optimal for robotics.
- **Short-horizon tasks only** — long horizon needs hierarchy/planning.
- **Imitation learning only** — RL is future work.
→ Our paper can position gesture-mimic as: a **new task/embodiment (SO-101,
live-human reactive mimic)**, a **latency-first deployment on AMD hardware**, and
an empirical deep-dive on the **latency ↔ reactivity ↔ accuracy** coupling that
the SmolVLA paper only touches via `g`.

---

## 11. Ready-to-use claims/citations for the paper

1. **Architecture** — 450M params; SmolVLM2 (SigLIP+SmolLM2); 64 visual tokens
   via pixel shuffle; first N=L/2 (16) LLM layers; interleaved CA+causal-SA;
   0.75× expert; flow matching; chunk n=50; 10 diffusion steps. (paper §3.1,
   Tables 6–13)
2. **Data** — 481 community datasets, 22.9K episodes, 10.6M frames; VLM-auto task
   relabeling; camera-view normalization. (paper §3.2, Table 1)
3. **Async/RTC** — Algorithm 1; threshold `g`; idle-avoidance condition
   `g ≥ E[ℓ_S]/(n·Δt)`; ~30% faster, 2× throughput. (paper §3.3, §4.6, Fig. 2–3,
   5)
4. **Speed↔accuracy** — chunk size 10–50 best (Table 12); **execution horizon:
   1→80.3%, 50→51.8%** (Table 13) — mirrored by our MAE-vs-action-states table.
5. **Efficiency vs π₀** — ~40% faster train, 6× less memory; competitive/better
   success at ~1/7 the params. (paper §4.5)
6. **Our systems delta (AMD)** — diffusion 30→2, full-graph torch.compile
   (encoder+prefill, not just denoise), compile-aware fp16, single-camera, RTC
   threshold=5, action smoothing → ~7× throughput, ~50% lower MAE.

---

## 12. Open questions / things to nail down before writing

- Exact **latency numbers per optimization step** on GPK (we have inf/s ladder;
  add ms + control-loop fps from report6).
- **Three-way SmolVLA vs ACT vs π₀.5** MAE table on gesture-mimic (referenced in
  background; collect final numbers).
- Whether to report **seen vs unseen speaker** generalization (current val is
  "seen speaker"; unseen would strengthen the paper).
- Formalize our **RTC-with-guidance + delay-skip** as a small extension of
  Algorithm 1 (aggregation function `f`), since upstream lerobot RTC differs from
  the paper's gRPC description.

---

### Companion file
- Code-level RTC / async control-loop internals (lerobot commit `c8ce413d`):
  `../GTAC2026-gesture_mimic/` and
  `/home/AMD/hvydana/Workspace/physical_ai_sdk/models/smolVLA/lerobot_setup_rtc_loop_explantions.md`.