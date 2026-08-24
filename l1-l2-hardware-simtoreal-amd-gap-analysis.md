# L1 & L2 Robotics Layers: Tech Ecosystem Gap Analysis for AMD
*Research date: 2026-08-13 | Sources: 30+ pages across hardware, SDK, and sim-to-real domains*

---

## Executive Summary

Two foundational layers govern who wins the robotics AI compute race: **L1 — Infrastructure (Hardware & SDKs)** and **L2 — Platform (Sim-to-Real Validation)**. NVIDIA holds an engineered lock-in across both — not through silicon superiority alone, but through a vertically integrated software stack (TensorRT → GXF → Isaac ROS/NITROS → cuRobo → Isaac Sim → Cosmos) where each layer consumes the one beneath it and forecloses cross-vendor substitution.

AMD launched its first explicit robotics hardware play in July 2026 (Ryzen AI Embedded X100 + Kria AI Robotics Developer Platform), but enters a market where the SDK layer is nearly empty on the AMD/ROCm side, GPU-accelerated motion planning has no AMD path, and the highest-throughput sim-to-real training workflows (MJX-Warp, Warp/Newton, Isaac Sim) are CUDA-only by design. The gaps are large, documented, and — critically — technically tractable starting from existing open-source foundations.

**The single highest-leverage gap for AMD:** Warp is open-source (Linux Foundation). Porting it to ROCm unlocks the entire cascade: Newton physics engine, MJX-Warp (3.35M steps/sec Humanoid scenes), MuJoCo Playground training recipes, and Isaac Lab workflows — all on AMD silicon. No current community effort targets this gap.

---

## Market Overview

| Segment | 2025 Size | 2031/2033/2034 Projection | CAGR |
|---|---|---|---|
| Edge AI Hardware | $25.08B | $68.73B (2031) | 17.46% |
| Robotics Simulation Software | $1.5B (2024) | $4.2B (2033) | 15.3% |
| Sim-to-Real Transfer Market | $3.8B | $34.6B (2034) | 28.5% |
| Synthetic Data for Physical AI | $2.03B | $63.95B (2035) | 41.25% |
| Broader Robotic Simulator Market | — | $146.9B (2033) | 21.8% |

Robots/drones are the **fastest-growing edge AI hardware segment** (18.32% CAGR, ahead of overall market), driven by humanoid deployment acceleration and logistics automation. Asia installs 70% of all new robots globally, compounding hardware demand.

Top-5 edge AI hardware vendors (NVIDIA, Qualcomm, Intel, Apple, Samsung) hold 55–60% market share. AMD is not in this top-5 — it is attacking from the workstation/data center side with Ryzen AI Embedded X100 and MI300X, not from an entrenched embedded position. Fragmented toolchains are identified by Mordor Intelligence as the primary market restraint (-1.2% CAGR drag), which is both AMD's current liability and its strategic opening.

---

## Current Ecosystem Map

### L1 — Infrastructure: Hardware & SDKs

#### Hardware — Compute Platforms

**NVIDIA**
- **Jetson Orin NX**: 100 TFLOPS FP16, 25W — volume edge robotics platform
- **Jetson AGX Orin**: 374 TFLOPS — flagship embedded AI
- **Jetson Thor T5000**: 1,035+ TOPS FP8, 40–130W configurable, Blackwell 4nm — humanoid/enterprise next-gen
- **NVIDIA DRIVE Thor**: AV-grade, ISO 26262 ASIL-D certified

**AMD**
- **Ryzen AI MAX+ 395** (consumer): 60 TFLOPS FP16 GPU + 50 TOPS NPU, x86 Zen 5 — robotics workstation baseline
- **Ryzen AI Embedded X100/X199** (announced July 2026, Q4 2026 GA): 60 TFLOPS GPU + 50 TOPS NPU, 55W TDP, 128GB LPDDR5x unified, 4nm Zen 5 × 16 cores; COM-HPC form factor (open standard); FPGA co-processor (Spartan UltraScale+) for EtherCAT/TSN/CAN-FD deterministic control; Zen hypervisor + FreeRTOS VM targeting <7μs interrupt latency
- **AMD MI300X**: 192GB HBM3, 5.3 TB/s bandwidth — data center training, not edge
- **AMD Kria KV260/KR260**: Zynq UltraScale+ FPGA+ARM, existing embedded platform

**Qualcomm**
- **Snapdragon QCS8275**: Hexagon NPU, 16+ TOPS — industrial robotics
- **Snapdragon Ride Flex**: ADAS/robotics SoC
- **AI Hub**: cloud-based model optimization + deployment tooling; QNN SDK for on-device inference

**Intel**
- **Movidius VPU**: <5W, ~4 TOPS INT8 — ultra-low power vision
- **Core Ultra / Panther Lake** (upcoming): integrated NPU, ~30–40 TOPS
- **Intel Arc GPU**: discrete GPU with OpenVINO acceleration

**Specialist Edge AI**
- **Hailo Hailo-15**: 20 TOPS, sub-5W; commercial contracts with BMW, Sony — highest deployment momentum in automotive-adjacent robotics
- **SiMa.ai MLSoC**: software-defined architecture, multiple DRAM configurations; positioned for industrial/robotics
- **Syntiant NDP120**: <1mW, always-on keyword/gesture detection — MCU tier
- **Ambarella CV7**: computer vision SoC for mobile robotics cameras
- **Google Coral TPU**: 4 TOPS, USB/mPCIe — Edge TPU for TF Lite Micro workloads
- **Apple A18 Pro**: 35 TOPS NPU; **M-series**: 38 TOPS — consumer robotics, on-device VLA inference
- **Rockchip RK3588**: 6 TOPS NPU, Linux-native, popular in maker robotics
- **ARM Ethos-U55/U85**: MCU-class NPU, sub-10W, Cortex-M/R ecosystem; TF Lite Micro runtime
- **RISC-V** (SiFive, Andes): open-ISA emerging in low-power robotics controllers

#### SDKs, Runtimes, and Middleware

**NVIDIA (CUDA-native stack)**
- **TensorRT**: primary inference optimizer; INT8/FP8/FP16 quantization; NVIDIA-only
- **GXF (Graph eXecution Framework)**: messaging/scheduling middleware for robot compute graphs; NVIDIA-only
- **Isaac ROS 4.0**: hardware-accelerated ROS 2 node library; NITROS (NVIDIA Isaac Transport for ROS) eliminates CPU-copy overhead in GPU pipelines; NVIDIA-only
- **cuRobo V2** (Apache 2.0, April 2026): CUDA-accelerated motion generation — batched L-BFGS trajectory optimization, parallel IK (37,000 queries/sec), continuous collision checking via GPU-voxel ESDF; ~30ms end-to-end on RTX 4090; dynamics-aware trajectories, whole-body humanoid motion; integrates as MoveIt 2 plugin via Isaac ROS cuMotion; CUDA kernel-heavy, no ROCm abstraction
- **Triton Inference Server**: model serving framework; partial ROCm support (limited backends)
- **CUDA / cuDNN / NCCL**: universal GPU compute substrate
- **NVIDIA Warp**: open-source (Linux Foundation), Python-GPU framework for physics simulation; used as kernel backend for Newton, MJX-Warp, and cuRobo; **CUDA-only**

**AMD (ROCm stack)**
- **ROCm / HIP**: open-source GPU compute platform; HIP migration tool claims ~75% CUDA code preservation, but CUDA-kernel-heavy libraries (cuRobo, Warp) fall in the hard 25%
- **MIGraphX**: AMD's graph inference engine; serves as ONNX Runtime MIGraphX Execution Provider (ORT ROCm EP deprecated in v1.23, 2026 — fully replaced by MIGraphX EP)
- **Composable Kernel (CK)**: hand-tuned GPU kernels for AMD CDNA/RDNA; underpins Flash Attention AMD fork
- **ROCm-native NITROS equivalent**: internal AMD project, not yet public — targeting Isaac ROS/NITROS feature parity on AMD edge hardware
- **AMD Kria AI Robotics Developer Platform** (July 2026): bundles X100 + FPGA + ODM partner boards (Arbor, Congatec, iBase, Sapphire) + AMD Robotics Partner Network (ODM, sensing, safety, sim partners)

