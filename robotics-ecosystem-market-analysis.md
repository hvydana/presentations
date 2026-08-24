# Robotics & Physical AI: Layered Tech Ecosystem Gap Analysis
*Research date: 2026-08-11 | Sources: ~50 live web pages across 12 search passes*

## How to read this report

You asked to look at **any robotic application as a stack of layers — from compute up to use case — and, at each layer, ask: where does the AI come from, where do the models come from, where does infrastructure come from, what is open vs. closed source, where are the bottlenecks, and what are the opportunities, risks, and convergences.**

This report is organized exactly that way. It first sizes the market and maps the players, then walks **seven layers of the stack bottom-to-top**, and for each layer gives you: who supplies it, open vs. closed source, the bottleneck, and the opportunity. It closes with cross-cutting gaps, convergences, and risks.

---

## Executive Summary

Robotics is having a "ChatGPT moment" — NVIDIA's Jensen Huang said exactly that at CES 2026 [11]. Capital agrees: robotics startups raised **$18.8B in H1 2026 alone**, already beating all of 2025 ($13.8–27.6B depending on definition) and the 2021 peak [11]. But the excitement masks a stack that is **lopsided**: intelligence (the "robot brain") is advancing fast and is increasingly open, while the **physical layer — actuators, precision reducers, roller screws, tactile sensors, rare-earth magnets — is the true bottleneck, and it is ~65% controlled by China** [7][8].

The single most important structural fact: **the value is migrating up the stack toward the software/intelligence layer** ("if one software layer can run any robot, whoever owns that layer collects recurring revenue across every deployment") [11], **while hardware is commoditizing faster than expected** — Unitree dropped a humanoid to $5,900 in July 2025 [3]. This creates a classic "picks-and-shovels" dynamic where the durable moats are (a) the foundation model + data flywheel, (b) NVIDIA's compute+simulation lock-in, and (c) control of the physical supply chain.

The biggest *open* gap across the entire stack is **data**: action-paired sensorimotor data does not exist at internet scale. The largest open robot dataset is ~1M episodes vs. trillions of text tokens for LLMs [6]. Everything else — world models, simulation, teleoperation rigs, cross-embodiment learning — is ultimately an attempt to route around this one gap.

---

## Market Overview

| Segment | 2025 | 2026 | Forecast | CAGR | Source |
|---|---|---|---|---|---|
| **Total robotics** | ~$73–79B | ~$88–93B | $218–421B (2031–35) | ~15–20% | [1][10] |
| **Humanoid robots** | $2.4–7.8B | $3.9–10.7B | $40–249B (2033–36) | 28–50% | [1] |
| **Humanoid/embodied AI** | $3.77B | — | $34.4B (2033) | 29.5% | [1] |
| **Autonomous Mobile Robots (AMR)** | $3.1–4.5B | $2.75–5.2B | $7–17B (2031–35) | 14–20% | [10] |

**Key reading of the numbers:**
- The **variance is enormous** (humanoid 2025 baseline ranges $2.4B → $7.8B; CAGRs 28% → 50%) because firms define "the market" differently. Treat these as directional, not precise [1].
- **Software is the fastest-growing component** inside humanoids (>45% CAGR), even though hardware captures most current value [1]. This is the "value migrating up the stack" thesis in a single stat.
- **China dominance:** ~75% of humanoid companies are Asia-based; China controls ~63% of key components and builds ~65% cheaper [3].
- **Geography:** North America led humanoid revenue (43% in 2025) but Asia-Pacific is fastest-growing; China humanoid market projected 47.6% CAGR to 2030 [1].

---

## The Seven-Layer Stack (compute → use case)

Think of every robotic application — a warehouse AMR, a surgical arm, a humanoid folding laundry — as the same seven layers stacked on top of each other. Below, each layer answers your core questions.

### Layer 1 — Compute / Silicon (the "brain hardware")

**What it is:** the onboard chip that runs perception + policy inference in real time, plus the datacenter GPUs used to train.

**Where it comes from:**
- **NVIDIA is the de facto monopoly at both ends.** Onboard: **Jetson AGX Thor** (Blackwell architecture, launched Aug 2025) delivers 2,070 FP4 TFLOPS in a 40–130W envelope — 7.5× the AI perf of the prior Orin [5]. It is the announced brain for Boston Dynamics Atlas, Agility Digit (gen 6), Figure, 1X, Amazon Robotics, Boston Dynamics, FANUC [5].
- **Training:** NVIDIA datacenter GPUs, same as the LLM world.
- **Challengers (all niche in humanoids):** Qualcomm Snapdragon Ride (300 TOPS, strong in *automotive* L2–L4, not humanoids); Intel Habana Gaudi; **AMD/Xilinx adaptive SoCs** for edge AI [5].

**Open vs. closed:** Silicon is closed. But NVIDIA's *moat is software, not the chip* — the CUDA + Isaac + Cosmos + Metropolis + Holoscan stack, 2M+ developers, 150+ hardware partners [5].

**Bottleneck:** Power/thermal envelope on a battery-powered mobile robot; and NVIDIA ecosystem lock-in. On-device compute is now *good enough* to run VLA models locally — that's the recent unlock [5].

**Opportunity:** (a) A credible **non-NVIDIA edge inference chip** for robotics with an open toolchain — this is the single biggest "everyone depends on one vendor" gap in the stack. (b) Power-efficient inference silicon tuned specifically for VLA/diffusion-policy workloads (which are inference-heavy and latency-sensitive). This is a natural opening for AMD.

