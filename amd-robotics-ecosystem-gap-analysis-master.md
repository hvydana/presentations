# AMD Robotics/Physical-AI Ecosystem Gap Analysis — Master Document

*Consolidated from the Knowledge Flow Graph (`flow_graph/robotics-ecosystem/`), Iterations 1–5. Last updated: 2026-09-06.*
*27 confirmed gaps, organized by technological stack layer. Framing: which layer is missing an AMD-equivalent repo/product/certification vs. NVIDIA's stack, given AMD-ROS (≈ Isaac ROS) and AMD-cuRobo (≈ cuRobo/MoveIt) already exist.*

---

## How to read this document

Each gap lists: **Rank tier** (by 12-point AMD-fit × ecosystem-benefit × openness × evidence score), **what's missing**, **why it's open**, **AMD's angle in**, and the **highest-leverage next action**. Full evidence citations and confidence levels are in `flow_graph/robotics-ecosystem/gap_register.md`; the reasoning trail (which question led to which finding) is in `knowledge_flow_graph.md`.

**Stack layers:**
- **L0** — Real-Time OS / Functional Safety / FPGA control
- **L1** — Infrastructure: Hardware & SDKs
- **L2** — Platform: Sim-to-Real
- **L3** — Application: VLA/Foundation Models & Data
- **L4** — Tooling: Observability & MLOps/Lifecycle
- **L5** — Compliance / Certification

---

## Top 5 Highest-Leverage Actions (Cross-Layer)