**Intel**
- **OpenVINO**: cross-framework inference optimizer (ONNX, TensorFlow, PyTorch); supports CPU, GPU, VPU, NPU targets; strong on Movidius and Core Ultra
- **Neural Compressor**: INT8/INT4 quantization toolkit; integrates into OpenVINO pipeline

**Qualcomm**
- **QNN (Qualcomm Neural Network)**: on-device inference runtime targeting Hexagon NPU + Adreno GPU
- **Snapdragon AI Hub**: cloud model optimization, profiling, and deployment workflow

**Cross-Platform / Open-Source Runtimes**
- **ONNX Runtime**: cross-platform inference; ROCm EP deprecated v1.23 → MIGraphX EP now the AMD path; CPU/CUDA/CoreML/DirectML/TensorRT EPs also available
- **ExecuTorch**: PyTorch's embedded/mobile inference stack; ARM/XNNPACK backends; growing robotics use
- **llama.cpp / GGUF**: edge LLM inference with HIP backend for AMD GPUs; community-validated on RX 7900 XTX (97.6 tok/s vs RTX 4090 158.4 tok/s — 38% gap)
- **TF Lite Micro**: MCU-tier inference; Ethos-U NPU delegate; sub-mW operation
- **LeRobot (Hugging Face)**: PyTorch-native robot learning library; ACT, Diffusion Policy, Pi0/Pi0Fast, GR00T N1.7; hardware-agnostic (no CUDA-specific kernels); accepted ICLR 2026; runs on AMD ROCm via standard PyTorch
- **MoveIt 2**: CPU-based robot motion planning (OMPL/RRTConnect); ROS 2 native; no GPU acceleration; only AMD-compatible motion planning option today

**Motion Planning / Trajectory**
- **cuRobo V2** (see NVIDIA above): GPU-accelerated, CUDA-only
- **MoveIt 2**: CPU, open, cross-platform — 100× slower than cuRobo in cluttered scenes; 50% success rate vs cuRobo's 100% in benchmark cage scenario

---

### L2 — Platform: Sim-to-Real Validation

#### Primary Simulation Environments

**NVIDIA Isaac Sim 5.0**
- Open-source (Apache 2.0, 2025); free for non-production use with NVIDIA Developer Program membership
- **Requires NVIDIA RTX GPU** — no AMD path; Omniverse Kit redistribution requires NVIDIA Enterprise license for production
- PhysX TGS solver (stable at scale for rigid-body + articulation); GPU-parallel rendering via RTX ray tracing
- Synthetic data generation at scale; integration with Cosmos world models
- 112 active robotics job postings referencing Isaac Sim (50% more than closest competitor)
- 110+ partners at GTC 2026; FANUC integration; MIG partitioning for concurrent workloads

**NVIDIA Cosmos**
- **Cosmos Predict 2.5** and **Transfer 2.5** (released Jan/Feb 2026); **Cosmos 3** (2026)
- Physics-aware world model for synthetic data generation and domain transfer
- Physical AI Data Factory Blueprint (March 2026): pipeline for generating training-ready sim datasets
- Requires Isaac Sim / NVIDIA stack; no standalone AMD path

**NVIDIA Omniverse / Isaac Lab**
- Omniverse: USD-native 3D simulation and collaboration platform; RTX-required for real-time rendering
- Isaac Lab: RL training environment built on Isaac Sim; NVIDIA-only; replaces Isaac Gym

**NVIDIA OSMO**
- Cloud-native orchestration for GPU simulation fleets; manages thousands of parallel sim instances
- Integrates Cosmos + Isaac Lab + GR00T into a managed pipeline

**Google DeepMind MuJoCo**
- Apache 2.0; CPU physics engine; cross-platform (Linux, macOS, Windows, WASM)
- Analytic soft-contact solver: stable at large dt, smooth/differentiable; gold standard for contact dynamics accuracy
- **MuJoCo Menagerie**: curated MJCF robot models (Franka, UR5, Spot, Unitree H1, etc.) — enables zero-shot sim-to-real via matched dynamics
- RSS 2025 Outstanding Demo Paper: zero-shot transfer across quadrupeds, humanoids, dexterous hands, robot arms
- 50–100 demonstrations sufficient to adapt Gemini Robotics SDK models when trained in MuJoCo environments

**Google DeepMind MJX-JAX**
- JAX/XLA implementation of MuJoCo physics; runs on **NVIDIA and AMD GPUs, Apple Silicon, Google TPUs**
- Supports auto-diff, domain randomization via jax.vmap, RL training pipelines (Brax, MuJoCo Playground `--impl jax`)
- AMD ROCm compatible today via `jax[rocm]` — the key existing AMD sim-to-real entry point
- **Performance bottleneck**: single-scene 10× slower than CPU MuJoCo; large mesh/many-contact scenes degrade faster than CPU
- **No AMD GPU appears in published MJX benchmark tables** — AMD is invisible to practitioners

**Google DeepMind MJX-Warp** (highest-throughput path)
- Warp-based GPU backend for MJX; reaches **3.35M steps/sec on Humanoid scenes** (vs ~300K for MJX-JAX)
- **CUDA-only** — AMD users cannot access this path
- Used in MuJoCo Playground training recipes (`--impl warp`)
- MuJoCo Playground install guide hardcodes `jax[cuda12]`; AMD users must manually substitute `jax[rocm]`

**NVIDIA Warp** (shared dependency)
- Open-source (Linux Foundation), Python GPU framework for differentiable physics
- Backend for Newton physics engine, MJX-Warp, and parts of cuRobo
- **CUDA-only** — no ROCm port, no open PR, no community signals for AMD effort

**Newton Physics Engine** (emerging)
- Co-developed by Google DeepMind, Disney Research, and NVIDIA; Linux Foundation
- Built on NVIDIA Warp + OpenUSD
- Announced open-source; **CUDA-only** in current form (Warp dependency)

**Google Brax**
- JAX-based rigid-body physics for RL; hardware-agnostic via JAX/XLA
- AMD ROCm compatible; lower fidelity than MuJoCo (rigid-body only, simplified contact)

**Applied Intuition**
- Enterprise AV/robotics simulation stack; scenario generation, sensor simulation, closed-loop testing
- SaaS/enterprise licensing; hardware-agnostic at API layer but GPU-accelerated rendering paths favor NVIDIA

**Parallel Domain**
- Synthetic data generation for perception training (cameras, LiDAR, radar)
- Cloud-based SaaS; GPU-accelerated rendering on provider hardware

**Siemens Tecnomatix**
- Enterprise industrial digital twin for manufacturing simulation (Process Simulate, Plant Simulation)
- Process-level simulation (assembly, robotics cells, factory flow); not RL training
- Proprietary; integrates with Siemens Xcelerator platform

**Dassault Systèmes 3DEXPERIENCE**
- PLM-embedded physics simulation (SIMULIA FEA, CFD); digital twin orchestration
- Structural/thermal/fluid emphasis; limited RL training use case
- Enterprise licensing; NVIDIA GPU acceleration for rendering

**PTC Vuforia / Creo Simulation Live**
- AR-based robot programming and simulation; industrial digital twin
- Visualization layer; not a physics-first RL training platform

**Gazebo Ionic** (ROS 2 ecosystem)
- Apache 2.0; maintained by Intrinsic (Alphabet); long-term support through Gazebo Kura (August 2026)
- Best-in-class ROS 2 integration via ros_gz bridge (bidirectional, low-latency)
- Physics backends: DART 6.16 (best accuracy), Bullet, ODE
- **CPU-bound** — no GPU physics acceleration; RL at scale is not practical
- Simulation fidelity gap vs MuJoCo (contact dynamics) and Isaac Sim (photorealism) is documented

**CoppeliaSim** (V-REP successor)
- Supports **5 physics backends**: MuJoCo, Bullet Physics, ODE, Newton, Vortex Dynamics
- Cross-validation across backends; Python/Lua scripting; hardware-agnostic
- CPU-primary; no GPU-parallel RL training path

**PyBullet** (Bullet Python binding)
- Python-friendly RL research; tight PyTorch/TensorFlow integration; many foundational RL papers
- Hardware-agnostic; CPU-primary; limited sensor simulation; no production deployment tooling

**Webots**
- Pre-built industrial robot model library (ABB, KUKA, UR, Fanuc); pick-and-place prototyping
- Apache 2.0; cross-platform; minimal AI training integration

