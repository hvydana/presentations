# AMD Opportunity Gap Register — Robotics & Physical AI
*Last updated: 2026-09-06 (RESUMED — Iteration 5: 2 new seed reports ingested + 5 additional research agents dispatched; 26 confirmed gaps total across 5 iterations)*

---

## Iteration 5 Update (2026-09-06)

Two previously-unread seed reports were ingested (`l1-l2-hardware-simtoreal-amd-gap-analysis.md`, `physical-ai-robotics-inference-pipeline-commercial-layers-market-analysis.md`), both already written in the technological-stack-layer framing the user asked for. Their named gaps are extracted below as **GAP-14 through GAP-27** (14 new entries). Five additional research agents were dispatched to fill evidentiary gaps and check staleness against the original 13 gaps (dated 2026-08-13, now 3+ weeks old):

- **Motion-planning/sim status** → found `rocRobo` (embryonic ROCm cuRobo analog) and two AMD-authored PRs (#1770, #1865) upstreaming HIP/ROCm groundwork into NVIDIA's own `nvidia/warp` repo. **This upgrades GAP-1's status** from "no community effort" to "early-stage upstream-in-progress" — AMD is already acting, not merely eligible to act.
- **AMD announcements status-check** → confirmed all 5 prior top-ranked actions remain unactioned as of Sept 2026; surfaced GitHub issue `lerobot#4205`, filed during AMD's own "AI DevMaster Hackathon" (Jul 10–Aug 6 2026), explicitly requesting a ROCm CI matrix for LeRobot — independent community confirmation that GAP-10 (MLC-LLM CI) is AMD's most shovel-ready action. Also: Digital Twin Consortium joined the AMD Robotics Partner Network.
- **Inference observability** → confirmed zero RocProfiler/ROCm integration exists in any robotics observability platform (Foxglove, Formant, InOrbit, Cogniteam) or in `ros-opentelemetry` (ROSCon 2025) — the closest extensible building block for GAP-25.
- **Robot MLOps whitespace** → independently confirmed no integrated, hardware-agnostic VLA policy-lifecycle platform exists for any vendor; Ketryx (safety QMS) is the closest counter-candidate but is pre-deployment/documentation-only — reinforces GAP-27 as the single highest-conviction whitespace in the entire register.
- **Safety certification path** → found AMD is not starting from zero: TÜV SÜD-certified Versal/Zynq design-flow (IEC 61508+ISO 26262) already exists (FPGA fabric only, not AI-inference tiles), plus active QNX and Green Hills RTOS partnerships — the fastest path for GAP-19 is extending these, not a new certification program.

---

## Synthesis — Top AMD Opportunities (FINALIZED — Iteration 4)

**Thirteen confirmed GAP-AMD nodes across four iterations.** Iteration 4's central finding: the NVIDIA edge inference SDK lock-in is a three-tier system — (1) **proprietary hard walls** (Isaac ROS+NITROS/GXF, TensorRT Plugin API, cuVSLAM — no open path for any AMD equivalent), (2) **open-source with AMD gap** (MLC-LLM, vla.cpp, Kenning — solvable with one CI contribution each), and (3) **AMD already building** (NITROS equivalent — announce-ready at Isaac ROS 4.0 parity on Jetson Thor).

**Critical strategic asset surfaced (Iteration 4):** AMD is internally building a ROCm-native NITROS equivalent that is feature-comparable to Isaac ROS 4.0 on Jetson Thor (unreleased). This converts the largest confirmed NVIDIA lock-in — GXF/NITROS gating 2M+ devs and 7,000+ Jetson Orin commercial customers — from an unserved gap into an AMD strategic asset awaiting announcement. Timing and framing of this announcement is AMD's single highest-priority GTM decision in robotics infrastructure.

**Ranked top AMD actions (FINALIZED — Iterations 1–4):**

1. **Announce AMD's internal NITROS-equivalent at Isaac ROS 4.0 feature parity** — announce before or concurrent with Jetson Thor GA; choose open-source (community default) vs. AMD proprietary (faster ship); this repositions AMD from hardware vendor to ROS 2 GPU transport author [N75/N80]
2. **Contribute AMD gfx942/gfx1100 CI pipeline to MLC-LLM upstream for LeRobot VLA models** — one GitHub Actions workflow compiling ACT/SmolVLA/Pi0 on AMD targets + publishing pre-compiled `.so` to `mlc.ai/wheels` = community self-porting flywheel (direct vLLM CI playbook) [N76]
3. **Approach Google DeepMind at researcher level to co-develop differentiable MJWarp-on-ROCm** — MJWarp is not differentiable on ANY backend (CUDA or ROCm); AMD's JAX/XLA on ROCm is the co-architect path; earn joint authorship credit + LF Newton governance seat [N60]
4. **Publish "Eno on AMD" inference guide with Genesis engineers before end-2026 commercial launch** — Genesis is choosing inference silicon NOW; no NVIDIA-Genesis Eno relationship exists; guide = AMD silicon in the Eno BOM at the most visible humanoid launch of 2026 [N61]
5. **Publish VLA inference Hz benchmark for ACT/SmolVLA on Ryzen AI MAX+ 395 via FastFlowLM 1.0** — zero AMD Hz data is the primary commercial adoption blocker; AMD MI300X HBM3 26× bandwidth advantage over Jetson AGX LPDDR5 for the memory-bound action expert stage is unmeasured and likely favorable [N79]
6. **Assemble `amd-robotics-inference` meta-SDK** = vla.cpp ROCm EP + Kenning VLA backend + `tvm_vendor` AMD auto-select, packaged on ROCm.ai — AMD is one contribution to each from building the first vendor-neutral TensorRT alternative for non-NVIDIA robotics edge [N78]
7. **Commit AMD as Linux Foundation Newton member and announce ROCm Warp backend contribution** — unlocks entire GPU simulation tier; affects Boston Dynamics, Agility, Figure AI, Toyota Research, Skild, Samsung (all Newton 1.0 adopters) [N42]
8. **Enroll Genesis AI in AMD Robotics Partner Network + co-author Genesis ROCm Reference Architecture** — formalize the existing technical relationship (ROCm tutorial + Real2Sim2Real arXiv) before NVIDIA claims Genesis during $500M fundraise [N44]
9. **Submit Ryzen AI X100 to Beckhoff TwinCAT 3 ML hardware validation at Q4 2026 GA** — AMD has CPU wins (CX20x3, K4131-Px) in TwinCAT; GPU/NPU certification is the $6.1B Windows IPC market next rung [N46]
10. **Co-announce AMD MI300X as a supported GPU config in ModulEdge fleet edge data center units** — Comino already supports MI300X; ModulEdge blog already lists AMD GPU servers; gap is one BD action, not an engineering certification process [N48/N62]

**Single highest-leverage next action:** Announce the internal NITROS-equivalent (action #1) simultaneously with the MLC-LLM CI contribution (action #2). The NITROS announcement repositions AMD from "NVIDIA tool runner" to "ROS 2 GPU transport co-author" at the highest developer layer; the MLC-LLM CI contribution makes every LeRobot model automatically AMD-deployable via `pip install`. Together they establish AMD as the open multi-hardware default for robotics inference — across both the GPU transport layer (Isaac ROS–equivalent) and the model inference layer (MLC-LLM) — without NVIDIA's permission.

---

## Full GAP-AMD Entries (13 confirmed, evidence-backed)

---

### GAP-1 (N42) — No Warp ROCm Backend; Linux Foundation Path Available
**Rank: 1** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H
**STATUS UPDATE (2026-09-06, N100/N105 Pivot):** Upgraded from "no community effort" to "early-stage upstream-in-progress." A motion-planning/sim research agent found `rocRobo` — an embryonic ROCm analog to cuRobo — already exists, and separately found two **AMD-authored PRs (#1770, #1865) upstreaming HIP/ROCm groundwork directly into NVIDIA's own `nvidia/warp` repository**. AMD engineering is already acting on this gap, not merely eligible to act. The action reframes from "commit to build" to "resource to completion and announce" — the highest-leverage next action is now to prioritize merging #1770/#1865 and pair the announcement with a public rocRobo roadmap (see GAP-14).

**What's missing:** No entity — NVIDIA, AMD, or Linux Foundation — has committed to a ROCm backend for NVIDIA Warp, despite Warp being the substrate for Newton (Linux Foundation), MuJoCo-Warp, and cuRobo. Every developer using these three stacks on AMD hardware is categorically excluded from the GPU-accelerated simulation tier.

**Why it's open:** The gap is organizational, not technical. No public GitHub issue on NVIDIA/warp requests ROCm support; no community HIP fork has emerged. The port requires translating Warp's JIT compiler CUDA surface (PTX emitter, warp-level primitives, CUDA Graphs) — a bounded, estimable engineering effort. AMD can contribute as a Linux Foundation Newton member without NVIDIA's permission.

**Who's affected:** Newton (5,100 GitHub stars) is adopted by Boston Dynamics, Agility Robotics, Figure AI, Toyota Research Institute, Skild AI, Samsung. cuRobo (1,700 stars, Apache 2.0, v0.8.0 April 2026) is used for motion planning in every Isaac ROS deployment. MuJoCo-Warp is 152–313× faster than MJX on RTX hardware — AMD users are forced onto the slow MJX path or excluded entirely from the robotics RL simulation tier.

**AMD angle:** ROCm + open-source contribution (Linux Foundation membership). A differentiable MJWarp-on-ROCm co-development with Google DeepMind is possible (differentiable MJWarp is not yet done even on CUDA), turning a port into a joint feature contribution.

**Evidence:** NVIDIA/warp: 7,000 GitHub stars, 585 forks. Newton 1.0 GA (GTC March 2026): 252–475× speedup vs. MJX. cuRobo v0.8.0 (April 2026, Apache 2.0): 30ms motion planning, embedded in Isaac ROS cuMotion. NVIDIA claims 2M robotics developers in ecosystem. [N11-agent: sources 1,2,3,4,5,6]

**Confidence: High** — blocked developer population confirmed and quantified; organizational gap is clear; Linux Foundation governance path is available.

**Highest-leverage next action:** Announce AMD's Linux Foundation Newton membership and ROCm Warp backend roadmap. Then engage Google DeepMind on co-developing differentiable MJWarp-on-ROCm as a joint feature (not a port) — earning co-authorship credit.

---

### GAP-2 (N44) — Genesis AI Absent from AMD Robotics Partner Network
**Rank: 2** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** Genesis AI is absent from AMD's Robotics Partner Network despite AMD having already published Genesis-specific ROCm tutorials (Feb 9, 2026) and an arXiv paper (Real2Sim2Real, 2026) demonstrating a full AMD ROCm pipeline combining 3D Gaussian Splatting with Genesis. There is no joint optimization roadmap, no AMD-endorsed support path, and no co-engineering agreement.

**Why it's open:** AMD has not formalized the relationship that technically already exists. The Robotics Partner Network has a no-cost entry tier. Genesis is raising ~$500M at $3B valuation — the window to claim the relationship before NVIDIA does is bounded by the fundraise timeline (expected close by end-2026).

**Who's affected:** Enterprise robotics OEMs evaluating simulation stacks; Genesis AI's planned LG CNS deployment (end-2026); AMD's 30+ Robotics Partner Network members who have no Genesis-compatible sim layer in the network's technology map.

**AMD angle:** Ecosystem — Genesis World 1.0 Quadrants compiler maps AMD hardware waves of 64 natively (architecturally first-class, not a port afterthought); Real2Sim2Real arXiv proves the AMD+Genesis sim-to-real stack works end-to-end. This is AMD's most accessible path to claiming an Isaac Sim alternative.

**Evidence:** AMD ROCm blog (Feb 9, 2026): hands-on Genesis tutorial on Ryzen AI MAX. arXiv 2607.22997 (2026): Real2Sim2Real AMD ROCm pipeline. Genesis at $3B valuation (talks, July 2026). NVIDIA has no confirmed Genesis relationship. HSG/CFIUS creates friction for acquisition but not for partnership. [N29-agent: sources N1,N5,N6,N8,N10]

**Confidence: High** — technical path confirmed; partnership gap confirmed; cost of closing the gap is zero (Network enrollment); NVIDIA absence confirmed.

**Highest-leverage next action:** Enroll Genesis AI in AMD Robotics Partner Network and co-author a "Genesis on ROCm Reference Architecture" guide with Genesis engineers — before Genesis raises its $500M round and NVIDIA makes a competing move.

---

### GAP-3 (N46) — $6.1B Windows Industrial IPC Market: Technical Done, Commercial Gap
**Rank: 3** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** AMD has zero certified design wins in the Windows-based industrial IPC market despite having removed the technical barrier. ROCm 7.2.2 (CES January 2026) shipped as a unified Windows+Linux release with native PyTorch. AMD's Microsoft Build 2026 announcement included a DirectX Compute Graph Compiler (DxCGC) and ONNX Runtime GPU EP plugin interface. DirectML on AMD GPUs delivers 4.7× over CPU and closes ~95% of the performance gap to TensorRT/OpenVINO. The market ($6.1B in 2025, growing to $8.9B by 2030) is the compute layer for industrial robot edge nodes (Beckhoff TwinCAT, Siemens SIMATIC Industrial Edge, Rockwell Studio 5000).

**Why it's open:** AMD's ROCm 7.2.2 news (CES 2026) may not have reached industrial IPC procurement teams. Bosch Rexroth ctrlX explicitly lists NVIDIA 2000A GPU in its AI-enabled controller — AMD has never been in a competing BOM position. The gap is now commercial certification: AMD needs to be listed in validated hardware configurations for 2–3 major IPC vendors.

**Who's affected:** Any industrial robot deployment using Beckhoff (TwinCAT CoAgent physical AI), Siemens (SIMATIC AI Inference Server), Rockwell (Studio 5000 AI), Advantech, Kontron, or ADLINK Windows-based edge servers.

**AMD angle:** Silicon — Ryzen AI Embedded X100 (Q4 2026 GA) targets exactly this market; ROCm 7.2.2 + DirectML is the software path. The Robotics Partner Network includes Arbor and Sapphire (AMD-ecosystem IPC builders) as existing channels.

**Evidence:** $6.1B industrial IPC market (Business Research Company 2025). Beckhoff TwinCAT 3 ML (Windows 10/11, ONNX-native). Siemens SIMATIC AI Inference Server (Windows-compatible). Bosch Rexroth ctrlX with NVIDIA 2000A (explicit competitor design win). AMD ROCm 7.2.2 (CES 2026): unified Windows+Linux. AMD Build 2026: DxCGC + ONNX Runtime GPU EP. DirectML 4.7× over CPU, ~95% of TensorRT gap closed. [N38-agent: sources 1,2,4,5,6,7,8]

**Confidence: High** — market sizing confirmed; technical readiness confirmed; AMD's commercial absence confirmed.

**Highest-leverage next action:** Launch AMD industrial IPC certification program. Engage Beckhoff (TwinCAT CoAgent uses MCP/AI; directly relevant) and Advantech (AMD ecosystem partner channel) for Ryzen AI X100 + Windows ML validation within Q4 2026 GA window.

---

### GAP-4 (N48) — Robot Fleet Edge Data Center: First-Mover in Uncontested Category
**Rank: 4** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H ← *upgraded from M after N62 Pivot*

**What's missing:** A productized "robot fleet edge data center" that bundles AMD GPU compute (MI300X/MI325X), ROCm-native inference runtime, OTA model update orchestration (ATC Deploy-class), fleet inference health telemetry, and local data landing for 4–7 TB/hour perception-action streams — co-branded as an AMD+ModulEdge offering.

**Why it's open:** SVRC 2025 explicitly calls fleet deployment infrastructure "the most under-built layer in the 2025 physical AI stack — barely exists as a product today." NVIDIA's 2026 fleet products (Mega, Halos, Fleet Command) address simulation and safety, not physical edge data center for local-first fleet operations. **N62 Pivot (Iter 3):** Comino GPU modules already list AMD MI300X as a supported configuration, and the ModulEdge blog already mentions "AMD GPU servers" as a supported deployment option. The gap is NOT a technical OEM certification process — it is a GTM gap: AMD has never co-announced or co-marketed the existing compatibility.

**Who's affected:** Every enterprise running 50+ heterogeneous robots where cloud streaming is cost-prohibitive: warehouse operators (Amazon, DHL, Ocado), automotive assembly (BMW, Mercedes, Bosch), and hospital logistics. Engineering teams currently burn 6–18 months building this infrastructure custom for each deployment.

**AMD angle:** Compute + ecosystem — MI300X's 192GB HBM3 enables single-GPU serving of 70B-class VLA models for robot swarms (141,521 tok/sec on Llama 2 70B in MLPerf 6.0). Agency Tool Company (YC) ATC Deploy handles OTA delivery 20× faster than Docker pull and already serves Burro (750+ field robots) — a potential AMD partnership for the software layer. **The enclosure + GPU module partnership already exists at the hardware level.**

**Evidence:** Robot OTA Update Platforms: $1.42B (2024) → $5.85B by 2033, 17.2% CAGR. ModulEdge: explicitly GPU-agnostic container. Comino: AMD MI300X listed as supported GPU module configuration. ModulEdge blog: "AMD GPU servers" cited as deployment option. Agency Tool Company (YC): serves Burro, Gather AI, Tempo. AMD MI300X MLPerf 6.0: 141,521 tok/sec Llama 2 70B. NVIDIA fleet products confirmed as non-overlapping. [N39-agent, N53-agent]

**Confidence: High** ← *upgraded from Medium via N62 Pivot. Comino+ModulEdge compatibility confirmed; gap is a single BD/GTM action.*

**Highest-leverage next action:** Co-announce AMD MI300X as a first-class supported GPU configuration in ModulEdge fleet edge data center units — a joint press release or technical brief positioning AMD alongside NVIDIA B200 in ModulEdge's lineup. This is a 1-week business development action, not a 6-month engineering certification.

---

### GAP-5 (N22) — LeRobot Model Hub Callsite Invisibility
**Rank: 5** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** No AMD-contributed or AMD-optimized model card exists in the HuggingFace LeRobot model hub. Developers starting a new robotics project from LeRobot's default workflow land on GR00T N1.7 (NVIDIA) or Pi0 (Physical Intelligence) as the first recommendation — AMD hardware never appears at the callsite.

**Why it's open:** AMD has published blog tutorials (Pi0 fine-tune on MI300X, SmolVLA on ROCm) but has not committed artifacts to the community-facing HuggingFace model registry in the LeRobot namespace. This is an outreach/engineering gap, not a technical barrier.

**Who's affected:** The 16M HuggingFace developers and 3M NVIDIA-defined robotics developers who discover VLA models through `lerobot`. AMD is invisible to all of them at the moment of hardware selection.

**AMD angle:** Ecosystem/tooling — AMD already has confirmed working checkpoints; the action is publishing them with ROCm as the reference backend.

**Evidence:** AMD ROCm blog confirms Pi0.5, Pi0, SmolVLA, ACT all fine-tuned on MI300X; SmolVLA confirmed working (no CUDA-specific kernels); Cosmos3-Nano community-confirmed on AMD ROCm; PyTorch 2.7 lists ROCm 6.3 as first-class; LeRobot Hub now has 58,000+ datasets — the single largest dataset category on HuggingFace. [N9-agent: sources 2,3,4,6]

**Confidence: High** — technical path confirmed; gap is a shipping/outreach decision.

**Highest-leverage next action:** Commit a SmolVLA checkpoint to `lerobot` model hub with ROCm as the reference backend, announce it as "AMD's first native LeRobot model." Measure developer adoption as the vLLM proxy metric.

---

### GAP-6 (N18) — FPGA Real-Time Control Loop Not Callable from ROS 2/Python
**Rank: 6** | AMD fit: H | Ecosystem benefit: H | Openness: M | Evidence strength: H

**What's missing:** No shipping ROS 2 or Python API exposes AMD Kria's FPGA 125 µs deterministic control loop. AMD's announced Robotics Core SDK (Q4 2026) is ROCm/NPU-centric and does NOT include FPGA control loop abstraction.

**Why it's open:** AMD's KRS already includes `colcon_acceleration`, REP 2008 provides the ROS 2 standard for the abstraction layer, and Xen hypervisor + RT isolation are pre-configured. The gap is last-mile packaging: pre-compiled EtherCAT/CAN-FD/TSN bitstreams distributed as a ROS 2 hardware_interface plugin.

**Who's affected:** All robotics software developers evaluating AMD Kria — they see "125 µs control loop" in marketing but cannot access it from Python or ROS 2.

**AMD angle:** Tooling — ROBOTCORE (Acceleration Robotics) on Zynq UltraScale+ already ships this exact pattern (2.5 µs deterministic ROS 2, no HDL required). AMD could license/OEM/fork ROBOTCORE as a first-party FPGA SDK shipped under the Kria brand.

**Evidence:** REP 2008 confirmed as ratified ROS 2 standard; ROBOTCORE confirmed shipping product on Zynq UltraScale+; Qualcomm QIRP SDK 2.2.0 is the hardware-NPU abstraction blueprint; AMD Robotics Core SDK Q4 2026 documentation does not reference FPGA control API. [N14-agent: sources 1,4,5,6,7,9]

**Confidence: High** — gap confirmed; blueprint exists; timeline is Q4 2026 SDK which could be updated.

**Highest-leverage next action:** Add `kria_fpga_hardware_interface` ROS 2 package to AMD Robotics Core SDK. Alternatively, evaluate ROBOTCORE OEM with Acceleration Robotics.

---

### GAP-7 (N27) — No Validated End-to-End AMD Synthetic Data Pipeline
**Rank: 7** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: M

**What's missing:** No validated, end-to-end open-source pipeline orchestrating Genesis World simulation + Cosmos 3 photorealistic augmentation + trajectory export to LeRobot/Open-X format on AMD ROCm hardware.

**Why it's open — updated after N49:** The component stack is confirmed ROCm-compatible, but N49 revealed a new bottleneck: Cosmos Predict2's NATTEN sparse attention (2.6× speedup) is locked to Hopper/Blackwell compute capability 9.0+. MI300X is estimated at 50–80% of H100 per-GPU throughput for the Cosmos augmentation step. However, two paths exist to close this: (1) AMD VSA (Video Sparse Attention, 3.31× kernel speedup on MI308X in MLPerf 6.0) ported to MI300X; (2) Wan2.2 substituted for Cosmos Predict2 (AMD-submitted to MLPerf 6.0; Xiaomi FlashAR+ achieves 82× data generation speedup). The pipeline orchestration gap and NATTEN gap are both software gaps.

**Who's affected:** Every robotics startup and research lab needing to train VLA models without paying NVIDIA cloud rates or building on Isaac Lab.

**AMD angle:** Compute (MI300X 192GB HBM3 advantage at batch 256+) + open-source (all components open; AMD orchestrates, doesn't build from scratch) + alternative world model (Wan2.2 is AMD-native and AMD-validated in MLPerf).

**Evidence:** Genesis Quadrants ROCm-native confirmed; AMD ROCm blog confirms Genesis on MI-series; Cosmos3-Nano-GPTQ-4bit confirmed on AMD Radeon; NATTEN Hopper/Blackwell lock-in confirmed (compute capability 9.0+); AMD VSA 3.31× speedup on MI308X confirmed in MLPerf 6.0; Wan2.2 AMD-submitted to MLPerf 6.0. [N12-agent + N28-agent]

**Confidence: Medium** — components confirmed individually; NATTEN gap is real but closeable; Wan2.2 alternative path exists but trajectory quality vs. Cosmos is unverified.

**Highest-leverage next action:** Publish "Genesis + Wan2.2 on AMD MI300X" pipeline tutorial on ROCm Blogs (avoiding NATTEN blocker by substituting Wan2.2 for Cosmos Predict2). Then evaluate AMD VSA port to MI300X to restore full Cosmos Predict2 compatibility.

---

---

### GAP-8 (N60) — AMD as Co-Architect of Differentiable Newton Physics API
**Rank: 8** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** The MuJoCo-Warp differentiable physics API — the layer that enables gradient-based robot learning on the Newton physics stack — is incomplete on ALL backends including CUDA. No entity has claimed ownership of the ROCm/JAX path. AMD has JAX/XLA working on ROCm (confirmed in training benchmarks), which is the same backend Google DeepMind uses for MJWarp development.

**Why it's open:** Google DeepMind has an open GitHub issue tracking the incomplete MJWarp differentiable API on CUDA. No ROCm path exists or is planned. AMD's existing JAX/XLA-on-ROCm work is the exact technical prerequisite for a co-development contribution. Linux Foundation Newton membership gives AMD governance rights to propose and co-own the differentiable physics API standard.

**Who's affected:** Every robotics lab using gradient-based RL on Newton physics (MJWarp is 152–313× faster than MJX — the absence of differentiability blocks the full value of Newton for learning). Google DeepMind (MJWarp author), Boston Dynamics, Agility, Figure AI, Toyota Research, Skild AI — all Newton adopters.

**AMD angle:** Open-source co-authorship + governance. This is qualitatively distinct from N42 (Warp ROCm backend, which is the GPU simulation runtime). N60 targets the differentiable API layer: AMD contributing the ROCm/JAX differentiable path earns joint authorship credit on the MJWarp paper and co-governance of the standard — reframing AMD from "hardware vendor enabling NVIDIA tools" to "physics software co-author."

**Evidence:** MJWarp differentiable physics confirmed incomplete on all backends (GitHub issue, Google DeepMind, 2026). AMD JAX/XLA on ROCm confirmed working in training benchmarks. Newton 1.0 Apache-2.0 under Linux Foundation. AMD confirmed as non-member of Linux Foundation Newton project (gap is organizational). [N50-agent: sources N2, N3, N6]

**Confidence: High** — differentiability gap confirmed on all backends; AMD's JAX/XLA ROCm path confirmed; organizational path (LF membership) clear.

**Highest-leverage next action:** AMD ML research team initiates researcher-level contact with Google DeepMind MJWarp team to propose co-development of the differentiable Newton physics API on ROCm/JAX — targeting joint authorship of the resulting paper and a LF Newton governance seat.

---

### GAP-9 (N61) — Genesis Eno Robot Silicon Selection: NOW
**Rank: 9** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** A hardware-specific "Eno on AMD" inference and training guide co-published with Genesis AI, naming AMD silicon (Ryzen AI MAX or MI300X) as the reference platform for Genesis's Eno humanoid robot — published before Eno's end-2026 commercial launch.

**Why it's open:** Genesis AI announced the "Eno" robot with LG CNS partnership in June 2026, targeting end-2026 commercial launch. Genesis is selecting inference silicon for Eno's deployment stack right now. No public NVIDIA-Genesis relationship exists for Eno specifically (no joint press release, no product page). AMD already has the technical foundation: ROCm blog tutorial (Feb 2026) + arXiv Real2Sim2Real pipeline + GENE-26.5 foundation model released. The Partner Network enrollment (N44) is a necessary but insufficient commercial signal — a hardware-specific Eno guide creates a named, BOM-level proof point.

**Who's affected:** Genesis AI's commercial deployment partners (LG CNS and future OEM partners); enterprise buyers evaluating Eno for warehouse/logistics (the primary target market); AMD's Ryzen AI MAX and MI300X positioning vs. NVIDIA's edge inference SKUs.

**AMD angle:** Silicon + tooling. Ryzen AI MAX targets the edge inference profile; MI300X targets cloud/server training for Eno behavior models. GENE-26.5 is Genesis's released foundation model — a guide citing GENE-26.5 + Real2Sim2Real + AMD hardware is specific enough to appear in procurement evaluations.

**Evidence:** Genesis Eno + LG CNS partnership (June 2026, Korean press). Genesis Eno end-2026 commercial launch (confirmed). No NVIDIA-Genesis Eno relationship (confirmed absence). AMD ROCm blog Genesis tutorial (Feb 9, 2026). arXiv 2607.22997 Real2Sim2Real AMD ROCm pipeline. GENE-26.5 model released. [N51-agent: sources N1, N3, N6]

**Confidence: High** — silicon selection window confirmed; AMD technical foundation confirmed; NVIDIA absence confirmed; action scope is a 4–6 week co-authorship engagement.

**Highest-leverage next action:** AMD developer relations team reaches out to Genesis engineering team to co-author an "Eno on AMD" inference guide: Ryzen AI MAX + GENE-26.5 + Real2Sim2Real pipeline, published on both AMD ROCm Blog and Genesis developer portal before the end-2026 Eno commercial launch.

---

---

### GAP-10 (N76) — MLC-LLM CI Pipeline: No AMD Artifacts for LeRobot VLA Models
**Rank: 10** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** No CI pipeline in MLC-LLM upstream compiles LeRobot VLA model architectures (ACT, SmolVLA, Pi0, Diffusion Policy) on AMD GPU targets (gfx942/gfx1100) and publishes pre-compiled `.so` artifacts to `mlc.ai/wheels`. As a result, community robotics developers using `pip install mlc-llm-nightly-rocm62` cannot deploy any LeRobot VLA model without manual per-model AMD engineering.

**Why it's open:** MLC-LLM already ships ROCm nightly wheels and auto-detects AMD GPU targets at compile time. Apache TVM v0.25.0.post1 (June 2026) has the ROCm backend active. The gap is a CI/testing gap, not an architectural one. AMD already has a confirmed working end-to-end LeRobot pipeline (WAICA 2026 arXiv, edge-to-cloud blog). The vLLM precedent (37%→93% in 2 months from a single CI pipeline merge) directly validates the scope and impact.

**Who's affected:** The 240+ hackathon developers already using AMD hardware with LeRobot; every future developer who discovers VLA models through LeRobot's policy registry (v0.6.0: ACT/Diffusion Policy/SmolVLA/Pi0).

**AMD angle:** Tooling — one GitHub Actions CI workflow in MLC-LLM upstream. Once merged, every new VLA model added to LeRobot's policy registry automatically becomes AMD-deployable without further AMD involvement.

**Evidence:** MLC-LLM auto-detects `gfx1100`/`gfx942` at compile time; ROCm nightly wheels (`mlc-llm-nightly-rocm62`) ship today; Apache TVM v0.25.0.post1 (June 2026) ROCm backend confirmed active; LeRobot v0.6.0 (July 2026) has growing policy registry; AMD WAICA 2026 paper + edge-to-cloud blog confirm full AMD ROCm pipeline works end-to-end. [N68-agent sources 1,2,3,4,5,6,7]

**Confidence: High** — infrastructure confirmed; gap is a CI workflow, not architecture; vLLM precedent validates the impact.

**Highest-leverage next action:** Contribute a GitHub Actions workflow to MLC-LLM upstream that compiles ACT-25M, SmolVLA-450M, and Pi0 on AMD gfx942/gfx1100 and publishes pre-compiled `.so` artifacts to `mlc.ai/wheels`. This is the vLLM CI merge playbook applied to robotics edge inference.

---

### GAP-11 (N77) — AMD Embedded NPU: No Open LLM Inference Compiler Path to Kria/Versal
**Rank: 11** | AMD fit: H | Ecosystem benefit: H | Openness: M | Evidence strength: H

**What's missing:** No open-source LLM inference compiler (MLC-LLM, vLLM, llama.cpp) has a documented, working path to AMD Kria KV260/KR260 or Versal AIE NPU targets. AMD's only embedded inference path is the proprietary Vitis AI stack — which is CNN-only (no transformer attention ops at LLM scale). The community self-porting flywheel that works at the AMD GPU tier (via MLC-LLM ROCm) does not exist for AMD embedded NPUs.

**Why it's open:** Three separate architectural gaps: (a) MLC-LLM has zero FPGA/embedded NPU backend (GitHub issue #1581, unresolved); (b) Apache TVM's Vitis AI BYOC supports Kria DPU for CNN subgraphs only — no transformer ops; (c) Versal AIE requires MLIR-AIE/llvm-aie/closed-source AMD AIE Compiler — architecturally incompatible with TVM's GPU shader model. AMD's Vitis AI 3.0 strategic pivot to ONNX Runtime VOE deprioritizes the TVM-DPU path. The `Xilinx/mlir-aie` open-source toolchain is a potential bridge (TVM Relax IR → MLIR-AIE dialects) but has not been connected.

**Who's affected:** Robotics teams deploying VLA inference on AMD Kria (KV260, KR260) or Versal AI Core edge boards — the primary AMD embedded edge compute tier.

**AMD angle:** Tooling/silicon. The most accessible near-term path is AMD Ryzen AI NPU (AIE-ML in Phoenix/Strix APUs) via ONNX Runtime VOE — the same path AMD is already developing for Windows IPC certification (N46). If ONNX Runtime VOE reaches LLM-scale ops on Ryzen AI NPU, that architecture may extend to Kria K24/K26 SOM AIE-ML tiles.

**Evidence:** MLC-LLM GitHub issue #1581 (unresolved FPGA support request); Vitis AI 3.5 docs confirm DPU supports only CNN Relay subgraphs; Vitis AI Library removed in v5.0 (2025.1 release); AMD Versal AIE toolchain confirmed incompatible with TVM by architecture (GPU shader vs. micro-coded instruction model); `Xilinx/mlir-aie` repo is open-source and potentially bridgeable. [N69-agent sources 1,2,3,4,5,6,7,8,9,10]

**Confidence: High** (gap confirmed) / Openness: M (Versal AIE compiler is partially closed-source).

**Highest-leverage next action:** Investigate whether AMD Ryzen AI NPU (Strix APU AIE-ML) is accessible via ONNX Runtime VOE for LLM-scale inference — if yes, document the path and extend it to Kria K24/K26 SOM AIE-ML tiles, creating a unified ONNX Runtime embedded inference path for both Windows IPC and robotics edge.

---

### GAP-12 (N78) — No Vendor-Neutral Robotics Inference SDK (TensorRT-Equivalent for Non-NVIDIA)
**Rank: 12** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** No open-source C++ robotics inference SDK combines all five production requirements: (a) ROS 2 native integration, (b) INT4/INT8 model quantization, (c) hardware-agnostic multi-silicon execution (AMD/Intel/Qualcomm/ARM), (d) VLA/diffusion policy model support, and (e) deterministic sub-10ms latency. TensorRT is the de facto standard for NVIDIA; no comparable open alternative exists.

**Why it's open:** The ROS 2 integration and VLA model support communities are advancing on entirely separate tracks: Kenning covers ROS 2 + multi-hardware + INT8 but has no VLA/diffusion support; vla.cpp (June 2026 arXiv) covers VLA/diffusion + cross-hardware C++ + GGUF quantization but has no ROS 2 integration and runs at ~150ms latency. Every near-miss project is missing at least two of the five criteria. Sub-10ms deterministic latency requires PREEMPT_RT + static core affinity — no open SDK packages all of this.

**Who's affected:** Every robotics deployment team evaluating non-NVIDIA hardware (AMD, Intel, Qualcomm, ARM) for production edge inference — they must build 5–7 inference artifacts per model (multi-format deployment chaos from the edge-inference seed report).

**AMD angle:** AMD is uniquely positioned to assemble this because it already has each building block: Ryzen AI CVML Library + ROS 2 node (ROSCon 2025, open-source GitHub), Autoware Foundation `tvm_vendor` (TVM ROS 2 wrapper with AMD target support), vla.cpp (needs only a ROCm EP), and Kenning (needs only a VLA model backend). No other silicon vendor has both the incentive and the existing components to assemble this stack.

**Evidence:** vla.cpp (arXiv 2606.08094, June 2026): serves pi0/pi0.5/GR00T N1.7/Cosmos3/MiniCPM across three hardware tiers; no ROS 2 integration; ~150ms latency. Kenning (Antmicro): ROS 2 native via CVNode, INT8, ARM/Qualcomm/Jetson/Movidius — no VLA support. LiteVLA-Edge (arXiv 2603.03380): ROS 2 + INT4 + VLA at 150ms — CUDA-only. AMD Ryzen AI CVML + ROS 2 node: open-source, ROSCon 2025 — perception only, no VLA. Autoware `tvm_vendor`: ROS 2 TVM wrapper — no VLA zoo. [N36-agent sources 1,2,3,4,5,6,7,8,9]

**Confidence: High** — gap is structural and confirmed; AMD's building blocks are individually verified; no other player is assembling them.

**Highest-leverage next action:** Contribute AMD ROCm EP to vla.cpp (one PR) + co-develop Kenning VLA model backend with Antmicro + package as `amd-robotics-inference` meta-SDK on ROCm.ai, with Autoware `tvm_vendor` as the hardware-agnostic compiler layer.

---

### GAP-13 (N79) — VLA Inference Hz Benchmark Gap: AMD vs. NVIDIA Unquantified
**Rank: 13** | AMD fit: H | Ecosystem benefit: H | Openness: H | Evidence strength: H

**What's missing:** No peer-reviewed or community-published Hz benchmark exists for visuomotor policy inference (ACT, Diffusion Policy, Pi0, SmolVLA) on any AMD hardware — GPU, APU, or FPGA. AMD's only published number is an internal, unverified claim of "~92ms" (~10 Hz) on Ryzen AI MAX+ 395. Commercial robotics teams evaluating AMD for production manipulation cannot make procurement decisions without this data.

**Why it's open:** AMD has shipped working VLA software stacks (FastFlowLM 1.0 + SmolVLA on XDNA2 NPUs; Real2Sim2Real arXiv 2607.22997 on RDNA4; edge-to-cloud blog with Pi0/SmolVLA on MI300X) but has published only training throughput and power numbers, never inference Hz. This is a benchmark publishing gap, not a software gap.

**AMD angle:** Structural hardware advantage likely untapped. The XPU VLA characterization paper (arXiv 2604.24447) establishes that the action expert stage is memory-bound (54 FLOPs/Byte) — the most latency-critical component for 50 Hz manipulation. AMD MI300X's 5.3 TB/s HBM3 vs. Jetson AGX Orin's 204 GB/s LPDDR5 is a 26× theoretical bandwidth ratio. At the APU level, FastFlowLM 1.0 on Ryzen AI MAX+ 395 XDNA2 NPU targets exactly this memory-bound stage at <2W. The VOTE-MLP4 architecture achieves 55.57 Hz on Jetson AGX Orin — AMD has no published response number.

**Who's affected:** Every commercial robotics team evaluating AMD Ryzen AI MAX+ 395 or MI300X for production robot manipulation — 50 Hz is the industry minimum for collaborative-cell manipulation.

**Evidence:** VLA-Perf (arXiv 2602.18397): Pi0 on H100=61.7–314 Hz; RTX 4090=32.2 Hz; no AMD results. VOTE (arXiv 2509.11480): VOTE-MLP4 on Jetson AGX Orin MAX mode=55.57 Hz — only published sub-50ms edge VLA. AMD Advancing AI 2026: Ryzen AI MAX+ 395 VLA reasoning claim "~92ms/~10 Hz" — internal, unpublished. FastFlowLM 1.0 (hwbusters.com): XDNA2 SmolVLA support confirmed; 20–80 tok/s on LLMs; no Hz. XPU VLA characterization (arXiv 2604.24447): action expert 54 FLOPs/Byte (memory-bound), VLM backbone 542 FLOPs/Byte (compute-bound). [N37-agent sources 1,4,5,7,10]

**Confidence: High** — benchmark absence confirmed; AMD hardware and software confirmed working; AMD structural advantage for memory-bound stage is theoretically clear but empirically unmeasured.

**Highest-leverage next action:** Run and publish ACT-25M + SmolVLA-450M Hz benchmarks on Ryzen AI MAX+ 395 using FastFlowLM 1.0 vs. PyTorch+ROCm. Publish as a ROCm Blog post with the XDNA2 NPU vs. RDNA3.5 iGPU comparison on the action expert stage. This is a one-engineer, one-week effort that changes AMD's commercial robotics narrative.

---

## New GAP-AMD Entries (14 additional, from Iteration 5 — resumed 2026-09-06)

*Extracted from the 2 newly-ingested seed reports plus 5 new research agents. Organized under the same evidence-backed format as GAP-1–13; ranks continue the existing sequence (relative ordering approximate — see updated Ranking Methodology table below for scores).*

---

### GAP-14 (N86) — No AMD Path into GPU-Accelerated Motion Planning (cuRobo)
**Fit: H** | **Ecosystem: H** | **Openness: H** | **Evidence: H**

**What's missing:** cuRobo (NVIDIA, Apache-2.0, embedded in Isaac ROS cuMotion, 30ms motion planning) has no ROCm/AMD equivalent. Distinct from GAP-1 (Warp = simulation substrate) — cuRobo is the motion-planning application layer built on top of it.

**AMD angle:** The motion-planning agent found `rocRobo`, an embryonic ROCm analog, already exists — this is an early inflection point, not a from-scratch build.

**Evidence:** rocRobo project confirmed to exist (early-stage); AMD PRs #1770/#1865 upstreaming HIP/ROCm into `nvidia/warp` confirm active AMD engineering investment in the adjacent substrate. [motion-planning agent]

**Confidence: High** — gap confirmed; early AMD activity confirmed.

**Highest-leverage next action:** Identify rocRobo's maintainers/roadmap and evaluate whether AMD should sponsor/upstream it as the official cuRobo-equivalent, timed with the Warp PR merges (GAP-1).

---

### GAP-15 (N87) — No AMD Equivalent to Isaac Sim as an Integrated Platform
**Fit: M** | **Ecosystem: H** | **Openness: M** | **Evidence: M**

**What's missing:** Isaac Sim bundles authoring UI + PhysX physics + RTX photoreal rendering + Omniverse into one integrated platform. Genesis AI (GAP-2/N44) and Warp/Newton (GAP-1/N42) each cover a slice, but no AMD-aligned project bundles all three the way Isaac Sim does.

**AMD angle:** Platform-completeness gap, not a single-component port — likely closed via ecosystem assembly (Genesis + an open rendering layer) rather than one engineering effort.

**Confidence: Medium** — gap is real but the fix is compound/multi-party, not a single bounded action.

**Highest-leverage next action:** Scope whether Genesis + an open rendering stack (Blender Cycles or equivalent) could be positioned as "Isaac Sim equivalent" within 12 months, as a follow-on to the Genesis Partner Network enrollment (GAP-2).

---

### GAP-16 (N88) — ONNX Runtime ROCm EP Deprecated; AMD Inference Path Fragmented
**Fit: H** | **Ecosystem: H** | **Openness: H** | **Evidence: H**

**What's missing:** ONNX Runtime's ROCm Execution Provider was deprecated, fragmenting AMD's inference path across MIGraphX EP, DirectML, and Vitis AI VOE with no single recommended default. This is a regression — something that existed and was removed — a different remediation shape than "never built" gaps.

**Who's affected:** Directly complicates GAP-12/N78's vendor-neutral SDK effort, since several of its building blocks assume a stable ONNX RT ROCm path.

**Confidence: High** — deprecation and fragmentation confirmed in the seed report.

**Highest-leverage next action:** Publish a clear AMD-recommended inference-path decision tree (MIGraphX EP vs. DirectML vs. Vitis AI VOE by use case) to stop the fragmentation from compounding across dependent efforts like GAP-12.

---

### GAP-17 (N89) — AMD Edge Hardware (X100/Kria) Ships with No Validated Robotics SDK Stack
**Fit: H** | **Ecosystem: H** | **Openness: M** | **Evidence: H**

**What's missing:** AMD's Ryzen AI Embedded X100 and Kria launched (July 2026) into a market where the SDK layer is "nearly empty" — no validated, benchmarked, third-party-confirmed robotics software stack ships with the silicon at launch, unlike Jetson's day-one Isaac ROS/JetPack maturity.

**Note:** This is the umbrella gap that GAP-6/N18 (FPGA control API), GAP-11/N77 (embedded NPU inference compiler), and GAP-19/N91 (safety cert) are specific instances of — kept as a separate top-level entry because it's the framing a hardware buyer encounters first.

**Confidence: High** — launch-timing gap directly confirmed.

**Highest-leverage next action:** Prioritize which single SDK component (FPGA control API vs. embedded NPU inference vs. safety cert) most changes buyer perception at launch, and ship that first as a flagship reference.

---

### GAP-18 (N90) — No AMD GPU Benchmark Visibility in Sim-to-Real Literature (MJX/Warp Docs)
**Fit: M** | **Ecosystem: M** | **Openness: H** | **Evidence: M**

**What's missing:** MJX and Warp documentation, benchmarks, and community sim-to-real writeups cite only NVIDIA GPU numbers — AMD hardware is invisible in the literature even where it would technically run. Compounds GAP-13/N79's VLA-inference benchmark gap with an equivalent gap at the simulation-throughput layer (different audience: sim/RL researchers choosing training hardware, vs. commercial teams choosing inference hardware).

**Confidence: Medium** — absence confirmed; impact on researcher hardware defaults unverified.

**Highest-leverage next action:** Publish MJX/Warp throughput benchmarks on MI300X as a ROCm Blog post, targeting the same researcher audience GAP-13's Hz benchmark targets for commercial teams.

---

### GAP-19 (N91) — No Certified Safety Envelope for AMD AI-Inference Compute
**Fit: H** | **Ecosystem: H** | **Openness: M** | **Evidence: H**

**What's missing:** AMD has zero certified functional-safety path (IEC 61508/ISO 26262) for AI-inference compute. Its existing certifications (TÜV SÜD design flow, TÜV Rheinland SIL3 study) cover Versal/Zynq **FPGA fabric only** — not the AI-engine/XDNA tiles actually running robot control policies.

**Why it's open:** AMD is not starting from zero. The dispatched safety-certification research agent confirmed AMD already has: (a) a TÜV SÜD-certified design-flow solution for Versal adaptive SoCs (IEC 61508 + ISO 26262); (b) a prior TÜV Rheinland SIL3 concept-design study on Zynq 7000; (c) active RTOS partnerships with **QNX** ("robotic system performance" collaboration, extended through 2026) and **Green Hills** (Versal AI Edge Gen 2, "safety certified AI edge growth"). None of these have been extended to cover AI-inference silicon specifically.

**Who's affected:** Every AMD robotics deployment competing against NVIDIA Halos-certified systems (Agility Robotics/Digit is Halos's first adopter) in safety-critical collaborative or industrial environments.

**AMD angle:** Extend existing relationships rather than build new ones — the fastest path is extending the TÜV SÜD design-flow certification and QNX partnership onto Kria X100/Versal AI Edge Gen 2, not launching a new certification program.

**Evidence:** AMD Functional Safety page confirms TÜV SÜD certified design flow (Versal, IEC 61508+ISO 26262) and TÜV Rheinland SIL3 Zynq 7000 study; no IEC 61508/X100-specific certification found; ROCm's "ROCm Certified" program (July 2026) is a developer-skills program, unrelated to functional safety; QNX-AMD collaboration press releases (Mar 2025–2026) confirm active partnership; AMD-Green Hills Alliance confirmed targeting Versal AI Edge Gen 2. [safety-certification agent, sources 1,4,5,6,7]

**Confidence: High** — existing certification infrastructure confirmed; gap (AI-inference tile coverage) confirmed; extension path is well-defined.

**Highest-leverage next action:** Scope a TÜV SÜD design-flow certification extension covering Kria X100's AI-engine tiles, run in parallel with formalizing whether the existing QNX collaboration's "robotic system performance" scope already includes a safety-certified OS roadmap or is purely deterministic/non-safety.

---

### GAP-20 (N92) — No AMD Equivalent to NVIDIA Halos AI Systems Inspection Lab
**Fit: M** | **Ecosystem: H** | **Openness: L** | **Evidence: H**

**What's missing:** NVIDIA Halos bundles IGX Thor hardware + Functional Safety Island + Holoscan Sensor Bridge SIL2 + an **ANAB-accredited AI Systems Inspection Lab** + a 40+ company ecosystem (first adopter: Agility Robotics/Digit) into one full-stack safety program. AMD has no equivalent inspection-lab/ecosystem construct at any maturity stage.

**Why it's distinct from GAP-19:** GAP-19 is about certifying AMD's own compute; this gap is about the accredited third-party inspection infrastructure and partner ecosystem that Halos also provides — a moat that outlasts any single certification.

**Confidence: High** — Halos's structure confirmed; AMD's absence in this specific category confirmed.

**Highest-leverage next action:** Evaluate partnering with an existing ANAB-accredited body (TÜV SÜD, exida) to replicate Halos's inspection-lab function faster than building one from scratch.

---

### GAP-21 (N93) — ISO 25785 Humanoid Safety Standard — Uncontested Participation Window
**Fit: H** | **Ecosystem: M** | **Openness: H** | **Evidence: M**

**What's missing:** ISO/CD 25785-1 (humanoid/dynamically-balanced-robot safety) remains at committee-draft stage as of mid-2026 — an uncontested standards-participation window. No public source lists AMD as a named ISO TC 299 participant (though the safety-certification agent notes AMD or its Alliance Partners could be present in non-public rosters).

**AMD angle:** This is the cheapest, longest-horizon gap in the entire register — standards-body participation costs headcount-hours, not engineering, and shapes the certification requirements every future AMD safety product will need to meet.

**Confidence: Medium** — draft status confirmed; AMD's public non-participation confirmed; private/Alliance-Partner participation unconfirmed either way.

**Highest-leverage next action:** Confirm whether any AMD employee or Alliance Partner is already on ISO TC 299 rosters; if not, nominate a participant — this is a near-zero-cost, high-optionality action.

---

### GAP-22 (N94) — GR00T Fine-Tuning Workflow Locked to NVIDIA Hardware
**Fit: M** | **Ecosystem: M** | **Openness: M** | **Evidence: M**

**What's missing:** NVIDIA GR00T's fine-tuning workflow (data prep, training scripts, deployment tooling) is documented and supported only on NVIDIA hardware/Isaac Lab. No AMD-validated equivalent fine-tuning path is published for GR00T-class foundation models on ROCm, even though other VLA models (SmolVLA, Pi0, ACT) already run on AMD (GAP-5/N22, GAP-10/N76).

**AMD angle:** GR00T specifically is NVIDIA's flagship foundation model — its lock-in is a stronger commercial signal than the smaller open-weight models AMD already supports.

**Confidence: Medium** — lock-in confirmed; scope of porting effort (just the fine-tuning recipe vs. deeper Isaac Lab integration) unverified.

**Highest-leverage next action:** Scope whether porting just the GR00T fine-tuning recipe (without the full Isaac Lab stack) to ROCm is sufficient for a "GR00T on AMD" reference guide.

---

### GAP-23 (N95) — Isaac Teleop Data-Collection Integration in LeRobot Excludes AMD
**Fit: M** | **Ecosystem: M** | **Openness: M** | **Evidence: L**

**What's missing:** Isaac Teleop's data-collection integration path into LeRobot is built and documented for NVIDIA hardware only — teams collecting teleoperation demonstration data through this specific pipeline are implicitly steered onto NVIDIA compute even though the resulting LeRobot dataset itself is hardware-agnostic. Compounds GAP-5/N22 (no AMD model card in LeRobot hub) at an earlier pipeline stage — data collection, not just inference.

**Confidence: Low-Medium** — gap confirmed in the seed report; not independently re-verified by a dispatched agent this round.

**Highest-leverage next action:** Document whether an AMD-compatible teleop data-collection path already exists outside Isaac Teleop that could be published as the ROCm-native alternative.

---

### GAP-24 (N96) — VLA Training Cluster Market: AMD MI300X Capacity Unclaimed
**Fit: M** | **Ecosystem: M** | **Openness: H** | **Evidence: M**

**What's missing:** A VLA training cluster market is emerging (teams renting/buying GPU capacity specifically to train foundation-model-scale robot policies), and NVIDIA DGX/HGX are the default assumption in nearly all public training writeups — despite MI300X's 192GB HBM3 being well-suited to the large-batch, memory-bound training regime VLA models require. No public case study yet documents an AMD-based VLA training cluster at production scale.

**Note:** Training-side counterpart to GAP-13/N79 (which covers inference Hz benchmarking, not training capacity).

**Confidence: Medium** — market emergence and MI300X technical fit confirmed; no case study exists yet either way.

**Highest-leverage next action:** Publish a "VLA foundation model trained end-to-end on MI300X cluster" case study, following the same playbook as the LeRobot pipeline blog that shifted defaults for smaller models.

---

### GAP-25 (N97) — No Robot Inference Observability & Monitoring Layer
**Fit: H** | **Ecosystem: H** | **Openness: H** | **Evidence: H**

**What's missing:** No product unifies per-joint-latency, Hz, VLA action-drift, and model-provenance monitoring for deployed robot fleets. Existing tools (Foxglove, Formant, InOrbit, Cogniteam, Arize, Langfuse, generic OpenTelemetry) each cover a slice but none is robotics-inference-Hz-aware.

**Why it's open:** The dispatched inference-observability research agent confirmed **zero RocProfiler or ROCm-specific integration exists anywhere in this ecosystem**, including in `ros-opentelemetry` (ROSCon 2025 project, maintainer szobov) — the closest extensible building block, since it's OpenTelemetry-based and vendor-neutral by design. AMD's own Robotics Partner Network (30+ members) has zero observability-category partners.

**Who's affected:** Every fleet operator running AMD hardware who currently has no way to monitor inference health, latency, or drift specific to their accelerator.

**AMD angle:** Cheap, high-leverage move (~4-week effort per the seed report) — contribute a RocProfiler↔ROS 2 telemetry exporter into `ros-opentelemetry` rather than build a competing product; partner with Foxglove for visualization.

**Evidence:** No robotics observability platform (Foxglove, Formant, InOrbit, Cogniteam) or generic AI-observability platform (Arize, Langfuse) has any RocProfiler integration; `ros-opentelemetry` confirmed OpenTelemetry-based and vendor-neutral; AMD Robotics Partner Network confirmed to have zero observability partners. [observability agent]

**Confidence: High** — absence confirmed across the entire named ecosystem; fix is bounded and cheap.

**Highest-leverage next action:** Contribute a RocProfiler exporter to `ros-opentelemetry`, then approach Foxglove for a visualization partnership — a 4-week engineering effort with no competing product to displace.

---

### GAP-26 (N98) — No Commercial Data-Intelligence / Fleet-Curation Layer
**Fit: M** | **Ecosystem: M** | **Openness: M** | **Evidence: M**

**What's missing:** Scale AI + Universal Robots (Mar 2026), HuggingFace + NVIDIA LeRobot (58,000+ datasets by May 2026), NVIDIA GR00T N1/N1.6, and HuggingFace's Pollen Robotics acquisition are all consolidating around a data-flywheel narrative — but no commercial "data intelligence layer" exists yet for fleet-scale curation specifically (dedup, quality scoring, active-learning selection across a fleet's raw perception-action stream).

**AMD angle:** Compute-only play (already ROCm-compatible) plus sponsoring an open fleet-curation toolchain — AMD has no natural data-asset position to compete on directly, so the value-add is infrastructure, not data ownership.

**Confidence: Medium** — market consolidation trend confirmed; whether any named player has an unannounced internal product is unverified.

**Highest-leverage next action:** Sponsor or seed an open-source fleet-scale data curation toolchain, positioned as hardware-agnostic but ROCm-default — lower commitment than the MLOps lifecycle platform in GAP-27.

---

### GAP-27 (N99) — No Integrated VLA-Specific Safety-Gated MLOps/Lifecycle Platform — Highest-Conviction Whitespace
**Fit: H** | **Ecosystem: H** | **Openness: H** | **Evidence: H**

**What's missing:** No vendor — general-purpose MLOps platforms (W&B, MLflow, Kubeflow, SageMaker, Azure ML, ClearML, JFrog ML, Domino) or robotics-specific tools (LeRobot, Calibra) — offers an integrated VLA-specific lifecycle platform combining: model registry, safety-gated A/B testing on physical hardware, safe rollback, OTA delivery with certification tracking, and action-level drift detection. Explicitly called **"no vendor owns this layer today"** in the seed report — the single strongest whitespace finding across both new reports.

**Why it's open:** The dispatched MLOps-whitespace research agent independently confirmed this in Sept 2026: point solutions exist for adjacent slices only — Calibra (BSL-1.1 OSS, dataset/embodiment auditing, but pre-deployment on training data, not runtime policies), LeRobot v0.6.0's "Imagine, Evaluate, Improve" sim2real workflow (no registry/rollback), and **Ketryx** (QMS/traceability platform, the closest counter-candidate — traces hazard analysis → SIL requirements → verification evidence with AI-driven change-impact flagging, but this is safety documentation/impact-analysis, not runtime A/B testing, OTA rollback, or action-level drift detection). IDC (May 2026) independently flags "runtime assurance" and "post-incident learning" as unmet governance needs in physical AI.

**Who's affected:** Robotics OEMs and Tier-1 integrators building fleets >50 units, currently stitching together generic MLOps + custom safety scripts.

**AMD angle:** High — this is a software/tooling layer, not silicon-bound, so AMD can anchor it via a ROCm-native reference implementation without competing on GPU FLOPS; owning the registry/rollback/drift schema creates a durable dependency independent of accelerator choice. The agent's suggested entry point: seed a "robotics extension" to MLflow/Kubeflow rather than founding a new framework, since LeRobot/Calibra already have OSS mindshare in the data layer.

**Evidence:** growthmarketreports.com Robotics MLOps Platforms Market 2033 report lists only general-purpose players; Calibra v0.8.0 (Aug 2026) confirmed pre-deployment-only scope; LeRobot v0.6.0 (Jul 2026) confirmed no registry/OTA/safety-gating; Ketryx confirmed as documentation/impact-analysis, not runtime; IDC (May 2026) and Cathay Innovation's May 2026 practitioner survey (n=135, safety/regulation ranked last among current deployment priorities) both independently confirm the tooling layer is unbuilt. [MLOps-whitespace agent, sources 1-6]

**Confidence: High** — this is the single highest-conviction gap in the register: independently confirmed by both the original seed report and a fresh Sept 2026 research pass, with an explicit "no vendor owns this" framing and a named AMD-favorable entry point.

**Highest-leverage next action:** Seed an open-source "robotics extension" to MLflow or Kubeflow implementing VLA-specific model registry + safety-gated rollback + action-level drift detection, ROCm-default but hardware-agnostic — positioning AMD as the founder of the layer rather than a later entrant, before Ketryx or a similar QMS vendor pivots into runtime scope.

---

## Ranking Methodology

Full entries scored by: **AMD fit × ecosystem benefit × openness × evidence strength** (H=3, M=2, L=1, max=12)

| GAP | Node | Fit | Ecosystem | Openness | Evidence | Score |
|-----|------|-----|-----------|----------|----------|-------|
| MLC-LLM CI pipeline (LeRobot VLA) | N76 | 3 | 3 | 3 | 3 | **12** |
| Vendor-neutral robotics inference SDK | N78 | 3 | 3 | 3 | 3 | **12** |
| VLA Hz benchmark gap | N79 | 3 | 3 | 3 | 3 | **12** |
| Differentiable Newton co-architect | N60 | 3 | 3 | 3 | 3 | **12** |
| Genesis Eno silicon selection | N61 | 3 | 3 | 3 | 3 | **12** |
| Warp ROCm backend (upgraded — in-progress) | N42 | 3 | 3 | 3 | 3 | **12** |
| Genesis Partner Network | N44 | 3 | 3 | 3 | 3 | **12** |
| Windows IPC certification | N46 | 3 | 3 | 3 | 3 | **12** |
| LeRobot model hub | N22 | 3 | 3 | 3 | 3 | **12** |
| Fleet edge data center | N48/N62 | 3 | 3 | 3 | 3 | **12** ← *upgraded from M via N62 Pivot* |
| No MLOps/lifecycle whitespace platform (NEW) | N99 | 3 | 3 | 3 | 3 | **12** |
| No robot inference observability layer (NEW) | N97 | 3 | 3 | 3 | 3 | **12** |
| cuRobo motion planning gap (NEW) | N86 | 3 | 3 | 3 | 3 | **12** |
| No certified safety envelope for AI compute (NEW) | N91 | 3 | 3 | 2 | 3 | **11** |
| AMD embedded NPU no open inference compiler | N77 | 3 | 3 | 2 | 3 | **11** |
| FPGA control loop API | N18 | 3 | 3 | 2 | 3 | **11** |
| Synthetic data pipeline | N27 | 3 | 3 | 3 | 2 | **11** |
| ONNX Runtime ROCm EP deprecated (NEW) | N88 | 3 | 3 | 3 | 3 | **12** |
| AMD edge hardware no validated SDK stack (NEW) | N89 | 3 | 3 | 2 | 3 | **11** |
| ISO 25785 participation window (NEW) | N93 | 3 | 2 | 3 | 2 | **10** |
| Halos Inspection Lab equivalent (NEW) | N92 | 2 | 3 | 1 | 3 | **9** |
| Data-flywheel/fleet-curation layer (NEW) | N98 | 2 | 2 | 2 | 2 | **8** |
| No AMD equivalent to Isaac Sim (NEW) | N87 | 2 | 3 | 2 | 2 | **9** |
| No AMD GPU visibility in sim-to-real lit (NEW) | N90 | 2 | 2 | 3 | 2 | **9** |
| GR00T fine-tuning locked to NVIDIA (NEW) | N94 | 2 | 2 | 2 | 2 | **8** |
| Isaac Teleop excludes AMD (NEW) | N95 | 2 | 2 | 2 | 1 | **7** |
| VLA training cluster MI300X unclaimed (NEW) | N96 | 2 | 2 | 3 | 2 | **9** |

*Note: "New" scores were assigned during Iteration 5 integration using the same rubric applied by prior iterations' agents; they have not been independently agent-verified via the frontier-scoring dispatch process, so treat as director-assigned estimates pending further verification.*