---

### Layer 2 — Actuation, Sensors & Physical Hardware (the "body")

**This is the real bottleneck of the entire industry.**

**Bill of materials breakdown for a humanoid** [7]:
- **Actuators: 40–60% of BOM** (a humanoid needs 40–70 of them)
- Sensing/perception: 10–20%
- Compute/control: 10–15%
- Structure: 5–10%
- Battery: 5–10%

**Where it comes from & the specific chokepoints:**
- **Harmonic / strain-wave drives:** near-monopoly. Japan's **Harmonic Drive Systems (35.5% share) + Nabtesco** dominate; each humanoid needs up to 44. China's **Suzhou Green Harmonic** (25%+ China share, 30–40% cheaper) is Tesla Optimus's supplier, scaling to 500K units/yr in 2026 [7].
- **Planetary roller screws — the "surprising" bottleneck.** As OEMs shift to linear actuators, these become the acute chokepoint: 3-micron thread tolerances, $1,350–2,700 *each*, Optimus uses 14 (~19% of robot cost). Narrow supplier base (SKF, GSA, Rollvis) [7].
- **Six-axis force/torque + tactile sensors:** calibration-intensive, low automation. ATI (US) + Schunk (Germany) own ~half the six-axis market. **Tactile sensing is called "the largest open platform opportunity in humanoid robotics today"** [7].
- **Rare-earth NdFeB magnets — the deepest upstream dependency:** China controls ~69% of mining, ~90% of processing. A humanoid uses 2× the magnet material of an EV motor. Musk has publicly flagged magnet supply as limiting Optimus [7].

**Open vs. closed:** Entirely closed/proprietary hardware; no meaningful "open source" analog except open *designs* (e.g., academic hands).

**The key nuance (McKinsey):** Most bottlenecks are **not raw capacity but qualifying robotics-grade components** — compact, high-durability, low-clearance subsets of parts that Bosch Rexroth/THK/Hiwin already make at scale [7].

**Opportunity:** (a) Western/allied **actuator and roller-screw manufacturing** ("America lost robotics at the actuator" [7]) — a re-shoring / friend-shoring play with strategic tailwinds. (b) **Tactile skin as a horizontal component platform** sold to all OEMs. (c) Rare-earth-free / reduced-magnet motor designs.

**Risk:** Anyone building a robot business on Chinese actuators inherits export-control and geopolitical exposure. Expect **supply-chain regionalization** — parallel China vs. Western hardware ecosystems [7].

---

### Layer 3 — OS / Middleware / Real-Time Control (the "nervous system")

**Where it comes from:**
- **ROS 2 is the open-source standard scaffolding** — DDS middleware, QoS, real-time, security primitives [4].
- Standard open components layered on ROS 2: **Nav2** (navigation), **MoveIt 2** (manipulation/motion planning), **ros2_control** (controllers), **Open-RMF** (fleet management) [4].

**Open vs. closed:** This layer is **healthily open source** — the one layer where open dominates and works well. Backed by Open Robotics.

**Bottleneck:** Real-time guarantees on legged/dynamic systems; the DDS/RMW layer's complexity; integration tax.

**Opportunity:** Real-time control middleware purpose-built for high-DOF humanoids (whole-body control) rather than retrofitted arm/AMR tooling. Tooling that removes the "workspace setup tax."

---

### Layer 4 — Simulation & World Models (the "training gym" and the sim-to-real bridge)

This layer exists to manufacture the data that reality can't provide. **Two philosophies are competing:**

**Simulators (open vs. closed):**
- **MuJoCo** — open source (Apache 2.0, DeepMind). The research standard for contact-rich manipulation, humanoids, legged locomotion. MJX runs on GPU/TPU (reported ~10,000× speedups) [4].
- **NVIDIA Isaac Sim / Isaac Lab** — **went open source in 2025 (Isaac Sim 5.0)**. Photorealistic RTX, PhysX, OpenUSD, ROS 2 bridge; Isaac Lab parallelizes thousands of RL environments [4].
- **Gazebo** — open source, deepest native ROS 2 integration [4].

**World Foundation Models (the newer, higher layer):**
- **NVIDIA Cosmos** — world models as a **synthetic-data multiplication engine**. Cosmos 3 (mid-2026) is an open omnimodal model (text/image/video/audio/action). Downloaded 2M+ times; adopters include Figure, Agility, Skild, 1X (training NEO Gamma), Uber [9].
- **Genesis AI (Genesis World 1.0)** — world model as an **evaluation engine first**. Claims a 166-hour real-robot eval compressed to ~30 min in sim, with **~0.90 Pearson correlation to real hardware** ("zero-shot real-to-sim") [9].

**Where AI comes from here:** NVIDIA (Cosmos), Genesis, and the open MuJoCo/Isaac ecosystems. This is increasingly **open at the model level** — a genuine shift.

**Bottleneck:** The **sim-to-real gap** on contact-rich tasks. Simulation generates millions of cheap episodes but fails on friction/contact physics [6][9].