**Unity / Unreal Engine**
- Game engine sim for perception/photorealism training
- **Unity**: ML-Agents toolkit; C# physics (PhysX under the hood); GPU-accelerated rendering (vendor-agnostic via DirectX/Vulkan)
- **Unreal Engine**: photorealistic environments; NVIDIA RTX Lumen/Nanite optimized but Vulkan path available (AMD compatible for rendering)
- Both used primarily for **visual fidelity** (synthetic data for perception), not physics-accurate RL

---

## Ecosystem Gaps (AMD Perspective)

### Gap 1: No AMD Path into GPU-Parallel RL Training (Warp Lock-In)

**What's missing:** The highest-throughput sim-to-real training workflow — MJX-Warp at 3.35M steps/sec — runs on CUDA. AMD users are blocked from this performance tier. The root cause is NVIDIA Warp, an open-source (Linux Foundation) Python-GPU framework that currently has no ROCm backend. Warp is the substrate for Newton, MJX-Warp, and parts of cuRobo.

**Evidence:** MJX-Warp documentation explicitly requires NVIDIA GPU [MuJoCo docs]. No ROCm port exists, no open GitHub PR or issue signals demand, no community effort is underway [Warp follow-up research]. The MuJoCo Playground install guide hardcodes `jax[cuda12]`, forcing AMD users to manually substitute `jax[rocm]` with no official support [MuJoCo Playground repo].

**Who's affected:** Research labs without NVIDIA GPU fleets; robotics teams targeting AMD-based edge hardware who want sim-to-real consistency; academic groups on AMD workstations.

**Why it's still open:** Warp uses custom CUDA kernels throughout; ROCm porting is nontrivial. NVIDIA has no incentive to open the ROCm path itself. No third party has yet taken on the port — the gap appears unrecognized publicly.

**Opportunity signal:** Warp is Linux Foundation open-source. AMD contributing a ROCm/HIP backend would be a single engineering investment with cascading unlock: Newton portability, MJX-Warp on AMD GPUs, MuJoCo Playground native AMD support, Isaac Lab workflows. The MJX-JAX path (already AMD-compatible) proves the feasibility — only the Warp layer remains blocked.

---

### Gap 2: GPU-Accelerated Motion Planning Has No AMD Path (cuRobo)

**What's missing:** cuRobo V2 (Apache 2.0, April 2026) is the state-of-the-art GPU motion planner — 37,000 parallel IK queries/sec, ~30ms end-to-end motion generation, 100% success rate in cluttered scenes. It is built entirely on CUDA-specific kernels and NVIDIA Warp with no HIP/ROCm abstraction. AMD's only motion planning option is MoveIt 2 (CPU), which fails 50% of the time in equivalent benchmark scenarios and takes 10× longer.

**Evidence:** Benchmark data from Black Coffee Robotics shows cuMotion (cuRobo-backed) solving a cage scene in 0.301s at 100% success rate vs. RRTConnect's 10s budget at 50% success rate. AMD's own robotics benchmark report explicitly acknowledges "no equivalent to Isaac Sim or Isaac Lab" and that "ROCm ecosystem is not at feature parity with CUDA for robotics-specific tooling."

**Who's affected:** Manipulator arm teams (logistics, assembly, surgical robotics) where trajectory planning speed determines system throughput; humanoid developers needing whole-body motion generation.

**Why it's still open:** cuRobo is CUDA-kernel-heavy throughout; HIP migration tool's 75% coverage stat does not apply to libraries built on custom kernels. No open-source GPU motion planning library with ROCm support exists.

**Opportunity signal:** cuRobo V2 is Apache 2.0. An AMD-funded ROCm port or a new ROCm-native GPU motion planning library (built on Composable Kernel) would be directly differentiated. Alternatively, porting Warp (Gap 1) enables cuRobo portability as a second-order effect.

---

### Gap 3: No AMD Equivalent to Isaac Sim for GPU-Parallel Sim-to-Real

**What's missing:** Isaac Sim 5.0 is the only GPU-accelerated photorealistic robotics simulator with integrated synthetic data generation (Cosmos), parallel RL training (Isaac Lab), and ROS 2 integration. It requires NVIDIA RTX hardware — explicitly: "Teams with AMD hardware or limited GPU resources will find the platform's full capabilities inaccessible." No AMD-GPU-accelerated simulator exists to fill this role.

**Evidence:** Isaac Sim documentation mandates RTX GPU + Omniverse Kit; production deployment requires NVIDIA Enterprise license. iotdigitaltwinplmcom.com 2026 comparison explicitly states this hardware lock-in. Developers needing non-NVIDIA paths default to CPU-based MuJoCo or Gazebo, sacrificing parallelism and synthetic data generation capability.

**Who's affected:** Teams doing sim-to-real for manipulation (requires GPU-parallel domain randomization); startups that cannot afford or do not want NVIDIA cloud costs via OSMO; AMD-centric data center customers (MI300X training, X100 deployment) who want simulation infrastructure consistency.

**Why it's still open:** Building a photorealistic, physics-accurate, GPU-parallel simulator is a multi-year effort. The open-source alternatives (MuJoCo, Gazebo, Brax) are feature-incomplete for this use case. Unity/Unreal have rendering capability but not physics-accurate RL training.

**Opportunity signal:** MJX-JAX already runs on AMD. Wrapping MJX-JAX with a synthetic data pipeline, domain randomization tooling, and a ROCm-optimized renderer would create the first AMD-native sim-to-real stack. This could be a partner/acquisition play (CoppeliaSim already supports 5 backends; Webots is open-source) rather than a greenfield build.

---

### Gap 4: ONNX Runtime ROCm EP Deprecated — Fragmented AMD Inference Path

**What's missing:** ONNX Runtime's ROCm Execution Provider was deprecated in v1.23 (2026) and removed for ROCm 7.1+. The replacement (MIGraphX EP) is less familiar to developers, has no equivalent benchmark visibility vs. TensorRT, and lacks Flash Attention / FP8 support on consumer RDNA cards.

**Evidence:** ORT ROCm EP documentation explicitly states deprecation. AMD's Flash Attention fork has two backends — Composable Kernel (MI-series only) and Triton (CDNA + RDNA experimental) — but the mainline Dao-AILab Flash Attention has no AMD support. HuggingFace TEI has no AMD support (PR #295 stalled 10+ months). FP8 quantization on AMD is MI-series only.

**Who's affected:** Robotics inference pipeline developers using ONNX models (VLAs, object detection, pose estimation); teams who picked ONNX for cross-platform portability and now find the AMD path less supported than CUDA/TensorRT.

**Why it's still open:** MIGraphX is less documented and less community-known than TensorRT. The transition from ROCm EP to MIGraphX EP was quiet (no major migration guide); developer awareness lags.

**Opportunity signal:** AMD publishing a robotics-specific ONNX inference benchmark (MIGraphX vs TensorRT on canonical robotics models: FoundationPose, YOLO, VLA policy heads) with matching documentation would collapse the perception gap. Cost: weeks of engineering + a blog post, not product development.

---

### Gap 5: AMD Edge Hardware Has No Validated Robotics SDK Stack

**What's missing:** The Ryzen AI Embedded X100 + Kria AI Robotics Developer Platform was announced July 2026 with Q4 2026 GA. There is no robotics SDK layer comparable to Isaac ROS 4.0 + NITROS. The internal ROCm-native NITROS equivalent is unreleased. AMD's motion planning answer is MoveIt 2 (CPU). The AMD Robotics Partner Network is nascent.

**Evidence:** AMD's own benchmark material explicitly lists "no Isaac Sim equivalent" and "ROCm not at feature parity for robotics tooling" as acknowledged gaps. Benchmarks were run on Ryzen AI MAX+ 395 consumer chip as proxy — production X100 silicon is not yet available. The COM-HPC form factor is an open standard advantage (vs. Jetson proprietary module), but the surrounding software ecosystem is ~5 years behind NVIDIA's.

**Who's affected:** ODMs designing robotics compute modules; robot OEMs evaluating Jetson Thor alternatives; European/US robotics teams concerned about supply chain diversification.

**Why it's still open:** AMD's robotics focus is recent (2025–2026). Building an SDK ecosystem comparable to NVIDIA's Isaac stack took NVIDIA 7+ years and a sustained multi-hundred-person engineering effort. AMD is starting from a narrow base of ROCm, HIP, MIGraphX, and MoveIt 2.