1. **Resource the in-progress rocRobo + AMD Warp ROCm PRs (#1770/#1865) to completion and announce** (L1/L2, GAP-1/GAP-14) — cheapest, furthest-along action in the entire register; status just upgraded from "commit to build" to "finish what's started."
2. **Seed an open-source VLA-specific MLOps/lifecycle extension to MLflow or Kubeflow** (L4, GAP-27) — the single highest-conviction whitespace, independently confirmed twice; no vendor owns this layer today.
3. **Contribute a RocProfiler↔ROS 2 exporter to `ros-opentelemetry`** (L4, GAP-25) — ~4-week effort, zero competing product, partner with Foxglove for visualization.
4. **Publish an official AMD VLA inference Hz benchmark** (L3, GAP-13) — zero published numbers exist; AMD's own "~10 Hz" claim is unverified publicly.
5. **Extend the existing TÜV SÜD design-flow certification and QNX partnership to cover AI-inference/XDNA tiles** (L0/L5, GAP-19) — extension of existing infrastructure, not a new certification program.

---

## L0 — Real-Time OS / Functional Safety / FPGA Control

### GAP-6 (N18) — FPGA Control Loop API
**Score: 11/12 (H/H/M/H)**
All SDK building blocks exist (KRS, REP 2008, Xen) — the gap is last-mile packaging, not foundational engineering. ROBOTCORE (Zynq UltraScale+) is a licensable blueprint.
**Next action:** OEM ROBOTCORE as AMD's first-party FPGA robotics SDK layer.

### GAP-11 (N77) — AMD Embedded NPU Has No Open Inference Compiler
MLC-LLM does not deploy on AMD Kria/Versal; Vitis AI DPU is CNN-only; Versal AIE requires closed MLIR-AIE/AMD AIE Compiler with no TVM frontend. Ryzen AI NPU via ONNX Runtime VOE is the more tractable near-term path.
**Next action:** Prioritize an ONNX RT VOE reference path for Ryzen AI NPU robotics workloads over a full TVM/Versal AIE bridge.

### GAP-17 (N89) — AMD Edge Hardware (X100/Kria) Ships With No Validated Robotics SDK Stack
**Score: 11/12** — *NEW, Iteration 5*
AMD's Ryzen AI Embedded X100 and Kria launched (July 2026) into a market where the SDK layer is "nearly empty" at launch — unlike Jetson's day-one Isaac ROS/JetPack maturity. Umbrella gap; GAP-6, GAP-11, and GAP-19 are its specific instances.
**Next action:** Pick one flagship SDK component and ship it as a reference stack timed to hardware availability.

### GAP-19 (N91) — No Certified Safety Envelope for AMD AI-Inference Compute
**Score: 11/12** — *NEW, Iteration 5*
AMD's existing certifications (TÜV SÜD design-flow, IEC 61508+ISO 26262; TÜV Rheinland SIL3 study) cover Versal/Zynq **FPGA fabric only**, not the AI-engine/XDNA tiles running robot control policies. AMD already has active QNX and Green Hills RTOS partnerships that could carry this forward.
**Next action:** Scope extending the TÜV SÜD design-flow certification to cover Kria X100's AI-engine tiles; clarify whether the QNX "robotic system performance" collaboration already implies a safety-certified OS roadmap.
*(See also L5 for the certification-ecosystem angle on this same gap.)*

---

## L1 — Infrastructure: Hardware & SDKs

### GAP-1 / N42 — Warp/Newton ROCm Backend
**Score: 12/12 — STATUS UPGRADED (2026-09-06)**
Newton (Linux Foundation) is adopted by Boston Dynamics, Agility, Figure AI, Toyota, Skild, Samsung; no ROCm commitment from any entity as of Iteration 2. **Update:** `rocRobo` (embryonic AMD motion-planning analog) already exists, and AMD-authored PRs #1770/#1865 are actively upstreaming HIP/ROCm support into `nvidia/warp`.
**Next action (reframed):** Resource the in-progress PRs to completion and announce — not "commit to build."

### GAP-9 (N71) — MLC-LLM CI Pipeline for LeRobot VLA Models
**Score: 12/12**
MLC-LLM already ships ROCm nightly wheels and auto-detects AMD GPU targets at compile time. The gap is one GitHub Actions CI pipeline for LeRobot VLA models (ACT/SmolVLA/Pi0) on AMD gfx942/gfx1100 + publishing to `mlc.ai/wheels` — the vLLM CI playbook applies directly.
**Next action:** Stand up the CI pipeline; this is the single cheapest "community self-porting flywheel" unlock in the register.

### GAP-12 (N73) — Vendor-Neutral Robotics Inference SDK
**Score: 12/12**
No SDK combines ROS2 integration + INT8 + VLA support + GGUF + low latency. Kenning (ROS2+INT8, no VLA) and vla.cpp (VLA+GGUF, no ROS2, ~150ms) are each missing 2+ criteria.
**Next action:** One ROCm EP to vla.cpp + one Kenning VLA backend assembles the alternative.

### GAP-16 (N88) — ONNX Runtime ROCm EP Deprecated
**Score: 12/12** — *NEW, Iteration 5*
ONNX Runtime's ROCm Execution Provider was deprecated, fragmenting AMD's inference path across MIGraphX EP, DirectML, and Vitis AI VOE with no recommended default. A regression, not a never-built gap — directly complicates GAP-12's vendor-neutral SDK effort.
**Next action:** Publish a clear AMD-recommended inference-path decision tree to stop fragmentation compounding into dependent efforts.

### GAP-3 (N45) — Windows Industrial IPC Certification
**Score: 12/12**
ROCm 7.2.2 (CES 2026) unified Windows+Linux — the technical exclusion is closed. AMD has zero certified design wins in the $6.1B Windows industrial IPC market (Beckhoff TwinCAT, Siemens SIMATIC, Advantech).
**Next action:** Pursue TwinCAT 3 ML / SIMATIC Edge GPU/NPU certification — AMD CPU wins already exist (CX20x3, K4131-Px) but zero GPU/NPU wins do.

---

## L2 — Platform: Sim-to-Real

### GAP-2 (N44) — Genesis AI Partner Network
**Score: 12/12**
AMD is already technically engaged with Genesis (ROCm tutorial + arXiv paper); Genesis raising $500M at $3B valuation; AMD is not in the Genesis Robotics Partner Network.
**Next action:** Free enrollment — closes before NVIDIA moves.

### GAP-8 (N61) — Genesis Eno Robot Silicon Selection
**Score: 12/12**
Genesis Eno robot (LG CNS deployment, end-2026 commercial launch) is choosing silicon now; no NVIDIA-Genesis relationship exists yet.
**Next action:** A minimal "Eno on AMD" reference guide is a stronger commercial signal than partner-network enrollment alone.

### GAP-7 (N60) — Differentiable Newton Co-Architect
**Score: 12/12**
MJWarp differentiable physics is incomplete on *any* backend (CUDA or ROCm) — AMD JAX/XLA on ROCm is a co-architect opportunity alongside DeepMind, not a port.
**Next action:** Approach DeepMind researchers for co-authorship on the ROCm/XLA differentiable path.

### GAP-14 (N86) — No AMD Path Into GPU-Accelerated Motion Planning (cuRobo)
**Score: 12/12** — *NEW, Iteration 5*
cuRobo (NVIDIA, embedded in Isaac ROS cuMotion) has no ROCm equivalent — distinct from GAP-1 (simulation substrate); this is the motion-planning application layer. `rocRobo` already exists as an early-stage analog.
**Next action:** Identify rocRobo's maintainers/roadmap; evaluate AMD sponsorship timed with the Warp PR merges.

### GAP-15 (N87) — No AMD Equivalent to Isaac Sim as an Integrated Platform
**Score: 9/12** — *NEW, Iteration 5*
Isaac Sim bundles authoring + physics + rendering + Omniverse; Genesis and Warp/Newton each cover a slice but nothing bundles all three.
**Next action:** Scope whether Genesis + an open rendering stack could be positioned as an Isaac Sim equivalent within 12 months.

### GAP-18 (N90) — No AMD GPU Benchmark Visibility in Sim-to-Real Literature
**Score: 9/12** — *NEW, Iteration 5*
MJX/Warp docs and community writeups cite only NVIDIA GPU numbers, even where AMD hardware would technically run.
**Next action:** Publish MJX/Warp throughput benchmarks on MI300X as a ROCm Blog post.

---

## L3 — Application: VLA/Foundation Models & Data

### GAP-5 (N22) — LeRobot Model Hub Presence
**Score: 12/12**
Working code exists (Pi0, SmolVLA on ROCm) but no AMD model cards are in the LeRobot hub — AMD is invisible at the callsite developers actually use.
**Next action:** Publish model cards; this is a documentation gap, not an engineering one.

### GAP-4 (N27) — Synthetic Data Pipeline
**Score: 11/12**
Genesis World 1.0 Quadrants is ROCm-native; Cosmos 3 Nano is community-confirmed on ROCm. The gap is orchestration and first-party ownership, not components.
**Next action:** Own and publish an end-to-end AMD synthetic-data pipeline reference.

### GAP-13 (N79) — VLA Hz Benchmark Gap
**Score: 12/12**
Zero published Hz benchmarks for VLA inference on AMD exist; AMD's internal "~92ms/~10 Hz" claim (Ryzen AI MAX+ 395) is unverified publicly. Jetson AGX Orin benchmarks (VOTE-MLP4, 55.57 Hz) are public. The action-expert stage is memory-bound — MI300X's 5.3 TB/s HBM3 bandwidth advantage over Jetson's 204 GB/s is entirely unmeasured publicly.
**Next action:** Publish an official, reproducible AMD VLA Hz benchmark — highest-visibility gap-closer in L3.

### GAP-22 (N94) — GR00T Fine-Tuning Workflow Locked to NVIDIA Hardware
**Score: 8/12** — *NEW, Iteration 5*
NVIDIA GR00T's fine-tuning workflow is documented/supported only on NVIDIA hardware, unlike smaller open-weight VLA models (SmolVLA, Pi0, ACT) which already run on AMD.
**Next action:** Scope porting just the GR00T fine-tuning recipe (not the full Isaac Lab stack) to ROCm.

### GAP-23 (N95) — Isaac Teleop Data-Collection Integration in LeRobot Excludes AMD
**Score: 7/12** — *NEW, Iteration 5*
Teams collecting teleop demonstration data via Isaac Teleop's LeRobot integration are implicitly steered onto NVIDIA compute, even though the resulting dataset is hardware-agnostic.
**Next action:** Document or publish a ROCm-native alternative data-collection path.

### GAP-24 (N96) — VLA Training Cluster Market: AMD MI300X Capacity Unclaimed
**Score: 9/12** — *NEW, Iteration 5*
An emerging VLA training-cluster market defaults to NVIDIA DGX/HGX in nearly all public writeups, despite MI300X's 192GB HBM3 fitting the memory-bound training regime well. No public AMD-based VLA training case study exists yet.
**Next action:** Publish a "VLA foundation model trained on MI300X cluster" case study.

---

## L4 — Tooling: Observability & MLOps/Lifecycle

### GAP-25 (N97) — No Robot Inference Observability & Monitoring Layer
**Score: 12/12** — *NEW, Iteration 5*
No product unifies per-joint latency, Hz, VLA action-drift, and model-provenance monitoring for deployed fleets. **Zero RocProfiler integration exists anywhere in this ecosystem** — confirmed across Foxglove, Formant, InOrbit, Cogniteam, Arize, and Langfuse. `ros-opentelemetry` (ROSCon 2025) is the closest extensible, vendor-neutral building block. AMD's own 30+-member Robotics Partner Network has zero observability partners.
**Next action:** Contribute a RocProfiler↔ROS 2 exporter to `ros-opentelemetry` (~4-week effort); partner with Foxglove for visualization. Cheapest high-leverage gap in the whole L4 layer.

### GAP-27 (N99) — No Integrated VLA-Specific Safety-Gated MLOps/Lifecycle Platform
**Score: 12/12 — HIGHEST CONVICTION** — *NEW, Iteration 5*
No vendor — general-purpose (W&B, MLflow, Kubeflow, SageMaker, Azure ML, ClearML, JFrog ML, Domino) or robotics-specific (LeRobot, Calibra) — offers an integrated registry + safety-gated A/B testing + rollback + OTA-with-cert-tracking + action-level drift detection. Independently confirmed twice: once in the seed report, once by a fresh Sept 2026 research pass. Ketryx (QMS/traceability) is the closest counter-candidate but is documentation/impact-analysis only, not runtime. IDC (May 2026) independently flags "runtime assurance" and "post-incident learning" as unmet governance needs.
**Next action:** Seed an open-source "robotics extension" to MLflow or Kubeflow implementing VLA-specific registry + safety-gated rollback + drift detection, ROCm-default but hardware-agnostic — position AMD as the layer's founder before Ketryx or a similar vendor pivots into runtime scope.

### GAP-26 (N98) — No Commercial Data-Intelligence / Fleet-Curation Layer
**Score: 8/12** — *NEW, Iteration 5*
Scale AI + Universal Robots, HuggingFace + NVIDIA LeRobot (58,000+ datasets), GR00T N1/N1.6, and the HuggingFace/Pollen Robotics acquisition are all consolidating around a data-flywheel narrative, but no commercial fleet-scale curation layer (dedup, quality scoring, active-learning selection) exists yet.
**Next action:** Sponsor or seed an open fleet-scale data curation toolchain — lower commitment than GAP-27.

---

## L5 — Compliance / Certification

### GAP-19 (N91) — see L0 above (cross-listed)
The certification-extension angle: AMD's existing TÜV SÜD/TÜV Rheinland certifications and QNX/Green Hills partnerships need to be extended to AI-inference tiles, not rebuilt from scratch.

### GAP-20 (N92) — No AMD Equivalent to NVIDIA Halos AI Systems Inspection Lab
**Score: 9/12** — *NEW, Iteration 5*
Halos bundles IGX Thor hardware + Functional Safety Island + Holoscan Sensor Bridge SIL2 + an ANAB-accredited AI Systems Inspection Lab + a 40+ company ecosystem (first adopter: Agility Robotics/Digit). AMD has no equivalent inspection-lab/ecosystem construct at any maturity stage — distinct from GAP-19 (certifying AMD's own compute) because this is the accredited third-party inspection infrastructure and partner moat.
**Next action:** Evaluate partnering with an existing ANAB-accredited body (TÜV SÜD, exida) to replicate Halos's inspection-lab function faster than building one from scratch.

### GAP-21 (N93) — ISO 25785 Humanoid Safety Standard — Uncontested Participation Window
**Score: 10/12** — *NEW, Iteration 5*
ISO/CD 25785-1 (humanoid/dynamically-balanced-robot safety) remains at committee-draft stage; no public source lists AMD as a named ISO TC 299 participant. Cheapest, longest-horizon action in the entire register — standards participation costs headcount-hours, not engineering, and shapes every future AMD safety-certification requirement.
**Next action:** Confirm whether any AMD employee or Alliance Partner is already on ISO TC 299 rosters; if not, nominate one.

---

## Full Ranked Score Table (all 27 gaps)

| Gap | Layer | Node | Score | Status |
|-----|-------|------|-------|--------|
| GAP-1 Warp ROCm backend | L1/L2 | N42 | 12 | Upgraded — in progress |
| GAP-2 Genesis Partner Network | L2 | N44 | 12 | Open |
| GAP-5 LeRobot model hub | L3 | N22 | 12 | Open |
| GAP-7 Differentiable Newton co-architect | L2 | N60 | 12 | Open |
| GAP-8 Genesis Eno silicon selection | L2 | N61 | 12 | Open |
| GAP-9 MLC-LLM CI pipeline | L1 | N76 | 12 | Open |
| GAP-3 Windows IPC certification | L1 | N46 | 12 | Open |
| GAP-10 Fleet edge data center | L1 | N48/N62 | 12 | Open (upgraded) |
| GAP-12 Vendor-neutral inference SDK | L1 | N78 | 12 | Open |
| GAP-13 VLA Hz benchmark gap | L3 | N79 | 12 | Open |
| GAP-14 cuRobo motion-planning gap | L2 | N86 | 12 | New |
| GAP-16 ONNX RT ROCm EP deprecated | L1 | N88 | 12 | New |
| GAP-25 Robot inference observability | L4 | N97 | 12 | New |
| GAP-27 MLOps/lifecycle whitespace | L4 | N99 | 12 | New — highest conviction |
| GAP-6 FPGA control loop API | L0 | N18 | 11 | Open |
| GAP-11 AMD embedded NPU compiler | L0 | N77 | 11 | Open |
| GAP-4 Synthetic data pipeline | L3 | N27 | 11 | Open |
| GAP-17 Edge hardware no validated SDK | L0 | N89 | 11 | New |
| GAP-19 No certified AI-inference safety envelope | L0/L5 | N91 | 11 | New |
| GAP-21 ISO 25785 participation window | L5 | N93 | 10 | New |
| GAP-15 No Isaac Sim equivalent | L2 | N87 | 9 | New |
| GAP-18 No AMD GPU visibility in sim-to-real lit | L2 | N90 | 9 | New |
| GAP-20 No Halos Inspection Lab equivalent | L5 | N92 | 9 | New |
| GAP-24 VLA training cluster unclaimed | L3 | N96 | 9 | New |
| GAP-22 GR00T fine-tuning locked to NVIDIA | L3 | N94 | 8 | New |
| GAP-26 No fleet-curation/data-intelligence layer | L4 | N98 | 8 | New |
| GAP-23 Isaac Teleop excludes AMD | L3 | N95 | 7 | New |

*Full evidence, confidence levels, and citations for every gap: `flow_graph/robotics-ecosystem/gap_register.md`. Full reasoning trail (question → dispatch → finding → gap): `flow_graph/robotics-ecosystem/knowledge_flow_graph.md`. Iteration-by-iteration process log: `flow_graph/robotics-ecosystem/iteration_log.md`.*