**Opportunity:** Verticalized, high-fidelity sim environments for specific domains (surgery, agriculture, kitchens); sim-to-real *evaluation* as a service (Genesis's bet); benchmarking/eval infrastructure (still immature).

**Convergence:** This is where **autonomous-vehicle tech and robotics merge** — Cosmos serves both AVs and robots with the same world models [9].

---

### Layer 5 — Data & the Training Flywheel (the scarce fuel)

**This is the industry's #1 gap.** "Data is the bottleneck in embodied AI because action-paired sensorimotor data does not exist at internet scale" [6].

**The scale mismatch:** 3.9M industrial robots operate globally, yet the largest open manipulation dataset (Open X-Embodiment) is ~1M episodes — vs. trillions of tokens for LLMs [6]. Physical Intelligence collected ~10,000 hours over a year to train π0 [2].

**Where data comes from (three sources, all imperfect):**
1. **Teleoperation** — highest fidelity, zero embodiment gap, but only **5–50 episodes/operator-hour at >$100/hr**. Rigs: ALOHA, GELLO, phone-teleop [6].
2. **Simulation** — millions of cheap episodes, but sim-to-real gap [6].
3. **Human video** — scales effortlessly, but no action labels + embodiment gap [6].
Production pipelines blend all three.

**Open vs. closed:**
- **Open:** **Open X-Embodiment** (1.4M episodes, 22 robots, 21-institution consortium) [2][6]; **Hugging Face LeRobot** — the standardizing framework, now **16K+ datasets from 2,200+ contributors** as of Sept 2025 [6]. Formats: LeRobot v2 (Parquet+MP4), HDF5, RLDS [6].
- **Closed:** Every well-funded lab's proprietary teleoperation corpus is its real moat (Physical Intelligence, Skild, Figure, Tesla).

**The key unlock — cross-embodiment learning:** training one model on many robot bodies makes it better on *each* body than a body-specific model. Open X-Embodiment's RT-X showed ~50% positive transfer across morphologies [2].

**Bottleneck evolution:** "The bottleneck has shifted from 'we have no way to share data' to 'we do not have enough diverse data to share'" [6].

**Opportunity:** This is the richest gap in the whole stack — **data-collection-as-a-service, cheaper teleoperation rigs, human-video-to-action label pipelines, and shared data marketplaces.** Whoever solves diverse-data-at-scale owns the flywheel.

---

### Layer 6 — Foundation Models / The "Robot Brain" (VLA & embodied reasoning)

This is the fastest-moving, most-hyped, and (surprisingly) **increasingly open** layer.

**The architecture that won: Vision-Language-Action (VLA)** — a multimodal model that takes camera + language instruction and directly outputs robot actions [2].

**Where the models come from (the landscape):**

| Model | Owner | Open/Closed | Significance |
|---|---|---|---|
| **RT-2** | Google DeepMind | Closed | First major VLA (2023); actions-as-tokens; needed proprietary 55B + robot fleet [2] |
| **OpenVLA** | Academic | **Open (7B)** | Democratized VLAs; a single A100 fine-tunes it in <24h; beat 55B RT-2-X [2] |
| **π0 / π0.5 / π0.6** | Physical Intelligence | Partially open | Flow-matching for dexterity; the "ResNet of VLAs"; $400M+ raised; π0.5 tidies unseen homes [2] |
| **Gemini Robotics 1.5/2 + ER** | Google DeepMind | Closed (SDK/on-device access) | "Thinking" VLA + embodied-reasoning brain; **GR2 controls whole humanoid body under one policy** [12] |
| **Gemini Robotics On-Device** | Google DeepMind | Closed but local | Runs on-robot; fine-tune with **50–100 demos**; ported to Franka + Apollo humanoid [12] |
| **NVIDIA GR00T** | NVIDIA | Open | Humanoid foundation model (uses Fourier GR1 data) [2] |
| **Cosmos 3** | NVIDIA | **Open** | Omnimodal world+action model [9] |
| **Helix** | Figure AI | Closed | First VLA purpose-built for humanoid whole-body control [2] |
| **SmolVLA** | Hugging Face | **Open (500M)** | Edge-efficient; 50× less inference compute; 15–30Hz on an RTX 4090 [2] |
| **Skild Brain** | Skild AI | Closed | Trained on 100,000 simulated robots; $14B valuation Jan 2026 [2][11] |
| **GENE-26.5** | Genesis AI | Closed | Human-scale dexterous-hand foundation model [9] |

**Where the AI comes from:** two poles — **Big Tech (Google DeepMind, NVIDIA)** with deep model+infra integration, and **well-funded pure-plays (Physical Intelligence, Skild, Genesis)** betting a single "brain" runs any robot [11].

**Bottleneck:** Data (Layer 5), not architecture. Also inference speed — flow-matching/diffusion policies need multiple passes; RT-2 ran at ~5Hz [2].

**Opportunity:** The "one brain for all robots" licensing model is the biggest prize in the industry — and why 77.6% of physical-AI capital went to robot foundation models + general-purpose robots [11]. But it's crowded and capital-intensive. Edge-efficient VLAs (SmolVLA path) and vertical fine-tunes are more accessible openings.

---

### Layer 7 — Embodiment & Use Case (the application)

**Where robots are actually deployed today (by traction, highest first):**

- **Warehouse & logistics (the real revenue):** 33% of AMR demand [10]. Amazon Robotics runs **1M+ robots** [10]. DHL invested $700M for 1,000+ robots (Boston Dynamics Stretch, Locus) in July 2025 [10]. **Agility Digit** moves totes at GXO/Amazon — the only humanoid with consistent commercial revenue [3].
- **Manufacturing / automotive:** Figure 02 did an 11-month BMW pilot (90,000 components, 1,250 hrs) [3]; Apptronik Apollo tested with Mercedes; US manufacturing AMR adoption +41% vs. 2022 [3][10].
- **Surgical / healthcare:** medical/surgical robotics growing 23.1% CAGR; hospital AMRs (Diligent's Moxi) at 19% CAGR [10].
- **Consumer / domestic:** 1X NEO (B2C, soft/safe home robot) — earliest, hardest [3].
- **Defense:** the sleeper — $8.0B across 234 deals in 2025, +139% YoY; Saronic's $1.75B round topped 2026 [11].
- **Agriculture:** emerging, largely untapped [10].

**The strategic split:** B2B-industrial (Figure, Agility, Apptronik) vs. B2C-consumer (1X), with a long-term **convergence thesis** — each expands into the other's territory [3].

**Reality check:** Despite $6B+ invested and Figure at a $39B valuation, **revenue across humanoids is minimal — mostly LOIs and pilots, not recurring revenue** [3]. No consensus leader: Figure owns valuation, Agility owns deployment, Unitree/UBTECH own volume/cost [3].

---

## The Stack at a Glance — Where AI, Models & Infra Come From

| Layer | Primary suppliers | Open source | Closed source | Bottleneck |
|---|---|---|---|---|
| 7. Use case | Amazon, Agility, Figure, DHL, Intuitive | ROS apps | Most deployments | Reliability, ROI, revenue |
| 6. Foundation model / brain | DeepMind, NVIDIA, Physical Intelligence, Skild | OpenVLA, GR00T, SmolVLA, Cosmos3 | Gemini Robotics, Helix, π0, Skild Brain | **Data**, inference speed |
| 5. Data / flywheel | Labs' teleop corpora, HF, consortia | Open X-Embodiment, LeRobot | Proprietary teleop data | **Diverse data at scale** |
| 4. Sim / world models | NVIDIA, Genesis, DeepMind | MuJoCo, Isaac Sim, Gazebo, Cosmos3 | Genesis GENE | **Sim-to-real gap** |
| 3. OS / middleware | Open Robotics | **ROS 2, Nav2, MoveIt 2** | Vendor drivers | Real-time on high-DOF |
| 2. Actuation / sensors / body | Harmonic Drive, Nabtesco, SKF, ATI, China cluster | (designs only) | Nearly all | **Actuators, roller screws, tactile, magnets** |
| 1. Compute / silicon | **NVIDIA** (Thor), Qualcomm, AMD, Intel | CUDA ecosystem is closed | Jetson Thor | Power/thermal, NVIDIA lock-in |

**Reading the table vertically:** notice the **inversion**. The *top* of the stack (brains, sim, data tooling) is trending **open**; the *bottom* (silicon, actuators, magnets) is **closed and supply-constrained**. This is the opposite of the classic software world, and it's why "hardware is the moat, software is commoditizing at the model layer" — even as *value* accrues to whoever owns the deployed intelligence + data loop.

---

## NVIDIA's "Default" Status: Hardware or Ecosystem? (and where AMD is missing)

**Short answer:** NVIDIA's default status is **~20% hardware, ~80% ecosystem**. It is a *hardware* default only at Layer 1. At Layers 4–6 it is default **purely through software** (Isaac, Omniverse, Cosmos, CUDA-X), and even Layer 1's durable lock-in is CUDA (~4M developers, cuDNN/TensorRT libraries years ahead of ROCm), not the transistors [15]. CUDA is the connective tissue binding all layers.

| Layer | NVIDIA default? | HW or ecosystem | Basis |
|---|---|---|---|
| 1. Compute silicon | Yes | **Both** (durable = ecosystem) | Thor wins HW (2,070 TFLOPS) [5]; CUDA is the real moat [15] |
| 2. Actuators / body | No | — | Harmonic Drive/Nabtesco/China own it; **AMD ahead here** [7] |
| 3. OS / middleware | No | Open | ROS 2 neutral [4] |
| 4. Sim / world models | **Yes** | **Pure ecosystem** | Isaac Sim + Omniverse + Cosmos; no silicon needed [9][15] |
| 5. Data / synthetic | Partly | Ecosystem | Cosmos synthetic-data engine + curation [9] |
| 6. Foundation model / brain | Yes (indirect) | Ecosystem | GR00T/Cosmos + everyone trains VLAs on CUDA [15] |
| 7. Use case | No | Application | Neutral |

### AMD's 2026 entry (Advancing AI 2026) [14][16]
Ryzen AI Embedded X100 (Zen 5 + RDNA 3.5 + XDNA 2 NPU) + Kria AI SOM + Robotics Developer Platform + 30+ partner Robotics Partner Network, on **ROCm + ROS 2**. Strategy: win on **deterministic real-time control**, not peak TFLOPS. Claims (AMD-sponsored, treat as directional) vs. Jetson T5000: 125µs / 8,000 control-decisions-per-sec loop with sub-100ms VLA inference; 3.4× real-time reliability, 1.6× spare CPU, 2.3× concurrent agents. Full body-to-brain silicon map: Versal AI Edge (comms), Zynq UltraScale+ (actuation), Spartan UltraScale+ (sensor fusion). Named design win: Bosch Rexroth controller. Production Q4 2026.

### Where AMD is MISSING (all ecosystem layers)
1. **Simulation / world models (Layer 4) — biggest hole.** No Isaac Sim / Omniverse / Cosmos equivalent [14]. This is NVIDIA's stickiest, HW-independent moat.
2. **Robot foundation models (Layer 6).** No GR00T-equivalent; plays "run others' models via ROCm" (75% CUDA→ROCm code preservation) — a follower, not a default-setter [14][15].
3. **Synthetic-data / data flywheel tooling (Layer 5).** No first-party stack.
4. **Software-ecosystem maturity.** VLM/VLA/LLM support reportedly *behind Intel and Qualcomm*; ROCm operator coverage still second-class vs. CUDA [15][16].
5. **Developer mindshare.** ~4M CUDA devs + decade of curricula vs. smaller ROCm base [15].
6. **Shipping / design-ins.** Thor already in Atlas/Digit/Figure [5]; AMD ships Q4 2026 [14][16].
7. **Peak edge AI TFLOPS.** Conceded to Thor [16].

### Where AMD is NOT missing (its wedge — Layers 2–3)
Deterministic control, whole-body distributed compute, motor control, sensor fusion, IEC 61508 functional safety, x86 + unified memory, open ROCm/ROS 2 [14][16]. **Implication:** AMD attacks the control layer NVIDIA's GPU-first design underserves — but breaking NVIDIA's *default* status requires closing the **ecosystem** gap (sim, world models, data, developer mindshare), which hardware parity alone cannot do.

---

## The Port List: GitHub/HF Repos AMD Must Port (or Lag Behind)

This is a repo-by-repo audit of the open robotics stack, ranked by ROCm-readiness. **The lock-in is not the programming model** — HIP/hipify auto-translates ~75% of CUDA [14][19]. The moat is (a) hand-optimized kernels with no AMD equivalent, and (b) the **Warp → Newton → cuRobo → Isaac** physics/sim stack, whose warp-level primitives hipify *cannot* auto-translate [19].

### 🟢 Tier 0 — Already ROCm-ready (AMD's beachhead)
| Repo / Model | Location | Status |
|---|---|---|
| PyTorch | upstream | ✅ ROCm upstreamed [19] |
| JAX / OpenXLA | ROCm/rocm-jax | ✅ Mature; gated on Instinct in CI; `jax[rocm7-local]` [20] |
| flash-attention | Dao-AILab + AMD fork | ✅ Official AMD fork (CK + Triton; MI200/250/300/355, RDNA3/4) [19] |
| MuJoCo / MJX | google-deepmind/mujoco | ✅ **Official AMD ROCm 7.2 guide** (JAX/XLA path) [17][19] |
| LeRobot | huggingface/lerobot | ✅ **AMD tutorial**: Pi0 fine-tuned on MI200, deployed on Ryzen AI [17][18] |
| SmolVLA | lerobot/smolvla_base | ✅ First-class in LeRobot → ROCm [18] |

### 🟡 Tier 1 — Portable but not officially done (PyTorch/HIP path)
| Repo / Model | Lock-in | Risk if unported |
|---|---|---|
| **OpenVLA** (openvla/openvla) | PyTorch + flash-attn + RLDS | Medium — #1 open-weight generalist VLA; reachable via ROCm PyTorch, unvalidated [18] |
| **Cosmos 3** (NVIDIA/Cosmos; HF `nvidia/Cosmos3-*`) | PyTorch/Transformers/Diffusers/vLLM; **no JAX, no official ROCm** | **High** — dominant world/synthetic-data model (2M+ downloads); PyTorch+vLLM reachable but undone [20] |
| **Genesis** (Genesis-Embodied-AI) | Taichi (multi-backend) but benchmarks CUDA-only | Medium — needs AMD validation |
| **openpi** (Physical-Intelligence/openpi) | JAX/XLA but **hard-requires NVIDIA GPU**, Ubuntu 22.04 | Medium — JAX-ROCm exists; blocked by hard-coded assumptions [18] |
| **PyTorch3D** (facebookresearch) | CUDA-only wheels, partial CPU fallback | Low-med — build from source [19] |
| **X-VLA** | LeRobot ecosystem | Low — inherits LeRobot portability [18] |

### 🔴 Tier 2 — Hard CUDA lock-in (THIS is where AMD lags)
| Repo / Model | Why locked | Consequence |
|---|---|---|
| **Isaac Sim / Isaac Lab** | PhysX + RTX; **no AMD support, no CPU physics fallback** | **Critical** — default large-scale RL sim; AMD has zero answer [19] |
| **NVIDIA Warp** (NVIDIA/warp) | warp-level primitives, PTX, JIT→CUDA | **Critical** — substrate under Newton & cuRobo; hipify can't translate [19] |
| **Newton physics** (newton-physics/newton) | Built on Warp (NVIDIA+DeepMind+Disney, Linux Foundation) | **Critical** — emerging cross-industry physics standard; inherits Warp lock [19] |
| **MuJoCo-Warp** | Warp backend | High — the *fast* MuJoCo path bypasses ROCm-friendly MJX [19] |
| **cuRobo** (NVlabs/curobo) | Custom CUDA kernels + Warp + nvblox + CUDA Graphs | High — de facto motion planner; "no clear ROCm path without kernel reimplementation" [19] |
| **Isaac-GR00T** (NVIDIA/Isaac-GR00T) | Tied to Isaac + flash-attn + Jetson Thor | Medium — NVIDIA's own model; won't be ported by NVIDIA [18] |
| **TensorRT-LLM** | NVIDIA-only inference | Low — vLLM (ROCm) substitutes [20] |

### Ranked porting priority for AMD
1. **Physics/sim substrate — the real lag risk.** A **ROCm backend for NVIDIA Warp** is the single highest-leverage port: it's open-source (Linux Foundation) and unlocks **Newton + MuJoCo-Warp** simultaneously. Without it, any team needing large-scale RL in Isaac Lab or motion planning via cuRobo has *no AMD path at all* [19].
2. **Cosmos 3 on ROCm + vLLM** — the world-model/synthetic-data default; PyTorch-based so reachable, just undone [20].
3. **Official ROCm validation of OpenVLA + openpi** — closes the model-layer gap fully [18].

**Net:** AMD's *accessible* robotics story (LeRobot/SmolVLA/MJX) already runs on ROCm. AMD lags the moment a workflow touches **Isaac Lab, Warp/Newton, or cuRobo** — the CUDA-kernel-heavy simulation and motion-planning layer.

---

## Cross-Cutting Ecosystem Gaps (the core of your question)

### Gap 1 — The Data Flywheel (the master gap)
**What's missing:** diverse, action-labeled sensorimotor data at anything near LLM scale. **Evidence:** 1M open episodes vs. trillions of tokens; teleop stuck at 5–50 episodes/hr [6]. **Who's affected:** every foundation-model player. **Why still open:** physical data can't be scraped; it must be *performed*. **Signal:** LeRobot's 16K datasets, Open X-Embodiment, and the entire world-model industry (Cosmos/Genesis) are all attacks on this gap [6][9].

### Gap 2 — Non-NVIDIA Edge Inference Silicon
**What's missing:** a credible robotics inference chip + open toolchain outside NVIDIA. **Evidence:** Thor is the announced brain for nearly every major humanoid [5]. **Why still open:** NVIDIA's moat is the *software stack*, not the transistors — hard to displace. **Opportunity signal:** AMD/Xilinx adaptive SoCs, Qualcomm's automotive edge presence [5]. **This is a direct opening for AMD.**

### Gap 3 — The Physical Component Base (actuators, screws, tactile, magnets)
**What's missing:** Western/allied volume manufacturing of robotics-grade actuators, roller screws, six-axis/tactile sensors; rare-earth-independent motors. **Evidence:** China 63–70% of supply, 30–40% cheaper; Japan monopoly on harmonic drives; roller screws at $1,350–2,700 each [7]. **Why still open:** ultra-precision manufacturing (3-micron tolerances) + qualification, not just capacity [7]. **Signal:** "America lost robotics at the actuator" reshoring discourse; Green Harmonic's 500K-unit plant [7].

### Gap 4 — Tactile Sensing / Dexterous Hands
**What's missing:** mature, mass-manufacturable tactile skin + dexterous hands. **Evidence:** explicitly called "the largest open platform opportunity in humanoid robotics today"; dexterous hands cited as a top technical hurdle [7][3]. **Opportunity:** a horizontal tactile-sensor supplier serving all OEMs.

### Gap 5 — Sim-to-Real for Contact-Rich Tasks
**What's missing:** simulation that reliably transfers on friction/contact. **Evidence:** sim fails on contact-rich tasks; Genesis's 0.90 correlation is notable *because* the baseline is poor [6][9]. **Opportunity:** domain-specific high-fidelity sim; eval-as-a-service.

### Gap 6 — Safety, Standards & Liability for Humanoids
**What's missing:** applicable safety standards + insurance for general-purpose mobile humanoids. **Evidence:** ISO 10218:2025 (absorbing TS 15066) covers industrial arms but **not legged mobility or fall risk**; "cutting power to a humanoid makes it collapse"; ISO 25785-1 still a working draft; **"no applicable safety standards exist for general-purpose mobile humanoids"** and insurance markets are nascent [13]. **Why it matters:** this gates deployment regardless of technical readiness — "unquantified legal exposure" slows adoption [13]. **Opportunity:** compliance/"trust architecture" tooling (telemetry, XAI, CAPA logs); functional-safety-certified control systems for legged robots.

### Gap 7 — Systems Integration / Deployment Tax
**What's missing:** turnkey integration. **Evidence:** 37% of logistics providers cite integration cost/facility retrofit as the barrier [10]. **Signal:** RaaS (Robot-as-a-Service) business models emerging to absorb this [10].

---

## Trends Enabling New Solutions (why now)

1. **On-device compute crossed the threshold** — Thor lets full VLA models run on the robot in real time [5].
2. **VLAs went open and small** — OpenVLA + SmolVLA put usable brains in every lab; fine-tune with 50–100 demos [2][12].
3. **World models attack the data gap** — Cosmos (2M+ downloads) + Genesis turn data scarcity into a *compute* problem [9].
4. **Cross-embodiment learning works** — one model, many bodies, positive transfer [2].
5. **Capital flood** — $18.8B H1 2026, strategic investors securing supply/data loops [11].
6. **Cost collapse** — Unitree R1 at $5,900 signals hardware commoditization [3].

---

## Key Convergences (where separate worlds are merging)

- **Autonomous vehicles ⇄ robotics:** shared world models (Cosmos serves both), shared compute (Thor descends from automotive), shared sim [5][9].
- **LLM/VLM ⇄ robotics:** VLAs are VLMs fine-tuned on action; Gemini Robotics is Gemini + action [2][12].
- **EV manufacturing ⇄ humanoids:** BYD, Geely, XPeng, Tesla pivot EV supply chains into robots; magnets/motors/batteries overlap [3][7].
- **B2B ⇄ B2C robots:** long-term dual-use expansion in both directions [3].
- **Safety ⇄ AI ⇄ cybersecurity:** compliance shifting to continuous "trust architectures" merging functional safety, XAI, and cyber [13].
- **Compute + simulation + model + data, vertically integrated by NVIDIA** — the deepest convergence and the deepest lock-in [5][9].

---

## Risks & Constraints

- **Funding washout:** "a record fundraising year guarantees a record washout later" as over-funded humanoid plays hit manufacturing/margin reality [11]. Revenue is mostly LOIs, not recurring [3].
- **China supply-chain dependency + export controls** on magnets/components — strategic and existential for Western OEMs [7].
- **NVIDIA single-vendor concentration** across compute + sim + world models [5][9].
- **Safety/liability vacuum** for humanoids — no standards, nascent insurance, unquantified legal exposure [13].
- **Persistent hardware limits:** battery life, dexterous hands, high-precision screw supply, actuator backdrive failure on falls [3][7].
- **Sim-to-real gap** still unsolved for contact-rich manipulation [6][9].
- **Inference latency** for diffusion/flow-matching policies on the edge [2].

---

## Where the Opportunities Concentrate (synthesis)

If you are looking for where to build or invest, the gaps rank roughly:
1. **Data flywheel infrastructure** (teleop rigs, human-video→action, data marketplaces) — the master gap [6].
2. **Physical component reshoring** (actuators, roller screws, tactile sensors, magnet-light motors) — strategic + underserved outside China/Japan [7].
3. **Non-NVIDIA edge inference silicon** with an open toolchain — the clearest single-vendor gap; a direct AMD opening [5].
4. **Tactile/dexterous-hand horizontal supplier** — explicitly named the biggest open platform [7].
5. **Safety/compliance "trust architecture" tooling** — gates all deployment [13].
6. **Vertical sim + eval-as-a-service** — sim-to-real for specific domains [9].
7. **RaaS + integration** to absorb the deployment tax [10].

---

## Sources

[1] Grand View Research / MarketsandMarkets / Fortune Business Insights / Future Market Insights / Emergen Research / Mordor Intelligence / DataM Intelligence — humanoid & embodied AI market sizing — https://www.grandviewresearch.com/industry-analysis/humanoid-robot-market-report ; https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html ; https://www.fortunebusinessinsights.com/humanoid-robots-market-110188 ; https://www.mordorintelligence.com/industry-reports/robotics-market
[2] VLA foundation models (RT-2, π0, OpenVLA, GR00T, SmolVLA, Helix, Skild, Open X-Embodiment) — https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/ ; https://www.pi.website/download/pi0.pdf ; https://github.com/keon/awesome-physical-ai ; https://robotics-transformer2.github.io/
[3] Humanoid competitive landscape (Figure, Tesla, Agility, Apptronik, 1X, Unitree) — https://valueaddvc.com/humanoid-robot-race ; https://sacra.com/research/figure-vs-apptronik-vs-agility-robotics/ ; https://standardbots.com/blog/humanoid-robotics-companies ; https://www.technerdo.com/blog/humanoid-robots-market-2026
[4] Robotics software stack & simulators (ROS 2, MuJoCo, Isaac Sim, Gazebo, MoveIt 2) — https://www.blackcoffeerobotics.com/blog/which-robot-simulation-software-to-use ; https://www.godrift.ai/blogs/best-robot-simulators-ros2 ; https://developer.nvidia.com/blog/a-beginners-guide-to-simulating-and-testing-robots-with-ros-2-and-nvidia-isaac-sim/ ; https://www.trossenrobotics.com/post/robot-arm-simulation-mujoco-isaac-sim-gazebo
[5] Robotics compute silicon (Jetson Thor, Qualcomm, edge AI) — https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://blogs.nvidia.com/blog/jetson-thor-robotics-edge-ai-agent/ ; https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/ ; https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics
[6] Robot training data & teleoperation (Open X-Embodiment, LeRobot, data pyramid) — https://www.shaip.com/blog/robot-training-data-strategy/ ; https://dexset.ai/blogs/teleoperation-data-collection-robot-learning-complete-2026/ ; https://arxiv.org/html/2602.22818v1 ; https://www.tanayj.com/p/the-robot-data-pyramid ; https://axisrobotics.ai/resources/learn/lerobot-open-robotics-data-stack
[7] Humanoid hardware supply chain (actuators, harmonic drives, roller screws, tactile, rare earths) — https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins ; https://www.gerra.com/insights/humanoid-robot-supply-chain ; https://humanoid.guide/the-humanoid-robot-supply-chain/ ; https://interestingengineering.com/ai-robotics/china-humanoid-robots-actuators ; https://www.manilatimes.net/2026/07/16/tmt-newswire/plentisoft/the-us589-billion-humanoid-robot-opportunity-starts-with-actuators-sensors-and-batteries-says-datam-intelligence/2386110
[8] Actuator/component China dependency (Medium, IDTechEx) — https://medium.com/@bailey55015/america-lost-robotics-at-the-actuator-heres-how-we-take-it-back-912cdba94266 ; https://www.idtechex.com/en/research-report/humanoid-robots/1149
[9] World models & sim-to-real (NVIDIA Cosmos, Genesis World) — https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/ ; https://www.nvidia.com/en-us/ai/cosmos/ ; https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai ; https://www.genesis.ai/blog/the-role-of-simulation-in-scalable-robotics-genesis-world-10-and-the-path-forward ; https://www.humanoidsdaily.com/news/genesis-ai-launches-genesis-world-1-0-turning-the-sim-to-real-gap-into-a-compute-problem
[10] AMR & use-case markets (warehouse, manufacturing, surgical, agriculture) — https://www.marketsandmarkets.com/Market-Reports/autonomous-mobile-robots-market-107280537.html ; https://www.gminsights.com/industry-analysis/autonomous-mobile-robots-market ; https://www.grandviewresearch.com/industry-analysis/autonomous-mobile-robots-market ; https://www.abiresearch.com/blog/global-robotics-market-outlook
[11] Robotics startup funding 2025–2026 (Crunchbase, PitchBook, Value Add) — https://news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/ ; https://valueaddvc.com/pulse/robotics-startups-record-venture-funding-2026-embodied-ai ; https://newmarketpitch.com/blogs/news/physical-ai-funding-analysis ; https://futureinvestments.news/p/when-intelligence-gets-a-body-the-investment-case-for-physical-ai
[12] Google DeepMind Gemini Robotics (VLA, ER, on-device, GR2) — https://deepmind.google/models/gemini-robotics/ ; https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/ ; https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ ; https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/ ; https://www.infoq.com/news/2025/07/google-gemini-robotics/
[13] Robotics safety, standards & liability (ISO 10218:2025, ISO 25785-1, humanoid gap) — https://www.osha.gov/robotics/standards ; https://www.iso.org/obp/ui/en/#!iso:std:73933:en ; https://blog.saphira.ai/functional-safety-for-humanoid-robots ; https://www.kitecompliance.ai/vertical-compliance/humanoid-robot-compliance ; https://www.automate.org/robotics/blogs/updated-iso-10218-faq
[14] AMD physical AI entry (Ryzen AI Embedded X100, Kria AI SOM, Robotics Partner Network, X100 vs Jetson benchmarks) — https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/ ; https://newsroom.amd.com/news/aai-2026-robotics-partner-network/ ; https://www.techpowerup.com/351008/amd-advancing-ai-2026-ryzen-ai-embedded-x100-kria-ai-robotics-platform-and-robotics-partner-network ; https://www.cnx-software.com/2026/07/24/amd-launches-ryzen-ai-embedded-x100-processors-kria-ai-som-and-physical-ai-robotics-developer-platform/ ; https://www.therobotreport.com/amd-unveils-kria-module-real-time-control-unified-memory-robots/
[15] NVIDIA CUDA moat & ROCm alternative (robotics ecosystem lock-in, Isaac/Omniverse stickiness) — https://builtin.com/articles/nvidias-cuda-future-ai-infrastructure ; https://pitchgrade.com/research/nvidia-competitive-moat ; https://www.thundercompute.com/blog/rocm-vs-cuda-gpu-computing ; https://aimultiple.com/cuda-vs-rocm ; https://www.sdxcentral.com/analysis/beyond-cuda-inside-the-push-to-loosen-nvidias-grip-on-ai-computing/
[16] AMD adaptive SoC/FPGA robotics (Versal/Zynq/Spartan motor control, determinism, x86 vs Jetson, software gap) — https://www.amd.com/en/solutions/industrial/robotics.html ; https://www.eetimes.com/amd-challenges-gpu-centric-architectures-as-it-takes-aim-at-nvidia-in-robotics/ ; https://www.techtimes.com/articles/318134/20260610/amd-carries-x86-robotics-cars-ryzen-ai-embedded-challenging-arm-based-rivals.htm ; https://www.therobotreport.com/how-does-nvidias-jetson-thor-compare-with-other-robot-brains/ ; https://www.allaboutcircuits.com/news/amd-unveils-processors-boards-and-dev-platformall-tuned-for-physical-ai/
[17] AMD ROCm robotics blogs (LeRobot Pi0 fine-tune on Instinct + Ryzen AI deploy; MuJoCo+JAX on ROCm) — https://rocm.blogs.amd.com/artificial-intelligence/rocm-lerobot/README.html ; https://rocm.blogs.amd.com/artificial-intelligence/rocm-jax-mujoco/README.html
[18] VLA repos CUDA/ROCm status (openpi, Isaac-GR00T, OpenVLA, LeRobot, SmolVLA, X-VLA) — https://github.com/Physical-Intelligence/openpi ; https://github.com/openvla/openvla ; https://huggingface.co/blog/smolvla ; https://www.roboticscenter.ai/tools/vla-models-comparison ; https://huggingface.co/docs/lerobot/xvla
[19] Robot-learning CUDA dependencies & ROCm portability (cuRobo, Warp, Newton, MuJoCo-Warp, flash-attn, PyTorch3D, Isaac Lab) — https://github.com/nvlabs/curobo ; https://github.com/newton-physics/newton ; https://developer.nvidia.com/warp-python ; https://github.com/dao-ailab/flash-attention ; https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md ; https://rocm.blogs.amd.com/artificial-intelligence/rocm-jax-mujoco/README.html
[20] NVIDIA Cosmos weights on HF & JAX-on-ROCm maturity (no official Cosmos ROCm/JAX path; PyTorch/vLLM route) — https://huggingface.co/nvidia/Cosmos3-Super ; https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai ; https://github.com/NVIDIA/Cosmos ; https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/jax-compatibility.html ; https://rocm.blogs.amd.com/software-tools-optimization/openxla-jax-rocm/README.html