**Opportunity signal:** LeRobot (PyTorch-native, ICLR 2026) runs on AMD ROCm today with no CUDA dependencies. Co-endorsing LeRobot as the AMD robotics policy learning reference stack, adding AMD GPU benchmarks to MJX documentation, and releasing the internal ROCm NITROS equivalent would establish a credible SDK surface without building from scratch.

---

### Gap 6: No AMD GPU Benchmark Visibility in Sim-to-Real Literature

**What's missing:** AMD GPUs do not appear in published MJX-JAX benchmark tables. Despite MJX-JAX officially supporting AMD via JAX ROCm, no AMD GPU data point exists in the MuJoCo performance documentation. This invisibility means robotics practitioners and researchers making platform decisions cannot evaluate AMD, even though the hardware can technically run the workload today.

**Evidence:** MJX documentation benchmark table includes Apple M3 Max, 64-core AMD 3995WX (CPU baseline only), NVIDIA A100, Google v5 TPU — no AMD GPU. The AMD 3995WX is listed as CPU reference, not GPU showcase. MuJoCo Playground hardcodes CUDA install; AMD is a manual workaround.

**Who's affected:** All robotics researchers making sim-to-real platform decisions; AMD MI300X and Instinct customers who could use existing infrastructure for robot policy training.

**Opportunity signal:** AMD submitting MJX-JAX benchmark results (MI300X, RX 7900 XTX) to Google DeepMind MuJoCo team, and contributing a one-line fix to MuJoCo Playground install docs (add `jax[rocm]` as alternative), costs engineering days and creates permanent visibility in the most-cited sim-to-real toolkit.

---

## Trends Enabling New Solutions

1. **Open-Source Unlocking of Previously Proprietary Stacks**: Isaac Sim 5.0 (Apache 2.0, 2025), cuRobo V2 (Apache 2.0, April 2026), and Newton (Linux Foundation) have all shifted to permissive licenses — removing the licensing barrier to AMD competing on these foundations via ROCm ports.

2. **JAX as Hardware-Agnostic Physics Backend**: JAX/XLA's multi-backend design (CUDA, ROCm, TPU, Metal) means any JAX-based physics library (MJX-JAX, Brax) is AMD-compatible by construction. As more physics work moves to JAX, the Warp gap narrows in scope.

3. **LeRobot's Hardware-Agnostic Policy Learning**: LeRobot's ICLR 2026 acceptance and PyTorch-native design (zero CUDA-specific kernels) gives AMD a credible claim in the policy learning layer without any porting effort. This is AMD's strongest existing bridgehead.

4. **COM-HPC Open Standard**: AMD's X100 uses COM-HPC (open) vs. Jetson's proprietary module. As OEMs increasingly demand vendor-neutral compute modules for supply chain resilience, open-standard form factors gain structural advantage.

5. **CES 2026 "ChatGPT Moment" for Physical AI**: Universal Robots' declaration at CES 2026 signals enterprise robotics deployment is entering exponential growth. Compute diversity demand (cost, supply chain, export control) creates structural pull for non-NVIDIA options even without feature parity.

6. **ONNX as Interoperability Standard**: ONNX's continued adoption as the inter-framework model exchange format means the MIGraphX EP path is viable for the majority of robotics inference workloads that do not require TensorRT-specific optimizations.

---

## Risks & Constraints

| Risk | Impact | AMD-Specific Implication |
|---|---|---|
| Warp ROCm port requires deep CUDA kernel expertise | High effort (~18–24 engineer-months estimated) | Need to recruit/acquire CUDA-to-HIP kernel specialists or partner with academic lab |
| NVIDIA ecosystem network effects (2M+ developers, 7+ year head start) | Structural disadvantage in SDK adoption | ROSCon/ICRA presence and open-source co-contributions are table stakes |
| AMD X100 production slips beyond Q4 2026 | Delays validated hardware for all SDK work | SDK development should proceed against Ryzen AI MAX+ 395 proxy hardware |
| cuRobo port is engineering-intensive (custom CUDA kernels throughout) | Gap 2 may take 12+ months to close | Prioritize Warp port first — cascades into cuRobo partially |
| ONNX Runtime MIGraphX EP coverage gaps (Flash Attention, FP8 on RDNA) | Robotics VLA inference on consumer AMD GPUs is incomplete | Contribute Flash Attention Composable Kernel to RDNA targets; document workarounds |
| Isaac Sim competitors (Unity, Unreal) have rendering advantage but not physics parity | No single AMD-friendly alternative covers full Isaac Sim feature set | Composite stack (MJX-JAX + BlenderProc + LeRobot) is the near-term answer |
| MuJoCo Playground zero-shot transfer is NVIDIA's strongest sim-to-real demonstration | AMD narrative lacks equivalent showpiece | AMD-run MuJoCo Playground experiment on MI300X / X100 with published results fills this |

---

## AMD Competitive Position Summary

| Layer | NVIDIA | AMD Today | Gap Severity |
|---|---|---|---|
| Edge compute TOPS | Jetson Thor: 1,035+ TOPS FP8 | X100: 50 TOPS NPU + 60 TFLOPS GPU | High — 10–20× headline gap; real workload gap narrower on mixed CPU+GPU tasks |
| GPU physics training (Warp/MJX-Warp) | MJX-Warp: 3.35M steps/sec | MJX-JAX: ~300K steps/sec (10× slower) | High — Warp port would close this |
| Motion planning acceleration | cuRobo V2: 37K IK/sec, 100% cluttered success | MoveIt 2 (CPU): 50% success, 10s budget | Critical — no GPU path on AMD |
| Sim-to-real photorealistic training | Isaac Sim 5.0 + Cosmos | No equivalent | Critical — requires build/partner strategy |
| Policy learning framework | Isaac Lab + GR00T | LeRobot (PyTorch, ROCm-compatible) | Moderate — LeRobot is credible, not yet at GR00T scale |
| Inference runtime | TensorRT (NVIDIA-only) | MIGraphX EP (less benchmarked) | Moderate — documentation and benchmarks needed |
| ROS 2 hardware acceleration | Isaac ROS 4.0 + NITROS | Internal effort (unreleased) | High — releasing NITROS equivalent is highest near-term leverage |
| Simulation benchmark visibility | Dominant | Zero AMD GPU data points in MJX docs | Low effort to fix — submit benchmarks |
| Open-source licensing | Apache 2.0 across stack | ROCm open, MIGraphX open | Parity — both stacks are open-source |

---

## L0 Expansion: Real-Time OS, Functional Safety & FPGA Control Layer
*Research date: 2026-08-13 | 16 additional sources*

This section maps the safety/RT OS layer that sits **below** L1 hardware — the deterministic substrate that makes AI-controlled robots legally deployable around humans. It is AMD's most significant unclaimed territory.

### Why This Layer Matters: The Probabilistic AI Problem

AI models (LLMs, VLAs) **cannot be certified** under IEC 61508 — they are structurally probabilistic with non-zero error floors. Certification standards (IEC 61508, DO-178C, ISO 26262) require verifiable, bounded, deterministic behavior. The only path to deploying AI in safety-critical robots is a **deterministic execution envelope** around the probabilistic AI brain. NVIDIA Halos implements this envelope on NVIDIA hardware. AMD has no equivalent [A2].

### NVIDIA Halos for Robotics — Full Stack (June 22, 2026)

Announced at Automate 2026, Chicago. Billed as "the industry's first full-stack safety system for physical AI."

**Hardware layer — IGX Thor:**
- 2,070 FP4 TFLOPs, 14 Arm Neoverse CPU cores, 128GB
- Dedicated **Functional Safety Island (FSI)**: lockstep multicore MCU with isolated clock, power, and memory domains; watchdog timers; ECC memory; CRC mechanisms; direct actuator interfaces — completely isolated from main AI compute
- Hardware designed to ISO 26262 (automotive) and IEC 61508 requirements

**Sensor connectivity — Holoscan Sensor Bridge:**
- ConnectX RDMA + GPU Direct for low-latency sensor streaming
- Scales to hundreds of sensors
- **IEC 61508 SIL 2** safety protocol for sensor data trust validation
- MACsec, device authentication, watermarking

