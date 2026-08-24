# Physical AI & Robotics: Tech Ecosystem Gap Analysis
*Research date: 2026-08-11 | Sources: 9 live web searches, GitHub/HuggingFace, analyst reports*

---

## Executive Summary

Physical AI — AI embedded in machines that perceive and act in the physical world — is transitioning from research demos to production deployments in 2026. The market spans $5–21B today (scope-dependent) growing to $50–182B by 2034. NVIDIA dominates every layer of the software ecosystem: simulation (Isaac Sim), foundation models (GR00T), developer gateway (LeRobot), and hardware (Jetson Thor). AMD has hardware parity arguments with the Ryzen AI Embedded X100 and Kria AI platform (announced July 2026, GA Q4 2026), but faces the same softpower gap that exists in Voice AI: absent from every on-ramp above the compute layer — no simulation containers, no foundation model integration, no training pipeline, no HuggingFace presence. The data bottleneck (not compute) is the binding constraint in Physical AI — and NVIDIA controls the synthetic data factory.

---

## Market Overview

| Metric | Value |
|---|---|
| Physical AI market (2025) | $5–21B (scope-dependent across analysts) |
| Physical AI market (2034) | $50–182B @ 32–47% CAGR |
| Humanoid robot market (2025) | **$2.9B** |
| Humanoid robot market (2035) | **$38B** (Goldman Sachs) |
| Physical AI silicon market (2035) | **$200B** (AMD's own projection) |
| Software segment CAGR (→2034) | **54.7%** — fastest-growing layer |
| Hardware share of 2025 revenues | **56.4%** — dominant today |
| Humanoid robots' Physical AI share | **42%** in 2025 |
| Consumer robotics CAGR | **44.6%** — fastest-growing sub-segment |
| Industrial robots CAGR in Physical AI | **56.7%** (2026–2032, MarketsandMarkets) |
| Enterprises with pilot/production embodied AI | **340+** in 28 countries (from <80 in 2023) |
| Robotics VC funding (Jan–Sep 2025) | **$8.5B** |
| NVIDIA robotics YoY growth | **72%** |
| Robotics as % of NVIDIA revenue | **1%** — but growing fast |
| Agricultural AI market (2026) | **$3.37B** @ 24.5% CAGR |
| AMR at Amazon alone | **1M+ robots** deployed |

**Regional:** North America leads; Asia-Pacific fastest growing (33.51% CAGR) driven by China Made in China 2025 + robot density targets. $2.7B VC deployed in embodied AI rounds in North America in 2025 alone.

---

## Current Ecosystem Map

### NVIDIA's Full Stack (The Platform AMD is Fighting)

NVIDIA's strategy: become the Android of robotics — hardware + software vendor powering the default, like Android for smartphones.

#### Layer 1 — Silicon
- **Jetson AGX Thor** (Blackwell, GA Aug 2025): 2,070 FP4 TOPS · 128 GB · 7.5× Orin AI perf · 3.5× more energy-efficient · 130W TDP · dev kit **$3,499**
- **Jetson T5000**: lower-cost Thor variant, 1,200 TOPS · 64 GB · 40–70W
- **Installed base**: 2M+ robotics developers, 7,000+ companies on Jetson Orin

#### Layer 2 — OS/Runtime
- **JetPack 7**: SBSA ARM-server standard · unified CUDA 13.0 across all Arm targets · enterprise-grade OS support

#### Layer 3 — Simulation (The Data Moat)
- **Isaac Sim 5.0** (open-sourced 2025): PhysX GPU physics · RTX ray-traced rendering · full ROS 2 bridge · domain randomization for synthetic training data
- **Isaac Lab**: GPU-parallelized robot training environments
- **Isaac Lab-Arena** (CES 2026, open on GitHub): unified benchmark with LIBERO, RoboCasa, RoboTwin — integrated into **LeRobot's Environment Hub**
- **Cosmos Predict 2.5 + Transfer 2.5**: world foundation models for synthetic trajectory generation — **780K trajectories generated in 11 hours** from single-image input
- **MuJoCo-Warp** (NVIDIA–DeepMind joint project): **>70× GPU acceleration** for robot RL workloads — CUDA-native

#### Layer 4 — Foundation Models
- **GR00T N1.7** (early access, commercial license): open VLA for humanoid robots · integrated into LeRobot · post-train and deploy through HuggingFace workflows
- **GR00T N2** (preview): DreamZero architecture · **2× success rate** on new tasks vs leading VLAs
- **Cosmos Reason 2**: reasoning VLM (Qwen3-VL base) feeding GR00T action head
- **GR00T N1.7 on Jetson Thor + TensorRT**: **3.5× faster inference** vs Orin on W4A16 quant
- LeRobot also integrates: pi0/pi0-FAST (Physical Intelligence), OpenVLA 7B (970K trajectories), X-VLA (290K episodes), SmolVLA — all trained on NVIDIA infrastructure

#### Layer 5 — Robotics SDK
- **Isaac ROS**: CUDA-accelerated ROS 2 packages — cuVSLAM, nvblox (3D mapping), full perception pipeline
- **cuVSLAM / nvblox**: visual SLAM + 3D scene reconstruction, GPU-native
- **Isaac Teleop**: teleoperation data collection framework — now integrated into LeRobot
- **GR00T-Dreams blueprint**: generates synthetic motion data with **zero teleoperation input**

#### Layer 6 — Developer Gateway (The Softpower Layer)
- **LeRobot** (Hugging Face partnership, July 2026): GR00T N1.7 + Isaac Teleop + Isaac Lab-Arena + Cosmos 3 (coming) all integrated
  - **15M dataset downloads** · 350K+ real/simulated trajectories · 57M grasps
  - NVIDIA connects **3M robotics developers** with HuggingFace's **16M AI builders**
- **Physical AI Open Datasets** on HuggingFace: **4.8M downloads** of NVIDIA-hosted data
- **Open Humanoid Robot Reference Design** (GTC Taipei, June 2026): Unitree H2 Plus + Sharpa hands + Jetson Thor + GR00T — full open-source stack, available late 2026

#### Layer 7 — Partner Ecosystem
- **110 robot brain developers** partnered at GTC 2026
- Industrial OEM lock-in: **ABB, FANUC, KUKA, Universal Robots, Yaskawa** — all SDK-certified on NVIDIA
- Humanoid leaders on NVIDIA: **Boston Dynamics** (Atlas + Google DeepMind, Hyundai 30K units/year by 2028), **Agility Robotics** (100K+ totes at GXO warehouse), **Figure AI** (30,000 BMW X3 vehicles on Figure 02)
- SI/ISV: Amazon Robotics (1M+ units), Caterpillar (Jetson Thor + Riva inside bulldozer cab), Siemens, KUKA, ADLINK certified OEMs

### Key Open-Source Robotics Models (HuggingFace / GitHub)

| Model | Developer | Parameters | Training Data | Key Feature |
|---|---|---|---|---|
| **GR00T N1.7** | NVIDIA | — | NVIDIA datasets | Commercial license, in LeRobot |
| **π0** | Physical Intelligence | — | OXE + PI dataset | Multi-robot generalist, flow model |
| **π0-FAST** | Physical Intelligence | — | Same | 5× faster with FAST/DCT tokenization |
| **π0.5** | Physical Intelligence | — | Web + robot data | Open-world generalization |
| **OpenVLA** | OpenVLA team | **7B** | 970K trajectories (OXE) | LoRA fine-tuning, REST API serving |
| **X-VLA** | Research | **0.9B** | 290K episodes | Cross-embodiment via soft prompts |
| **SmolVLA** | HuggingFace | Small | — | Lightweight deployment |

- [`github.com/huggingface/lerobot`](https://github.com/huggingface/lerobot) — the open-source developer gateway
- [`github.com/openvla/openvla`](https://github.com/openvla/openvla) — OpenVLA 7B

### AMD's Current Position (as of Aug 2026)

**Hardware announced (Advancing AI 2026, July 2026):**
- **Ryzen AI Embedded X100**: 16-core Zen 5 + RDNA 3.5 iGPU (40 CUs) + XDNA 2 NPU (~50 TOPS at 2W) · -40 to 105°C · 10-year longevity · unified memory · sampling Jun 2026 · **GA Q4 2026**
- **Kria AI SOM**: COM-HPC standard · 125 µs CPU control loop (8,000 decisions/sec) · sub-100ms VLA reasoning
- **Kria AI Robotics Developer Platform**: Spartan UltraScale+ FPGA carrier · GMSL cameras · CAN-FD · EtherCAT/TSN · IMU · Xen hypervisor for RT + GPOS isolation

**Performance claims vs Jetson T5000** *(AMD-commissioned via Open Navigation LLC — no independent validation):*
- 3.4× better real-time reliability · 1.6× more CPU cores · 3× higher FP32 · 2.3× more concurrent agents · 2.1× higher multithread CPU perf vs Intel Core Ultra Series 3

**Software stack:** ROS 2, MoveIt, PyTorch, ONNX, ROCm open stack · 75% CUDA code preserved in migration · Ryzen AI CVML Library for ROS 2 (perception tasks)

**Partner Network (July 2026):** 30+ companies · free entry tier · Analog Devices, SICK, Voyant Photonics · ODM SOMs: Arbor, Congatec, iBase, IEI, Sapphire, Seavo

**ROCm status signal (adjacent — vLLM):**
- Nov 2025: 37% tests passing → Jan 2026: **93% passing** — significant momentum
- ROCm CI pipeline live Dec 29, 2025; pre-built Docker image Jan 2026
- Still missing: Windows support, bitsandbytes quantization, reliable RDNA fine-tuning

### Qualcomm (Most Credible Chip Competitor)
- **QIRP SDK**: full robotics SDK with hardware-accelerated SLAM, vision AI, motion control on Hexagon NPU — real ROS 2 integration with sample apps and Gazebo simulation
- Competes for efficiency-first (not performance-headroom) segment

---

## Ecosystem Gaps

### Gap 1 — Training Loop Moat

**What's missing:** AMD has no play in the VLA training pipeline. Every training tool is CUDA-native with no ROCm path.

**Evidence:** In a survey of 1,228 VLA papers analyzed at ICLR 2026, zero mention ROCm. MuJoCo-Warp, Cosmos, Isaac Lab, cuVSLAM — all CUDA-only. The data bottleneck ($100/hr teleoperation, 200 demos/worker/day, needing 100-1000× more scale) means whoever controls the synthetic data pipeline controls the model supply chain. NVIDIA's DreamGen produced 780K trajectories in 11 hours — AMD has nothing comparable.

**Who's affected:** Every robotics startup, academic lab, and foundation model developer needing to train or fine-tune on non-NVIDIA hardware.

**Why it's still open:** Training infrastructure requires deep CUDA kernel work. AMD has vLLM inference parity but zero robotics training tooling.

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| Isaac Lab (GPU-parallel RL) | ROCm RL training environment | **Absent** |
| MuJoCo-Warp (70× GPU accel) | ROCm MuJoCo | **Absent** |
| Cosmos world models (synthetic data) | AMD synthetic data pipeline | **Absent** |
| GR00T-Dreams (0 teleoperation needed) | AMD data factory | **Absent** |
| Isaac Teleop (in LeRobot) | AMD teleoperation tools | **Absent** |
| NeMo → TensorRT export loop | ROCm training → deployment | **Partial** |

**Opportunity signal:** Synthetic data factories are capital-intensive but the output (datasets) can be open-sourced. An AMD-compatible data pipeline on MI300X + Cosmos-class open world model would directly serve the 100-1000× data gap the entire industry faces.

---

### Gap 2 — Simulation Ecosystem

**What's missing:** No AMD-accelerated simulation stack. Gazebo works without NVIDIA but is unaccelerated. MuJoCo runs CPU-only without CUDA.

**Evidence:** 8 synthetic samples = 1 real teleoperated sample for manipulation tasks. Scale demands GPU simulation. Isaac Sim 5.0 is open-source — but PhysX + RTX rendering are CUDA-native.

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| Isaac Sim 5.0 (open-sourced 2025) | ROCm GPU physics simulation | **Absent** |
| Isaac Lab-Arena (in LeRobot) | AMD unified sim benchmark | **Absent** |
| Cosmos Predict 2.5 (world model) | AMD world model | **Absent** |
| RTX ray-traced rendering | AMD RT rendering for robotics | **Absent** |

**Who's affected:** All robot learning teams without NVIDIA hardware.

**Why it's still open:** GPU simulation requires low-level GPU kernel integration. NVIDIA has PhysX + Warp — AMD has no equivalent robotics compute primitives.

**Opportunity signal:** Isaac Sim is open-source. An AMD-accelerated Gazebo Harmonic or ROCm MuJoCo backend could be a credible alternative.

---

### Gap 3 — Foundation Model & HuggingFace Developer Gateway

**What's missing:** NVIDIA is the default at the LeRobot call site. AMD is entirely absent.

**Evidence:** LeRobot v0.6.0 (July 2026) ships GR00T N1.7, MolmoAct2, EO-1, EVO1, FastWAM, VLA-JEPA — all NVIDIA ecosystem or CUDA-native. 15M dataset downloads, 4.8M from NVIDIA Physical AI Open Datasets. Search results across the entire robotics literature contain "no significant mentions of ROCm" in VLA training pipelines.

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| GR00T N1.7 in LeRobot | AMD foundation model in LeRobot | **Absent** |
| Isaac Lab-Arena in LeRobot | AMD sim environment in LeRobot | **Absent** |
| Cosmos 3 in LeRobot (coming) | — | **Absent** |
| 4.8M downloads NVIDIA datasets | AMD-hosted robotics datasets | **Absent** |
| NVIDIA GPU assumed in all training docs | ROCm training path documented | **Absent** |

**Who's affected:** 16M HuggingFace developers, 3M NVIDIA-defined robotics developers — AMD is invisible to all of them.

**Why it matters:** Same as `ChatNVIDIA(...)` in the Voice AI stack — the `lerobot.train(policy="groot")` call site encodes the hardware dependency before the developer thinks about compute. AMD needs a named package in LeRobot.

---

### Gap 4 — Developer On-Ramp & Container Gap

**What's missing:** No AMD equivalent to "docker pull → working robotics prototype in 30 seconds."

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| Jetson Thor dev kit ($3,499, available NOW) | Kria AI dev platform (Q4 2026) | **Absent** |
| Isaac Sim container (docker pull) | AMD robotics simulation container | **Absent** |
| GR00T inference container | AMD VLA inference container | **Absent** |
| Open humanoid reference design (Unitree H2 Plus) | AMD humanoid reference | **Absent** |
| RTX Spark (AI PC prototype → production path) | AMD AI PC robotics template | **Absent** |

**Who's affected:** All developers starting a new robotics project — NVIDIA is the path of least resistance.

**Opportunity signal:** AMD's FPGA integration (125 µs deterministic control loop) is a genuine technical differentiator. The play: make FPGA power transparent through a high-level SDK layer so developers never touch it directly.

---

### Gap 5 — ROS 2 GPU Acceleration Stack

**What's missing:** No ROCm GPU-accelerated ROS 2 middleware — the layer where NVIDIA has Isaac ROS, cuVSLAM, nvblox.

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| Isaac ROS (CUDA-accelerated ROS 2 packages) | ROCm-accelerated ROS 2 packages | **Absent** |
| cuVSLAM (GPU visual SLAM) | ROCm SLAM | **Absent** |
| nvblox (3D GPU mapping) | ROCm 3D mapping | **Absent** |
| Qualcomm QIRP SDK (Hexagon NPU SLAM) | AMD robotics SDK | **Absent** |

**Evidence:** AMD published a single blog post on Ryzen AI CVML Library with a ROS 2 node for depth estimation. That is far short of a full GPU-accelerated middleware stack. ROS 1 reached end-of-life May 31, 2025 — the migration to ROS 2 is complete across the industry. AMD needs to be native-first in ROS 2, not a blog post.

---

### Gap 6 — Partner & ISV Ecosystem

**What's missing:** AMD's 30-partner nascent network vs. NVIDIA's 110 robot brain developers and 7,000+ Jetson companies — a 7-year ecosystem depth gap.

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| ABB, FANUC, KUKA, UR certified | None certified | **Absent** |
| Figure AI (BMW 30K vehicles/yr) | No humanoid OEM anchor | **Absent** |
| Agility Robotics (100K+ totes, GXO) | No AMR anchor | **Absent** |
| Amazon Robotics 1M+ units | No warehouse AMR anchor | **Absent** |
| SI certification programs (TCS, Infosys) | No SI program | **Absent** |
| Caterpillar (construction + bulldozer) | No industrial anchor | **Absent** |

**Why it's still open:** Robot OEMs design hardware around Jetson — changing mid-product requires full re-validation. 7+ years of SDK depth means NVIDIA is the path of least resistance at the design decision point.

---

### Gap 7 — Safety Certification Path

**What's missing:** No certified AMD robotics deployment path for regulated industries.

**Evidence:**
- No ISO standard exists yet for dynamically balancing legged robots (years from finalization)
- Liability unresolved: "If a humanoid robot injures a worker — who is liable?"
- NVIDIA certified OEMs: Siemens, KUKA, ADLINK, Caterpillar — each required Jetson-specific validation
- AMD: no safety-certified robotics hardware partnership announced
- IEC 61508 (functional safety) / ISO 26262 (automotive) / ISO 10218 (fixed robots) — no AMD path
- Industrial clients expect **99.99% uptime**; production line downtime = $10K+/minute

**Opportunity signal:** Kria AI's FPGA + Xen hypervisor RT isolation is technically well-suited for safety-critical workloads. A path to IEC 61508 certification through this architecture is credible — if funded.

---

### Gap 8 — Real-World Data & Teleoperation Infrastructure

**What's missing:** AMD has zero presence in the data supply chain — the most strategic bottleneck in Physical AI.

**Evidence:**
- Teleoperation = gold standard: costs ~**$100/hr** · yields **<200 demos/worker/day** · hardware rigs cost $50K–$150K each
- Robot training data at ~**0.1–1% of LLM training data volume** — field needs 100–1,000× more
- **8 synthetic samples = 1 real teleoperated sample** for in-domain manipulation
- NVIDIA: Physical AI Data Factory (780K trajectories/11hrs) + Physical AI Open Datasets (4.8M HuggingFace downloads)
- AMD: **zero teleoperation tooling**, zero synthetic data pipeline, zero datasets on HuggingFace
- "Teleoperation facilities = semiconductor fab equivalent" — whoever builds trusted data pipelines holds leverage comparable to TSMC

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| Physical AI Data Factory (Cosmos-powered) | AMD synthetic data pipeline | **Absent** |
| Physical AI Open Datasets (HuggingFace) | AMD robotics datasets | **Absent** |
| GR00T-Dreams (zero-teleoperation data gen) | — | **Absent** |
| Isaac Teleop (in LeRobot) | AMD teleoperation framework | **Absent** |

---

## Trends Enabling New Solutions

**1. Sim-to-Real Closing Slowly**
Contact dynamics still not accurately simulated in any tool. Visual realism gap causes policies trained on renders to fail on real cameras. The ratio varies: locomotion may need 10–20% real data; dexterous manipulation needs 60–80% real data even with strong simulation pretraining. Isaac Sim 5.0 open-sourcing (2025) creates an opportunity for AMD to contribute GPU acceleration.

**2. VLA Models Scaling Fast**
164 VLA submissions at ICLR 2026. Architecture bifurcating into single-model (RT-2, OpenVLA, π0) and dual-system (Helix, GR00T N1) designs. Key research gaps: negative transfer from heterogeneous datasets; benchmark fragility (LIBERO: 95% → <30% under perturbation); memorization vs. generalization. Data infrastructure now described as "a first-class research problem" — same conclusion from 1,228 papers.

**3. ROS 1 Dead, ROS 2 Standard**
ROS 1 reached end-of-life May 31, 2025. ROS 2 Humble (LTS, May 2027) and Jazzy are the standard. Every simulator now prioritizes ROS 2 integration. Window for AMD to enter as a first-class ROS 2 GPU-acceleration contributor is now.

**4. LeRobot as the Developer Gateway**
LeRobot has become the open-source hub for robot learning — 15M downloads, ICLR 2026 presentation, v0.6.0 shipping GR00T + world models + reward APIs + simulation benchmarks. NVIDIA is deeply embedded. This is the "Pipecat plugin" equivalent for Physical AI. Being absent from LeRobot means being invisible to 16M HuggingFace developers.

**5. Open Hardware Reference Designs**
NVIDIA's open humanoid reference design (Unitree H2 Plus + GR00T + Jetson Thor, late 2026) is the Physical AI equivalent of an AMD AI Blueprint. It sets the default architecture that academic labs and startups design around. AMD needs a comparable open reference design.

**6. AMD's FPGA Advantage (Real, If Surfaced)**
The Kria AI's deterministic 125 µs control loop (8,000 decisions/sec) + simultaneous VLA inference is technically superior to Jetson for real-time robotics. FPGA learning curve is the barrier — the play is abstracting it behind a high-level SDK.

---

## Risks & Constraints

| Risk | Detail |
|---|---|
| AMD benchmark credibility | All claims vs Jetson T5000 are AMD-commissioned (Open Navigation LLC) — no independent validation |
| Kria platform availability | GA Q4 2026; developers prototype on what's available *now* → Jetson Thor ($3,499) |
| FPGA learning curve | Spartan UltraScale+ requires specialist knowledge — high barrier for robotics software developers |
| ROCm library gaps | bitsandbytes quantization unreliable; fine-tuning unstable on RDNA; Windows ROCm second-class |
| Data moat depth | NVIDIA's synthetic data factory is 11-hours-for-780K-trajectories. AMD has no equivalent at any scale |
| Safety certification timelines | IEC 61508 certification for new hardware takes 18–24 months minimum |
| Partner ecosystem depth | AMD has 30 partners vs NVIDIA's 7,000+ companies — Jetson OEMs are locked in by design history |
| VLA training lock-in | Zero ROCm mentions in 1,228 VLA papers — a community norm, not a technical barrier |
| Humanoid battery | 90 min (Agility), 2–3 hrs (Figure) — the hardware bottleneck AMD cannot address |
| Dexterity + autonomy gap | Hardware is ahead of software across all platforms — a universal constraint |

---

## Sources

[1] [Physical AI Market — MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/physical-ai-market-240269196.html)
[2] [Physical AI Market — Astute Analytica](https://www.astuteanalytica.com/industry-report/physical-ai-market)
[3] [Embodied AI Market — Research and Markets](https://www.researchandmarkets.com/reports/6226237/embodied-ai-market-report)
[4] [NVIDIA Isaac Developer Platform](https://developer.nvidia.com/isaac)
[5] [Isaac GR00T — NVIDIA Developer](https://developer.nvidia.com/isaac/gr00t)
[6] [Jetson Thor — NVIDIA](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
[7] [Introducing Jetson Thor — NVIDIA Technical Blog](https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/)
[8] [NVIDIA wants to be the Android of generalist robotics — TechCrunch](https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/)
[9] [NVIDIA and Global Robotics Leaders — NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world)
[10] [AMD Advancing AI 2026 — AMD Newsroom](https://newsroom.amd.com/press-kits/advancing-ai-2026-all-news/)
[11] [AMD Ryzen AI Embedded X100 — AMD Newsroom](https://newsroom.amd.com/news/aai-2026-ryzen-ai-embedded-x100/)
[12] [AMD Kria AI Robotics Developer Platform — AMD Newsroom](https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/)
[13] [AMD Robotics Partner Network — AMD Newsroom](https://newsroom.amd.com/news/aai-2026-robotics-partner-network/)
[14] [AMD Physical AI Plans Come Into Focus — ServeTheHome](https://www.servethehome.com/amds-physical-ai-plans-come-into-focus-as-company-launches-ryzen-embedded-ai-x100/)
[15] [Jetson vs Kria vs Rockchip vs Intel 2026 — Promwad](https://promwad.com/news/edge-ai-platforms-2026-jetson-kria-rockchip-movidius)
[16] [AMD Kria AI Solutions](https://www.amd.com/en/products/system-on-modules/kria/ai.html)
[17] [LeRobot GitHub — Hugging Face](https://github.com/huggingface/lerobot)
[18] [LeRobot v0.4.0 — HuggingFace Blog](https://huggingface.co/blog/lerobot-release-v040)
[19] [LeRobot v0.6.0 — HuggingFace Blog](https://huggingface.co/blog/lerobot-release-v060)
[20] [π0 and π0-FAST — HuggingFace Blog](https://huggingface.co/blog/pi0)
[21] [OpenVLA GitHub](https://github.com/openvla/openvla)
[22] [NVIDIA + HuggingFace bring GR00T to LeRobot — NVIDIA Blog](https://blogs.nvidia.com/blog/hugging-face-lerobot-models-frameworks-open-robotics/)
[23] [GR00T Policy in LeRobot — HuggingFace Docs](https://huggingface.co/docs/lerobot/groot)
[24] [NVIDIA Open Humanoid Robot Reference Design — NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design)
[25] [ROCm Becomes First-Class in vLLM — ROCm Blogs](https://rocm.blogs.amd.com/software-tools-optimization/vllm-omni/README.html)
[26] [AMD vLLM Development Roadmap Q3 2026 — GitHub](https://github.com/vllm-project/vllm/issues/44091)
[27] [AMD ROCm in 2026 — CraftRigs](https://craftrigs.com/articles/amd-rocm-local-llm-2026/)
[28] [Physical AI Data Wall — Eventual.ai](https://www.eventual.ai/blog/the-data-wall-in-physical-ai)
[29] [Robotics Data Gap — ISF Voices 2026](https://scsp222.substack.com/p/isf-voices-2026-the-robotics-data)
[30] [Physical AI Training Data Guide 2026 — DataX Power](https://www.dataxpower.com/blog/physical-ai-training-data)
[31] [VLA Training Data Problem — Label Studio](https://labelstud.io/blog/vla-robot-data-problem/)
[32] [VLA Survey 2026](https://vla-survey.github.io/)
[33] [State of VLA Research at ICLR 2026 — Moritz Reuss](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
[34] [Humanoid Robots State of Industry 2026 — CTCO](https://www.ctco.blog/posts/humanoid-robots-state-of-the-art-2026/)
[35] [Top 8 Humanoid Robot Companies 2026 — EVST](https://www.evsint.com/top-8-humanoid-robot-companies-2026/)
[36] [Humanoid Robotics Challenges 2026 — RoboZaps](https://blog.robozaps.com/b/challenges-in-humanoid-robotics)
[37] [Physical AI Infrastructure Platforms 2026 — The Robot Report](https://www.therobotreport.com/5-physical-ai-infrastructure-platforms-shaping-robotics-in-2026/)
[38] [Best Robot Simulators for ROS 2 2026 — Drift](https://www.godrift.ai/blogs/best-robot-simulators-ros2)
[39] [Robot Simulation Software 2026 — Black Coffee Robotics](https://www.blackcoffeerobotics.com/blog/which-robot-simulation-software-to-use)
[40] [Edge Computing in Robotics Survey — arXiv](https://arxiv.org/html/2507.00523v1)
[41] [From Centralized Brains to Edge Intelligence — RoboticsTomorrow](https://www.roboticstomorrow.com/story/2025/09/from-centralized-brains-to-edge-intelligence-rethinking-compute-architectures-for-autonomous-mobile-robots/25497/)
[42] [NVIDIA and Qualcomm Robotics Platform Comparison — Constellation Research](https://www.constellationr.com/blog-news/insights/nvidia-highlights-its-robotics-momentum-qualcomm-makes-its-platform-case)
[43] [Agricultural AI Robotics — Farmonaut](https://farmonaut.com/precision-farming/ag-robotics-ai-robotics-in-agriculture-2025-trends)
[44] [Ag Robotics Systematic Review 2015–2025 — MDPI Crops](https://doi.org/10.3390/crops5050075)