**Software layer — Halos OS:**
- Option A: Linux only (lower safety integrity)
- Option B: **Linux + QNX Safety 8.0** — NVIDIA hypervisor partitions IGX into Linux VM (AI workloads) + QNX VM (safety-critical functions)
- NVIDIA quote on QNX: "a real-time operating system with a long pedigree in certified safety systems… its inclusion enables stronger software partitioning for higher safety integrity use cases"
- Halos Outside-In Safety Blueprint: open-source, external cameras + AI perception + finite-state safety decision maker

**Certification — NVIDIA Halos AI Systems Inspection Lab:**
- ANAB-accredited ISO/IEC 17020 inspection body
- Provides inspection reports usable with: TÜV Rheinland, TÜV SÜD, UL Solutions, exida, SGS, CertX
- Standards targeted: IEC 61508 (functional safety), ISO 13849 (safety-related control systems), ISO/IEC TR 5469 (AI-related functional safety)
- **40+ companies** in the ecosystem

**First production adopter:** Agility Robotics (Digit humanoid; Amazon/GXO/Schaeffler/Toyota customers) [A3]

### RTOS Ecosystem — Full Map

| RTOS | License | Safety Level | Primary Use | Key Partners | AMD Compatible? |
|---|---|---|---|---|---|
| QNX Neutrino 8.0 | Commercial | ASIL-D / SIL 3 | Domain controllers, humanoid safety VM | NVIDIA Halos, Kinova, J&J, Apex.AI | Not integrated |
| Wind River VxWorks | Commercial | ASIL-D / SIL 3 | Industrial automation, aerospace | ABI Research "Leader" | Not integrated |
| SYSGO PikeOS | Commercial | SIL 4 | Rail, avionics | ABI Research "Leader" | Not integrated |
| Green Hills INTEGRITY | Commercial | ASIL-D | Military, automotive | ABI Research "Leader" | Not integrated |
| FreeRTOS | MIT (AWS) | User responsibility | MCU/sensor nodes, <64KB RAM | AMD Kria X100 (FreeRTOS VM) | Partial (FreeRTOS VM on X100) |
| Zephyr | Apache 2.0 (LF) | ISO 26262 support (select configs) | Gateways, RISC-V, CAN | Nordic, NXP, Intel | Yes (generic) |
| ThreadX (Azure RTOS) | MIT/Proprietary | Medical-grade | Medical devices, NASA | Microsoft | Not integrated |
| Mbed OS | Apache 2.0 | Limited | Education, Cortex-M | Arm | Limited (deprecated) |

**ABI Research "Leaders" in RTOS for Robotics Functional Safety (April 21, 2026):** QNX, Wind River, SYSGO, Green Hills Software — all four are commercial, proprietary RTOSes. **None have announced AMD Kria/X100 integration.**

### QNX Market Position

- **Q4 FY26 revenue:** $78.7M (+20% YoY) — record quarter [A2]
- **Royalty backlog:** ~$950M [A2]
- **FY27 guidance:** $290–307M [A2]
- **Installed base:** 275 million vehicles
- **General Embedded Market (GEM):** ~20% of revenue; management believes TAM could exceed automotive
- **Non-automotive wins (2026):**
  - Kinova KIMA surgical arm: QNX OS 8.0 + IEC 62304 Class C; 12–18 months saved vs custom certification
  - Johnson & Johnson AI-driven heart pump: QNX OS for Safety selected
  - India metro rail (Medha): QNX OS for Safety → SIL 3 / EN 50128 SIL 4 target
  - Apex.AI: ROS 2 autonomy framework compatible with QNX SDP 8.0 (Dec 2025)

### Third-Party Safety Controller Ecosystem — NVIDIA-Anchored

**Synapticon POSITRON SAFETY AI:**
- First certifiable solution addressing both mechanical instability AND non-deterministic AI behavior
- SIL3 PLe (TÜV Rheinland certified)
- Safe motion monitoring for **50+ DOF** (industry standard: <10 DOF); safe inverse kinematics up to 7 DOF
- EtherCAT/FSOE Master/Slave; PROFISAFE, CIP Safety, CC-Link Safety
- Integrates with VLMs, VLAs, ROS-based systems
- **Hardware: ARM R52 (2× 800MHz) + NVIDIA IGX Jetson Thor SOM** — NVIDIA-only [A5]

### Regulatory Standards Status (2026)

| Standard | Status | Scope | SIL/ASIL Level |
|---|---|---|---|
| IEC 61508:2010 | Active | Functional safety (all industries) | SIL 1–4 |
| ISO 10218-1/-2:2025 | **Refreshed 2025** | Industrial robots/cells | Up to SIL 3 |
| ISO 13849 | Active | Safety-related control systems | PLa–PLe |
| ISO 13482 | Active (revision underway) | Personal-care robots | — |
| ISO 15066 | Active | Collaborative robot speed/force limiting | — |
| IEC 62304 | Active | Medical device software | Class A/B/C |
| ISO 25785 | **DRAFT — NOT finalized** | Dynamically walking humanoids | — |
| ISO/IEC TR 5469 | Active | AI-related functional safety | — |

**Critical gap: No finalized safety standard for dynamically walking humanoids** (ISO 25785 still in draft). Fenceless deployment certification remains the open barrier for humanoid commercialization at scale [A2].

### AMD's Current Safety/RT Position

**What AMD has:**
- AMD Adaptive SoCs and FPGAs: "For decades, AMD adaptive computing technologies have powered the sensing, safety and real-time control systems at the heart of industrial and surgical robots" — Salil Raje, SVP AMD Embedded [A6]
- Kria X100 FPGA (Spartan UltraScale+): EtherCAT/TSN/CAN-FD deterministic control
- Zen hypervisor + FreeRTOS VM: <7μs interrupt latency target
- 8,000 decisions/second (125μs) demonstrated with Bosch Rexroth controller on X100 [A6]
- Robot reasoning <100ms (Pi0.5 VLA inference, benchmarked by embedL) [A6]

**What AMD lacks:**
- No IEC 61508 SIL 2+ certified inference compute platform (NVIDIA Holoscan Sensor Bridge achieves SIL 2 for sensor connectivity)
- No equivalent to NVIDIA Halos AI Systems Inspection Lab — no accredited certification support body
- No QNX, Wind River, SYSGO, or Green Hills integration announced
- No robotics safety hardware partner (equivalent to Synapticon for NVIDIA)
- AMD ROCm runtime has no safety certification (IEC 61508, ISO 26262)
- FreeRTOS VM on X100 provides determinism but no pre-certified path to SIL 2/3

### AMD Gaps — Real-Time OS & Functional Safety

#### Gap 11: No Certified Safety Envelope for AMD AI Compute
**What's missing:** NVIDIA IGX Thor has a hardware-level Functional Safety Island (isolated MCU, ECC memory, watchdogs) that allows IEC 61508 SIL 2 certification of the safety monitoring layer alongside AI compute. AMD X100 has an FPGA for deterministic control and a FreeRTOS VM, but no equivalent hardware FSI architecture and no path to IEC 61508 SIL 2+ certification for the AI inference layer.

**Evidence:** Synapticon POSITRON SAFETY AI explicitly states it is "NVIDIA IGX Jetson Thor SOM-based" — the safety controller partner ecosystem has already chosen NVIDIA as its compute anchor. AMD's Kria page highlights decades of FPGA safety heritage but no inference-layer safety certification [A5][A6].

**Who's affected:** Robot OEMs building cobots and humanoids that must operate unfenced around people (ISO 13849 PLd/PLe, IEC 61508 SIL 2); European manufacturers subject to Machinery Directive; hospital/surgical robotics (IEC 62304).

**Why it's still open:** IGX Thor's dedicated FSI is a custom silicon feature that required years of automotive safety engineering. AMD Embedded X100 was designed for AI performance, not safety island architecture. Retrofitting a certified safety channel onto an existing SoC is very hard.

**AMD opportunity:** Partner with a commercial RTOS vendor (Wind River, SYSGO, or Green Hills — all ABI Research Leaders) to create a certified software partition on AMD X100 using the existing FPGA as the safety island substrate. AMD's FPGA heritage is the enabling differentiator: the Spartan UltraScale+ already handles deterministic EtherCAT/TSN — certify that path to IEC 61508 SIL 2 and declare the FPGA as the safety channel. Cost: partnership + 18–24 month certification project. Alternative: co-fund the Zephyr RTOS IEC 61508 certification (currently only "partial" support).

---

#### Gap 12: No AMD Equivalent to NVIDIA Halos AI Systems Inspection Lab
**What's missing:** NVIDIA's ANAB-accredited inspection lab provides partners with inspection reports that certification bodies (TÜV, UL, exida) accept. This infrastructure — which took NVIDIA 18,000 engineer-years to build from autonomous vehicles — makes NVIDIA the default choice for robot OEMs who need a certification path. AMD has no equivalent body, no accreditation, and no structured path for AMD-based robots to reach TÜV certification.

**Evidence:** 40+ companies in NVIDIA Halos ecosystem; Agility Robotics is already integrating IGX Thor + Halos into Digit's safety system. Once Digit ships at scale (Amazon/GXO/Schaeffler/Toyota), the safety architecture becomes a de facto standard that is expensive to deviate from [A3][A5].

**Who's affected:** Every robot OEM that needs to ship in regulated environments (EU Machinery Directive, FDA for surgical robotics, OSHA for industrial robotics).

**AMD opportunity:** AMD cannot replicate the NVIDIA inspection lab alone — but it can co-invest with TÜV Rheinland or exida to create an accredited AMD-specific safety evaluation program, leveraging AMD's automotive heritage (AMD DRIVE platform has ISO 26262 work) as credibility evidence.

---

#### Gap 13: ISO 25785 (Humanoid Safety) Standard — Uncontested Participation Opportunity
**What's missing:** ISO 25785 (safety for dynamically walking humanoids) is still in DRAFT with no finalized standard expected before 2027–2028. The standard being written today will determine the hardware architecture requirements for the trillion-dollar humanoid market. NVIDIA is positioned through Halos to influence the IGX-aligned requirements. AMD is not participating.

**Evidence:** "There is no finalized safety standard for a dynamically walking humanoid yet — the relevant standard (ISO 25785) is still in draft, and certifying a robot to work unfenced, around people, remains the open deployment barrier" [A2].

**AMD opportunity:** Nominate AMD engineers to ISO TC 299 (robotics) working groups developing ISO 25785. Low cost, high long-term leverage — standards bodies encode hardware architecture assumptions that become certification requirements for a decade.

### Robotics Safety Market Data

| Segment | 2025 Value | Projection | CAGR |
|---|---|---|---|
| Humanoid market | ~$3B | $38B by 2035 (Goldman Sachs) | — |
| AMR (Autonomous Mobile Robot) | $4.5–5.3B | Growing 17–22%/year | ~20% |
| QNX annual revenue | $313M (FY26) | $290–307M (FY27 guidance) | — |
| QNX royalty backlog | $950M | — | — |

---

## L3 Expansion: VLA & Foundation Models — Edge Deployment Layer
*Research date: 2026-08-13 | 24 additional sources*

This section maps the VLA/foundation model layer that sits on top of L1 hardware and L2 simulation — where inference runs on the edge device and where AMD's hardware story ultimately needs to land.

### VLA Model Landscape (full taxonomy)

#### Closed / Commercial-Weight Models
| Model | Owner | Params | Action Type | Control Hz | Hardware Requirement |
|---|---|---|---|---|---|
| Gemini Robotics 2 | Google DeepMind | Undisclosed | VLA (cloud) | — | Cloud inference |
| Gemini Robotics ER 2 | Google DeepMind | Undisclosed | VLM agent | — | Cloud |
| Gemini Robotics On-Device 2 | Google DeepMind | Undisclosed | VLA (on-device) | — | Hardware-agnostic |
| Helix / Helix 02 | Figure AI | 7B (System 2) + 80M (System 1) | Dual-system | 200Hz | Figure 02 humanoid |
| π0 / π0.5 | Physical Intelligence | 3B | Flow-matching | 50Hz | 48GB+ VRAM (fine-tune) |

#### Open-Weight Models
| Model | License | Params | VRAM (inference) | Hardware | ROCm-compatible? |
|---|---|---|---|---|---|
| OpenVLA | Apache 2.0 | 7B (Llama2+DINOv2+SigLIP) | 16GB+ | Any 16GB+ GPU | Yes (PyTorch) |
| SmolVLA | Open | 450M | 4GB | MacBook / edge GPU | Yes |
| GR00T N1 / N1.5 / N1.6 | Weights available | 2.2B | ~24GB | **Fine-tune requires NVIDIA** | Fine-tune: No |
| GR00T N1.7 | Weights available | 2.2B | ~24GB | Isaac Teleop integration | Fine-tune: No |
| GR00T-H (surgical) | Open | 3B (N1.6 arch) | ~32GB | 32× A100 for training | Training: No |
| Pi0 / Pi0Fast / Pi0.5 | Partial open | 3B | 48GB+ | Training on H100 cluster | Training: No (CUDA) |
| Octo | MIT | 27M / 93M | Low | Any GPU | Yes |
| RT-X / RT-1-X | Apache 2.0 | — | — | JAX checkpoints | Yes (JAX ROCm) |
| InternVLA-M1 | MIT | — | — | Standard GPU | Yes |
| RoboFlamingo | MIT | — | — | Standard GPU | Yes |
| BridgeVLA | Open | — | — | Standard GPU | Yes |
| Diffusion Policy | Open | — | Low | Any GPU | Yes |
| ACT | Open | Small | Low | Any GPU | Yes |
| XVLA / EO-1 / MolmoAct2 / WALL-OSS / EVO1 | Open (via LeRobot) | Various | Various | Standard GPU | Yes |

#### Dual-System Architecture (2025–2026 convergence)
All production-grade VLAs have converged on a two-system design:
- **System 2** (slow, 7–9 Hz): VLM backbone — visual + language understanding (Cosmos-2B, PaLI-Gemma, Eagle 2.5, Gemini 2.0)
- **System 1** (fast, 100–200 Hz): Motor control — diffusion transformer or flow-matching action expert (Figure S1 is 80M params)

#### Key Datasets
- **Open X-Embodiment**: 970K+ episodes, 22 robot types, 33 institutions — foundation for OpenVLA, GR00T, RT-X
- **AgiBot World** (Chinese): Larger and "higher quality" than Open X-Embodiment per AgiBot claims; hundreds of tele-operated robots in Shanghai
- **LeRobotDataset Hub**: 58,000+ community datasets (Parquet + MP4 format) on Hugging Face Hub
- **Open-H-Embodiment** (surgical): 770 hours, 124,019 episodes, 20 robotic platforms, 49 institutions — used for GR00T-H

#### LeRobot (Hugging Face) — AMD's Best Existing Bridgehead
- PyTorch-native, zero CUDA-specific kernels; ICLR 2026 paper; hardware-agnostic
- Supports: ACT, Diffusion Policy, SmolVLA, Pi0/Pi0Fast/Pi0.5, GR00T N1.7, XVLA, EO-1, MolmoAct2, WALL-OSS, EVO1
- World Models in-progress: VLA-JEPA, LingBot-VA, FastWAM
- Hardware support: SO100, Koch, Unitree G1, Reachy2, OpenARM, reBot B601, and community plugins (UR5e, Franka, xArm, etc.)
- GR00T N1.7 + Isaac Teleop announced integrated into LeRobot (MACHINA 2026) — but Isaac Teleop is NVIDIA-specific

#### Proven AMD VLA Pipeline (Community-Validated)
**Datawhale "Every Embodied" project** (datawhalechina.github.io) has replicated ACT, SmolVLA, Pi0, and Pi0.5 training and deployment on **AMD Ryzen AI MAX+ 395 / ROCm**:
- Full pipeline: MuJoCo teleoperation → LeRobot dataset format → ROCm training → closed-loop sim evaluation
- Validates: PyTorch + ROCm + LeRobot + MuJoCo stack is functional on AMD today
- Caveat: Unified memory architecture on Ryzen AI MAX+ 395 requires careful GPU/system memory allocation monitoring; ROCm/PyTorch/LeRobot version alignment is non-trivial
- Finding: "The truly difficult part usually isn't changing cuda strings to hip, but aligning model dependencies, data formats, action semantics, execution frequency, and physical evaluation protocols simultaneously"

### Market Data — VLA / Embodied AI

| Metric | Value | Source |
|---|---|---|
| Embodied AI market 2025 | $4.44 trillion (including all physical AI) | VnRobo |
| Embodied AI growth rate | 39% CAGR → $23T by 2030 | VnRobo |
| Morgan Stanley humanoid TAM (2050) | $5 quadrillion | Morgan Stanley |
| Physical Intelligence valuation | $5.6B ($1.1B total funding including $600M recent) | VnRobo |
| Robotics startup funding 2025 | $22.2B (69% YoY increase) | VnRobo |
| OpenVLA training cost | 64× A100 GPUs, 15 days | OpenVLA |
| GR00T-H training cost | 32× A100 80GB, ~1.5 days | emergentmind.com |
| GR00T N1.5 inference latency | 80ms on Jetson Thor; was 220ms on Jetson AGX Orin | omnimes.com |
| OpenVLA inference latency | 60–80ms on RTX 4090 | omnimes.com |
| SmolVLA VRAM requirement | 4GB (runs on MacBook) | serendeep.tech |
| Pi0 VRAM requirement (inference) | 48GB+ | serendeep.tech |

### AMD Gaps — VLA / Foundation Models

#### Gap 7: GR00T Fine-Tuning Locked to NVIDIA Hardware
**What's missing:** GR00T N1.5/N1.6/N1.7 — the most production-grade open-weight VLA — explicitly requires NVIDIA hardware (Jetson Thor or H100/B200 server) for fine-tuning and training. AMD users can download weights but cannot participate in the GR00T fine-tuning workflow. GR00T N1.7 integration into LeRobot ships with Isaac Teleop, which is also NVIDIA-specific.

**Evidence:** Source [2] states directly: "GR00T is open weight, but training and fine-tuning require NVIDIA hardware (Jetson Thor or a server with H100/B200). For smaller plants that means an additional USD 5–20k on hardware vs OpenVLA on a consumer GPU." GR00T-H training used 32× A100 80GB GPUs — no AMD MI300X equivalent training recipe published [6].

**Who's affected:** Manufacturing integrators adopting GR00T for FANUC/KUKA/ABB robots; humanoid developers on AMD infrastructure; European mid-market that prefers x86 open-standard compute.

**AMD opportunity:** Publish a ROCm training recipe for GR00T N1.x on MI300X (192GB HBM3 is sufficient for the 3B model). A single reproducible `lerobot-train --policy.type=gr00t_n1 --device=rocm` example in the LeRobot codebase would establish AMD as a supported training platform. AMD should contribute this to the LeRobot repo rather than maintaining a fork.

---

#### Gap 8: No Official AMD VLA Benchmark Numbers
**What's missing:** No VLA model (OpenVLA, SmolVLA, Pi0, GR00T, Octo) has published inference benchmarks on AMD hardware. The Datawhale "Every Embodied" project has demonstrated feasibility on Ryzen AI MAX+ 395, but no throughput, latency, or success-rate numbers exist that AMD could cite to practitioners evaluating hardware.

**Evidence:** SmolVLA runs on 4GB VRAM (MacBook-class) and is PyTorch-native — it can run on AMD GPUs today with zero porting. OpenVLA's 7B model at 16GB VRAM maps to AMD RX 7900 XTX (24GB) or Radeon AI PRO R9700 (32GB). Yet no AMD GPU appears in any VLA paper's hardware comparison table [4][12].

**Who's affected:** Robotics teams making hardware selection decisions for VLA inference; AMD Kria X100 positioning vs. Jetson Thor for on-robot VLA deployment.

**AMD opportunity:** Run SmolVLA and OpenVLA inference benchmarks on: (a) MI300X (data center training baseline), (b) Radeon AI PRO R9700 (workstation inference), (c) Ryzen AI MAX+ 395 (robotics edge). Publish numbers. Submit PRs to OpenVLA and SmolVLA repos adding AMD GPU to hardware table. Cost: ~1 week of engineer time.

---

#### Gap 9: Isaac Teleop Integration in LeRobot Excludes AMD
**What's missing:** NVIDIA's announcement at MACHINA 2026 integrated Isaac Teleop directly into LeRobot as the canonical teleop data collection pipeline for GR00T N1.7. This gives NVIDIA-hardware users a seamless sim-to-data-to-policy pipeline within LeRobot. AMD users have no equivalent — they must use community MuJoCo teleoperation (functional but unsupported) or third-party VR teleoperation tools.

**Evidence:** LinkedIn/MACHINA 2026 announcement confirms Isaac Teleop + GR00T N1.7 integration in LeRobot [10]. "Every Embodied" project uses MuJoCo keyboard teleoperation as AMD workaround [5].

**Who's affected:** Any AMD-hardware team trying to collect demonstration data for VLA fine-tuning in a supported pipeline.

**AMD opportunity:** Contribute an AMD-compatible teleop plugin to LeRobot using an open teleoperation standard (keyboard, SpaceMouse, or open VR controller path) that does not depend on Isaac infrastructure. The LeRobot plugin system (`lerobot_teleoperator_*` package prefix) is designed for exactly this.

---

#### Gap 10: VLA Training Cluster Market — AMD MI300X Unclaimed
**What's missing:** GR00T training runs cost 32–64× A100s for days. As VLA models grow toward >100B parameters (predicted before end 2026), training costs scale into thousands of A100-days. AMD MI300X (192GB HBM3, 5.3 TB/s) is technically superior to A100 for memory-bound workloads, yet no VLA lab has published MI300X training runs or ROCm training recipes.

**Evidence:** OpenVLA trained on 64× A100 for 15 days [8]. GR00T-H on 32× A100 80GB for 1.5 days [6]. Physical Intelligence ($5.6B valuation) and Figure AI ($2.6B) are both actively training VLA models at scale — both currently CUDA-dependent. Robotics startup funding was $22.2B in 2025 [3].

**Who's affected:** Well-funded VLA startups facing A100/H100 supply constraints; cloud providers wanting to offer AMD MI300X-based VLA training.

**AMD opportunity:** Sponsor one major open VLA training run on MI300X (OpenVLA re-training or GR00T fine-tuning), publish the cost comparison vs A100. This single benchmark would establish AMD's data center GPU as a viable VLA training platform — the training market dwarfs the inference market in near-term revenue.

---

### Trends Enabling AMD's VLA Entry

1. **LeRobot as the hardware-agnostic standard** — ICLR 2026 acceptance and 19M developer access (via Hugging Face) makes LeRobot the de-facto open VLA framework. Every model AMD contributes to LeRobot reaches this entire audience with no additional distribution effort.

2. **SmolVLA 450M at 4GB VRAM** — The efficiency curve is compressing VLA inference into AMD Kria X100 territory. SmolVLA already runs on MacBook (Apple Silicon, 4GB GPU). The AMD Ryzen AI MAX+ 395 with 128GB unified memory and 60 TFLOPS GPU can run SmolVLA with significant headroom.

3. **ROCm 7.14.0 "TheRock" modular release (July 2026)** — Transitions ROCm to a modular ecosystem (PyTorch 2.12, JAX 0.10, vLLM 0.23). This is the most significant ROCm architectural change since launch — reduces dependency friction that "Every Embodied" encountered.

4. **Community validation exists** — Datawhale's "Every Embodied" proves ACT/SmolVLA/Pi0/Pi0.5 on Ryzen AI MAX+ 395 + ROCm is feasible today. AMD can amplify and officially support this community work rather than building from scratch.

5. **GR00T N1.5 latency improvement** (220ms → 80ms on Jetson Thor) shows VLA inference is entering the sub-100ms real-time window — this is where edge hardware differentiation matters and where AMD's X100 FPGA-backed deterministic compute is differentiated.

---

## Sources

[1] AMD Launches Ryzen AI Embedded X100 processors, Kria AI SoM and Physical AI Robotics Developer Platform — https://www.cnx-software.com/2026/07/24/amd-launches-ryzen-ai-embedded-x100-processors-kria-ai-som-and-physical-ai-robotics-developer-platform/

[2] AMD Challenges Nvidia Jetson with Ryzen AI Embedded X100 and Kria Robotics Platform — https://www.houdao.com/d/18307-AMD-Challenges-Nvidia-Jetson-with-Ryzen-AI-Embedded-X100-and-Kria-Robotics-Platform

[3] Edge AI Hardware 2026: On-Device Intelligence, Architecture Comparison — https://neuralcoretech.com/edge-ai-hardware-2026-chip-comparison/

[4] AMD Launches Kria AI Robotics Developer Platform With Ryzen X100 — https://embodiedglobal.com/en/article/amd-kria-ai-robotics-developer-platform-ryzen-x100

[5] Edge AI Hardware Market Report 2026 — https://www.mordorintelligence.com/industry-reports/edge-ai-hardware-market

[6] Edge AI Inference at Scale: NVIDIA Jetson, Intel, and Arm NPU — https://iotdigitaltwinplm.com/edge-ai-inference-nvidia-jetson-intel-movidius-arm-npu/

[7] Isaac Sim vs Gazebo vs MuJoCo: Choosing a Robot Simulator in 2026 — https://iotdigitaltwinplm.com/isaac-sim-vs-gazebo-vs-mujoco-robot-simulation-comparison-2026/

[8] Robotics Simulation Platforms Powered By AI Models Reviewed — https://aitechmodel.com/robotics-simulation-platforms-powered-by-ai-models-reviewed/

[9] MuJoCo XLA (MJX) Documentation — https://mujoco.readthedocs.io/en/stable/mjx.html

[10] GitHub — google-deepmind/mujoco_warp — https://github.com/google-deepmind/mujoco_warp

[11] GitHub — google-deepmind/mujoco_playground — https://github.com/google-deepmind/mujoco_playground

[12] cuRobo Official Documentation / NVLabs GitHub — https://curobo.org/ and https://github.com/NVLabs/curobo

[13] cuRobo V2 (Nvidia) and ROS2 for Robotic Motion Planning — https://www.blackcoffeerobotics.com/blog/curobo-nvidia-and-ros2-for-motion-planning

[14] ONNX Runtime ROCm Execution Provider (deprecated notice) — https://onnxruntime.ai/docs/execution-providers/ROCm-ExecutionProvider.html

[15] AMD GPUs for AI Inference in 2026: What Works, What's Broken — https://www.idfs.ai/blog/amd-gpus-for-ai-inference-2026

[16] AMD GPU for AI in 2026: ROCm Status Update — https://gigagpu.com/amd-gpu-ai-2026-rocm-update/

[17] NVIDIA vs AMD GPUs in 2026: CUDA, ROCm & Market Comparison — https://www.gpunex.com/blog/nvidia-vs-amd-gpus-2026/

[18] GitHub — huggingface/lerobot — https://github.com/huggingface/lerobot

[19] ICRA 2026 Program (sim-to-real papers) — https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html

[20] MuJoCo — Advanced Physics Simulation — https://mujoco.org/

[21] NVIDIA Isaac Sim Developer Page — https://developer.nvidia.com/isaac/sim

[22] Simulation for Robotics: MuJoCo vs Isaac Sim vs Gazebo — https://vnrobo.com/en/blog/sim-series-1-overview

[23] Isaac Sim vs MuJoCo vs Gazebo: Robotics Simulator Comparison — https://rigyd.com/compare/isaac-sim-vs-mujoco-vs-gazebo

[24] Robot Simulation Software Compared: MuJoCo, Isaac Sim, Gazebo — https://www.roboticscenter.ai/learn/robot-simulation-software-comparison

[25] Edge Computing for Robotics: NVIDIA Jetson, Real-Time AI — https://srphm.ai/pages/robotics/edge-computing-robotics

[26] Accelerate AI Inference for Edge and Robotics with NVIDIA Jetson T4000 — https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/

[27] NVIDIA Introduces New Jetson Thor Computers — https://blogs.nvidia.com/blog/jetson-thor-robotics-edge-ai-agent/

[28] Accelerated inference on AMD GPUs via Hugging Face Optimum-ONNX — https://huggingface.co/docs/optimum-onnx/onnxruntime/usage_guides/amdgpu

[29] Best Physical AI Development Tools and Frameworks in 2026 — https://www.analyticsinsight.net/artificial-intelligence/best-physical-ai-development-tools-and-frameworks-in-2026

[30] Discover the Leading Physical AI Tools for Robotics in 2026 — https://www.analyticsinsight.net/artificial-intelligence/best-physical-ai-development-tools-and-frameworks-in-2026

*— VLA / Foundation Models expansion (added 2026-08-13) —*

*— Real-Time OS, Functional Safety & FPGA Control expansion (added 2026-08-13) —*

[31] VLA Models Powering the Future of Robotics — https://dzone.com/articles/vision-language-action-vla-models-powering-robotic

[32] Robot Foundation Models in the factory: Pi-Zero, OpenVLA, GR00T N1.5 — https://www.omnimes.com/en/blog/robot-foundation-models-in-the-factory-pi-zero-openvla-groot-n1-5-the-end-of-teach-pendant-programming

[33] Embodied AI 2026: Overview and Trends — https://vnrobo.com/en/blog/embodied-ai-2026-landscape

[34] VLA & VLM Model Directory: OpenVLA, Octo, RT-X, π0 — https://www.roboticscenter.ai/vla-models

[35] The Rise of Physical AI and VLA Models — https://cosys-airsim.com/the-rise-of-physical-ai-and-vla-models/

[36] VLA & RFM Progress (chronological model timeline) — https://sudoremove.com/en/knowledge/essays/insights/vla-rfm-progress/

[37] OpenVLA: An Open-Source Vision-Language-Action Model — https://openvla.github.io/

[38] GR00T-H: Open VLA Model for Surgical Robotics — https://www.emergentmind.com/topics/gr00t-h

[39] GitHub — huggingface/lerobot — https://github.com/huggingface/lerobot

[40] Embodied AI — Why 2026 Became the Year of Humanoid Robots — https://unitree.kz/en/blog/embodied-ai-2026-god-robotov-gumanoidov

[41] Hugging Face Expands Open Robotics with GR00T 1.7 (MACHINA 2026) — https://www.linkedin.com/posts/arundhati-banerjee-130912a0_machina2026

[42] VLA Models Demystified — https://blog.serendeep.tech/blog/vla-models-demystified

[43] Every Embodied: Replicating Embodied Intelligence Policies on ROCm — https://datawhalechina.github.io/hello-rocm/05-amd-yes/every-embodied

[44] AMD ROCm tutorials, GPU architecture table, framework support — https://datawhalechina.github.io/hello-rocm/04-references/

[45] Run Meta Muse Glimmer 30B on AMD Ryzen AI Max and Radeon GPUs — https://www.amd.com/en/blogs/2026/run-meta-muse-glimmer-30b-on-amd-ryzen-ai-max-and-radeon-gpus.html

[46] The Robot Needs a Reflex: QNX and the Physical-AI Safety Layer — https://bananarat.com/blogs/blog/qnx-robotics-humanoid-safety-layer

[47] NVIDIA Halos Turns Robot Safety Into a Full-Stack AI Platform — https://techscurrent.com/2026/06/nvidia-halos-robotics-safety-physical-ai/

[48] POSITRON Safety AI for AI-based Robotics — https://www.synapticon.com/en/products/positron-safety-ai

[49] AMD Kria AI Solutions — https://www.amd.com/en/products/system-on-modules/kria/ai.html

[50] AMD Kria AI Solutions launched for Physical AI — https://ucadvanced.com/amd-kria-ai-solutions-launched-for-physical-ai/

[51] AMD extends AI portfolio with Ryzen X100 and Kria SoM for demanding robotics — https://noah-news.com/amd-extends-ai-portfolio-with-ryzen-x100-and-kria-som-for-demanding-robotics-and/

[52] Automotive AI RTOS Comparison: QNX vs FreeRTOS vs Zephyr — https://www.pudn.club/qnx/automotive-ai-rtos-comparison-qnx-vs-freertos-vs-zephyr/

[53] Choosing an RTOS for Your Device: FreeRTOS vs Zephyr vs ThreadX — https://promwad.com/news/choosing-rtos-freertos-zephyr-threadx-comparison

[54] Why Large Language Models Cannot Be Certified for Safety-Critical Systems — https://americanimpactreview.com/article/e2026066

[55] IEC 61508 — Wikipedia — https://en.wikipedia.org/wiki/IEC_61508

[56] QNX Embedded Software & Solutions — https://qnx.software/

[57] $349 AMD Kria KR260 Robotics Starter Kit takes on NVIDIA Jetson AGX Xavier — https://www.cnx-software.com/2022/05/18/349-amd-kria-kr260-robotics-starter-kit-takes-on-nvidia-jetson-agx-xavier-devkit/
