# AMD Robotics / Physical-AI — Ecosystem Gap Census

*Generated 2026-09-06 by `render_gaps.py` from `catalog.tsv` + `gaps.tsv`. Do not hand-edit — edit the ledgers and re-render.*

**279 ecosystem components enumerated and checked. 182 are gaps. 5 unresolved.**

This is a *census*, not a search: every row below came from an external component catalog (NVIDIA's shipped stack, ROS Index, the open-source robotics ecosystem) and was checked for an AMD path regardless of how promising it looked. The denominator is therefore meaningful — see `coverage.md`.

## Ranked shortlist

Score = openness × AMD fit × ecosystem leverage × evidence strength (1–81). P0 ≥ 36, P1 ≥ 18, P2 ≥ 8.

| # | Score | Tier | Layer | Gap | AMD status | First action |
|---|-------|------|-------|-----|------------|--------------|
| 1 | 81 | P0 | L1 | **No single edge inference optimizer spanning Ryzen AI NPU Radeon iGPU and Kria FPGA** | partial | Unify NPU iGPU and FPGA behind one ONNX Runtime edge profile with published latency |
| 2 | 81 | P0 | L1 | **No first-party ROS 2 detection nodes with AMD-published accuracy and throughput for YOLO/RT-DETR** | partial | Publish a supported isaac_ros_object_detection-equivalent ROS 2 package with per-SKU benchmark numbers |
| 3 | 81 | P0 | L1 | **No end-to-end GPU-accelerated manipulation reference workflow bringup on AMD** | partial | Publish a MoveIt plus perception plus grasp reference bringup for a common arm on the Kria dev platform |
| 4 | 81 | P0 | L1 | **No low-latency sensor-to-inference streaming graph framework with zero-copy or RDMA sensor bridge equivalent** | partial | Extend the Robotics Software Suite with a documented zero-copy sensor ingest graph API on Versal and Kria |
| 5 | 81 | P0 | L2 | **No AMD-backed GPU-resident massively parallel RL and IL environment framework** | community | Fund and CI-validate MJX-JAX on ROCm and publish a parallel-environment RL training reference |
| 6 | 81 | P0 | L2 | **No GPU-resident rigid body and articulation solver maintained on ROCm, the open Newton engine depends on NVIDIA Warp** | community | Contribute a HIP or Triton solver backend to Newton, or port Warp kernels, to break the CUDA dependency |
| 7 | 81 | P0 | L2 | **Warp has no merged ROCm backend; AMD PRs are in flight but unlanded** | partial | Resource PRs #1770/#1865 to completion and announce — cheapest action in the register |
| 8 | 81 | P0 | L2 | **No real-capture-to-simulation neural reconstruction pipeline that feeds reconstructed scenes into a robot simulator** | partial | Publish a ROCm gsplat to Gazebo or MuJoCo scene export reference so captures become simulatable assets |
| 9 | 81 | P0 | L1 | **No drop-in GPU/FPGA-accelerated replacement for the standard image_proc and stereo_image_proc nodes on AMD silicon** | partial | Ship ROCm and Vitis backed image_proc and stereo_image_proc nodes with identical topic and parameter contracts to image_pipeline |
| 10 | 81 | P0 | L1 | **MLC-LLM has no CI publishing AMD artifacts for LeRobot VLA models** | partial | Stand up the GitHub Actions CI and publish to mlc.ai/wheels — the vLLM CI playbook applies directly |
| 11 | 81 | P0 | L2 | **Upstream perf investment has moved to MJX-Warp which is NVIDIA-only leaving the AMD path on the slower JAX branch** | partial | Fund an MJX-Warp-equivalent HIP/Triton backend or upstream ROCm kernels and publish MI300X env-steps/sec numbers |
| 12 | 81 | P0 | L2 | **AMD is technically engaged with Genesis but absent from its Robotics Partner Network** | community | Enroll in the Genesis partner network (free) and publish an Eno-on-AMD reference guide before NVIDIA moves |
| 13 | 81 | P0 | L2 | **ManiSkill lists GPU simulation as unsupported on AMD GPUs so the flagship parallel manipulation benchmark cannot run on ROCm** | none | Get ManiSkill CPU-sim CI green on ROCm first, then sponsor a ROCm GPU-sim backend via its SAPIEN dependency |
| 14 | 81 | P0 | L2 | **No ROCm-accelerated MoveIt planner plugin; AMD only runs the CPU planners while cuRobo gives NVIDIA order-of-magnitude planning latency wins** | partial | Ship a HIP/Triton batched collision-checking and trajectory-optimization MoveIt plugin as a cuRobo answer |
| 15 | 81 | P0 | L3 | **Upstream openpi JAX/CUDA training stack has no ROCm build so AMD users can only reach pi0 through the LeRobot re-implementation** | partial | Publish a ROCm-tested openpi container and upstream a ROCm install path plus CI job to Physical-Intelligence/openpi |
| 16 | 81 | P0 | L3 | **No AMD GPU in upstream LeRobot CI so ROCm-only breakages ship unnoticed (uint8 bilinear interpolate NotImplementedError in SmolVLA resize_with_pad)** | partial | Donate a gfx942 and gfx1100 runner to huggingface/lerobot CI and gate policy tests on it |
| 17 | 81 | P0 | L3 | **No AMD model cards in the LeRobot hub — AMD is invisible at the developer callsite** | community | Publish model cards; this is a documentation gap, not an engineering one |
| 18 | 81 | P0 | L6 | **No AMD-published VLA policy checkpoints or LeRobot datasets despite an active and large HF org** | partial | Publish ROCm-validated ACT, SmolVLA and pi0 checkpoints and one teleop dataset under huggingface.co/amd |
| 19 | 81 | P0 | L5 | **No safety-certifiable RTOS image or certification artifact package that runs on AMD adaptive SoCs and Kria SOMs** | partial | Fund an upstream Zephyr board port plus safety-scope certification evidence for Kria K24/K26 so customers inherit the artifacts |
| 20 | 81 | P0 | L4 | **No integrated VLA-specific safety-gated MLOps and lifecycle platform exists from any vendor** | none | Seed an open-source robotics extension to MLflow or Kubeflow — registry, safety-gated rollback, drift detection — ROCm-default but hardware-agnostic |
| 21 | 81 | P0 | L4 | **No product unifies per-joint latency, Hz, VLA action-drift and model provenance for deployed fleets** | none | Build on ros-opentelemetry and partner with Foxglove for visualization |
| 22 | 81 | P0 | L4 | **Zero RocProfiler integration exists anywhere in the robotics or AI observability ecosystem** | none | Contribute a RocProfiler-to-ROS 2 exporter to ros-opentelemetry — roughly a 4-week effort with no competing product |
| 23 | 81 | P0 | L3 | **Zero published VLA inference Hz benchmarks on AMD silicon; the action-expert stage is memory-bound and unmeasured** | none | Publish an official reproducible AMD VLA Hz benchmark — highest-visibility single gap-closer in L3 |
| 24 | 81 | P0 | L1 | **No SDK combines ROS 2 integration, INT8, VLA support, GGUF and low latency** | none | One ROCm EP for vla.cpp plus one Kenning VLA backend assembles the alternative |
| 25 | 81 | P0 | L1 | **No single recommended AMD inference execution path; guidance is fragmented across EPs** | none | Publish the decision tree — a documentation action that unblocks several dependent efforts |

## Gaps by layer

### L0 — Silicon, RTOS, Real-Time Control & Functional Safety

*35 components checked · 23 gaps*

#### [P0 · 81] AMD edge hardware (Ryzen AI X100, Kria) shipped into a nearly empty SDK layer, unlike Jetson's day-one maturity

- **Component / trigger:** (whitespace) day-one edge robotics SDK bundle (NONE) — reference robotics SDK stack shipped with edge AI hardware at launch
- **AMD status:** `none` — no AMD path
- **Who is blocked:** every design win evaluating AMD edge silicon
- **Action:** Pick one flagship SDK component and ship it as a reference stack timed to hardware availability — umbrella for several other gaps
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-17
- **Component ref:** derived:grid-sweep

#### [P0 · 54] No AMD-published PREEMPT_RT reference config or RT-safe ROCm/NPU submission path

- **Component / trigger:** PREEMPT_RT (OSS) — Deterministic scheduling in Linux kernel
- **AMD status:** `partial` — partial / in progress (nearest: Ryzen AI Embedded X100 firm real-time Linux with sub-7us interrupt latency plus PetaLinux RT kernels)
- **Who is blocked:** ros2_control users running GPU inference and a hard control loop on one SoC
- **Action:** Publish an RT kernel BSP with cyclictest and ROCm-under-RT jitter numbers for X100
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.servethehome.com/amds-physical-ai-plans-come-into-focus-as-company-launches-ryzen-embedded-ai-x100/
- **Component ref:** https://wiki.linuxfoundation.org/realtime/start

#### [P0 · 54] No AMD-maintained or FPGA-offloaded EtherCAT master integrated with the Robotics Software Suite

- **Component / trigger:** IgH EtherCAT Master (OSS) — EtherCAT fieldbus master stack
- **AMD status:** `partial` — partial / in progress (nearest: IgH master runs on AMD x86 Linux and the Kria robotics platform exposes EtherCAT/TSN ports)
- **Who is blocked:** Industrial servo and motion integrators building on Kria carriers
- **Action:** Publish a validated IgH-on-X100 reference with cycle jitter numbers and a Spartan offload option
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.cnx-software.com/2026/07/24/amd-launches-ryzen-ai-embedded-x100-processors-kria-ai-som-and-physical-ai-robotics-developer-platform/
- **Component ref:** https://gitlab.com/etherlab.org/ethercat

#### [P0 · 54] No AMD-maintained ros2_control hardware interface for FPGA fabric or EtherCAT I/O

- **Component / trigger:** ros2_control (OSS) — Hardware interface and controller execution
- **AMD status:** `partial` — partial / in progress (nearest: ros2_control runs on X100; AMD cites a Bosch Rexroth controller at 8000 control decisions per second)
- **Who is blocked:** Arm and AMR builders wiring Kria carrier I/O into ROS 2 control
- **Action:** Open-source a ros2_control hardware_interface plugin for the Kria carrier FPGA
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/ai.html
- **Component ref:** https://github.com/orgs/ros-controls/repositories

#### [P0 · 54] No AMD-maintained static partitioning hypervisor or mixed-criticality reference for Kria or Versal

- **Component / trigger:** Jailhouse (Siemens / OSS) — Static partitioning hypervisor for mixed criticality
- **AMD status:** `community` — community-maintained only (nearest: Jailhouse upstream supports Xilinx ZCU102 Zynq UltraScale+ and AMD x86 with SVM and NPT, but Siemens maintains it)
- **Who is blocked:** Robot builders consolidating safety-critical control and AI inference onto one AMD SoC
- **Action:** Adopt and CI-test the Jailhouse ZCU102 cell configuration on a current Kria KR260 image
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 3 · confidence high
- **Evidence:** https://github.com/siemens/jailhouse
- **Component ref:** https://github.com/siemens/jailhouse

#### [P0 · 54] FPGA real-time control loop is not callable from ROS 2 or Python — last-mile packaging, not foundational engineering

- **Component / trigger:** (whitespace) FPGA control-loop high-level API (NONE) — FPGA real-time control loop callable from ROS 2/Python
- **AMD status:** `none` — no AMD path (nearest: KRS, REP 2008 and Xen are the building blocks; ROBOTCORE is a licensable blueprint)
- **Who is blocked:** robotics teams that would use FPGA determinism but will not write RTL
- **Action:** OEM ROBOTCORE as AMD's first-party FPGA robotics SDK layer
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-6
- **Component ref:** derived:grid-sweep

#### [P0 · 36] No unified robotics BSP bundling RT preempt kernel secure boot and OTA in one supported image

- **Component / trigger:** Jetson Linux / JetPack 7 (NVIDIA) — Embedded Linux BSP real-time kernel
- **AMD status:** `partial` — partial / in progress (nearest: Ubuntu plus ROCm on X100 and PetaLinux/Yocto on Kria)
- **Who is blocked:** Robot integrators who must assemble kernel security and update stack themselves
- **Action:** Ship one versioned robotics BSP image for X100 plus Kria with RT kernel and OTA
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.cnx-software.com/2022/05/18/349-amd-kria-kr260-robotics-starter-kit-takes-on-nvidia-jetson-agx-xavier-devkit/
- **Component ref:** https://developer.nvidia.com/embedded/jetpack

#### [P0 · 36] No AMD first-party EtherCAT master or slave stack and no ros2_control bridge on Kria

- **Component / trigger:** EtherCAT (EtherCAT Technology Group) — Deterministic fieldbus for servo drives
- **AMD status:** `partial` — partial / in progress (nearest: Kria K24 and KD240 with Vitis Motor Control libraries and PL Ethernet; EtherCAT stacks come from third-party IP vendors)
- **Who is blocked:** Multi-axis servo integrators wiring ROS 2 down to drives on AMD SoCs
- **Action:** Ship an EtherCAT master reference design on KD240 wired into ros2_control
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/k24/kd240-drives-starter-kit.html
- **Component ref:** https://www.ethercat.org/en/technology.html

#### [P0 · 36] No open ML compiler reaches AMD embedded NPU/AI-engine tiles; MLC-LLM does not deploy to Kria/Versal

- **Component / trigger:** (whitespace) open compiler path to embedded NPU (NONE) — open ML compiler targeting embedded NPU/AI-engine tiles
- **AMD status:** `none` — no AMD path (nearest: Vitis AI DPU is CNN-only; Ryzen AI ONNX RT VOE is the tractable path)
- **Who is blocked:** embedded robotics teams on AMD NPU silicon
- **Action:** Prioritize an ONNX RT VOE reference path for Ryzen AI NPU over a full TVM/Versal AIE bridge
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 2 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-11
- **Component ref:** derived:grid-sweep

#### [P1 · 27] No AMD ASIL-D safety companion MCU and no packaged robot safety-island reference to answer NVIDIA Halos

- **Component / trigger:** AURIX TC4x (Infineon) — Lockstep safety co-processor MCU
- **AMD status:** `partial` — partial / in progress (nearest: Dual Cortex-R5F lockstep on Zynq UltraScale+ and Kria K26 plus a TUV SUD certified functional safety design flow)
- **Who is blocked:** Humanoid and cobot OEMs needing a certifiable emergency stop path beside AI compute
- **Action:** Package R5F lockstep plus IDF isolation into a documented robot safety island reference design
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/functional-safety.html
- **Component ref:** https://www.infineon.com/cms/en/product/microcontroller/32-bit-tricore-microcontroller/

#### [P1 · 24] No AMD-validated humanoid whole-body control library or reference policy stack

- **Component / trigger:** GR00T-WholeBodyControl (NVIDIA) — Humanoid whole-body control
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Humanoid developers evaluating ROCm as the training and deployment target
- **Action:** Validate one open WBC stack end to end on ROCm and publish the recipe and rates
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://developer.nvidia.com/isaac/gr00t
- **Component ref:** https://developer.nvidia.com/isaac/gr00t

#### [P1 · 24] No AMD-supplied CANopen CiA 402 drive state machine bridging Vitis motor control to ROS 2

- **Component / trigger:** CANopen CiA 402 drive profile (CAN in Automation) — CAN device profile for drives and motion
- **AMD status:** `partial` — partial / in progress (nearest: CAN and RS-485 controllers on Kria KD240 plus Vitis Motor Control libraries, but no CiA 402 profile stack)
- **Who is blocked:** Low-cost servo, gripper and joint-module integrators building on Kria
- **Action:** Publish a CiA 402 drive state machine example on KD240 CAN wired to ros2_control
- **Scores:** openness 2 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/k24/kd240-drives-starter-kit.html
- **Component ref:** https://www.can-cia.org/canopen

#### [P1 · 24] No safety island paired with AMD AI compute in the way one vendor already ships

- **Component / trigger:** (whitespace) safety island alongside AI accelerator (NONE) — safety co-processor / functional safety island for AI compute
- **AMD status:** `none` — no AMD path
- **Who is blocked:** OEMs architecting mixed-criticality robot compute
- **Action:** Evaluate whether Versal deterministic fabric can be positioned as the safety island beside the AI tiles
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-19
- **Component ref:** derived:grid-sweep

#### [P1 · 18] No single shipping robot-brain SoC with an integrated safety island at Thor class

- **Component / trigger:** Jetson AGX Thor (NVIDIA) — Robot edge AI compute silicon
- **AMD status:** `partial` — partial / in progress (nearest: Ryzen AI Embedded X100 plus Kria AI SoM Robotics Developer Platform)
- **Who is blocked:** Humanoid and AMR OEMs choosing a 2026 compute platform
- **Action:** Publish X100 plus Kria FuSa roadmap and firm dev-kit GA dates against Thor
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.cnx-software.com/2026/07/24/amd-launches-ryzen-ai-embedded-x100-processors-kria-ai-som-and-physical-ai-robotics-developer-platform/
- **Component ref:** https://developer.nvidia.com/embedded/jetpack

#### [P1 · 18] No safety-certified hypervisor with an AMD-validated BSP and safety island for robot SoCs

- **Component / trigger:** QNX Hypervisor for Safety (BlackBerry QNX) — Safety-certified hypervisor for robot SoCs
- **AMD status:** `partial` — partial / in progress (nearest: Xen on Versal/Zynq and Ryzen Embedded; no QNX-certified host BSP or safety island from AMD)
- **Who is blocked:** Humanoid and AMR OEMs needing SIL/ASIL partitioning between an AI Linux VM and a certified RTOS VM on AMD silicon
- **Action:** Fund a QNX SDP 8 plus QNX Hypervisor for Safety reference BSP on Versal and Ryzen Embedded X100 and publish the partitioning reference design
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://bananarat.com/blogs/blog/qnx-robotics-humanoid-safety-layer
- **Component ref:** https://blackberry.qnx.com/en/products/foundation-software/qnx-hypervisor

#### [P2 · 12] No documented FPGA-to-GPU-memory direct sensor ingest path equivalent to Holoscan Sensor Bridge

- **Component / trigger:** Holoscan Sensor Bridge (NVIDIA) — FPGA sensor-to-GPU data ingest
- **AMD status:** `partial` — partial / in progress (nearest: Kria FPGA paired with X100 in the AMD Robotics Developer Platform)
- **Who is blocked:** Multi-camera and lidar rigs needing deterministic low-latency ingest
- **Action:** Document and benchmark a Kria PL to Radeon iGPU zero-copy sensor ingest reference design
- **Scores:** openness 2 · fit 3 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://www.cnx-software.com/2026/07/24/amd-launches-ryzen-ai-embedded-x100-processors-kria-ai-som-and-physical-ai-robotics-developer-platform/
- **Component ref:** https://docs.nvidia.com/holoscan/

#### [P2 · 12] No AMD packaging or NIC/RT validation of a lightweight embeddable EtherCAT master

- **Component / trigger:** SOEM (OSS) — Lightweight EtherCAT master library
- **AMD status:** `community` — community-maintained only (nearest: SOEM builds and runs unmodified on AMD x86 and ARM Linux hosts)
- **Who is blocked:** Embedded integrators wanting fieldbus control from an AMD SoC without a kernel master
- **Action:** Add SOEM to AMD robotics reference images with a tested NIC and real-time configuration
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://github.com/OpenEtherCATsociety/SOEM
- **Component ref:** https://github.com/OpenEtherCATsociety/SOEM

#### [P2 · 12] No AMD analogue of the NVIDIA IGX Linux-plus-QNX hypervisor partitioned safety reference design

- **Component / trigger:** QNX Neutrino RTOS 8.0 (BlackBerry QNX) — Certified microkernel RTOS for robot controllers
- **AMD status:** `partial` — partial / in progress (nearest: QNX 8 runs on AMD x86-64 embedded, but AMD ships no Kria or Versal BSP and no safety-partitioned reference)
- **Who is blocked:** Humanoid and automotive integrators needing a certified RTOS partition beside AI compute
- **Action:** Publish a Kria or Ryzen AI Embedded reference that runs a certified RTOS partition next to the Linux AI domain
- **Scores:** openness 1 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://bananarat.com/blogs/blog/qnx-robotics-humanoid-safety-layer
- **Component ref:** https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems

#### [P2 · 9] On-die hardware isolation exists but there is no certified separation-kernel RTOS story on AMD adaptive SoCs

- **Component / trigger:** INTEGRITY-178 tuMP (Green Hills Software) — Separation-kernel RTOS for certified systems
- **AMD status:** `partial` — partial / in progress (nearest: TUV SUD certified Isolation Design Flow and Vivado Isolation Verifier for on-die spatial partitioning)
- **Who is blocked:** DO-178C and IEC 61508 aerospace and defence robot controller programs
- **Action:** Co-publish an INTEGRITY or PikeOS partitioning reference on Versal AI Edge backed by IDF isolation evidence
- **Scores:** openness 1 · fit 3 · leverage 1 · evidence 3 · confidence med
- **Evidence:** https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/functional-safety.html
- **Component ref:** https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems

#### [P3 · 6] No NuttX architecture or board port for AMD Zynq R5 or MicroBlaze V

- **Component / trigger:** Apache NuttX (OSS) — Real-time OS for flight/motor control
- **AMD status:** `none` — no AMD path
- **Who is blocked:** PX4 and drone developers who would otherwise use an AMD SoC as flight controller
- **Action:** Either upstream a ZynqMP R5 NuttX board port or explicitly point flight-control users at the existing Zephyr AMD ports
- **Scores:** openness 3 · fit 1 · leverage 1 · evidence 2 · confidence med
- **Evidence:** https://github.com/apache/nuttx/tree/master/arch/arm/src
- **Component ref:** https://github.com/apache/nuttx

#### [P3 · 6] No AMD-validated co-kernel option for workloads where PREEMPT_RT jitter is insufficient

- **Component / trigger:** Xenomai (OSS) — Hard real-time Linux co-kernel
- **AMD status:** `community` — community-maintained only (nearest: Xenomai and EVL build on AMD x86-64 and ARM hosts with no AMD packaging or validation)
- **Who is blocked:** Motion-control vendors needing hard real-time on Ryzen Embedded
- **Action:** Validate and document Xenomai or EVL on X100 as an alternative to PREEMPT_RT
- **Scores:** openness 3 · fit 2 · leverage 1 · evidence 1 · confidence low
- **Evidence:** https://xenomai.org/
- **Component ref:** https://xenomai.org/

#### [P3 · 6] Could not confirm any AMD first-party or partner PROFINET IRT stack for Zynq UltraScale+ or Versal

- **Component / trigger:** PROFINET IRT (PROFIBUS and PROFINET International) — Isochronous industrial Ethernet for cells
- **AMD status:** `unknown` — UNRESOLVED (coverage debt)
- **Who is blocked:** Siemens-centric factory cell integrators evaluating AMD SoCs as a cell controller
- **Action:** Audit the AMD industrial partner IP catalogue and state PROFINET IRT coverage publicly
- **Scores:** openness 1 · fit 3 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://www.amd.com/en/solutions/industrial.html
- **Component ref:** https://www.profibus.com/technology/profinet

#### [P3 · 4] Unclear whether Wind River publishes a current VxWorks BSP for Kria, Versal or Ryzen Embedded

- **Component / trigger:** VxWorks (Wind River) — Hard real-time OS for industrial controllers
- **AMD status:** `unknown` — UNRESOLVED (coverage debt)
- **Who is blocked:** Industrial arm, aerospace and legacy controller vendors standardized on VxWorks
- **Action:** Confirm VxWorks BSP coverage for Kria and Ryzen Embedded and state it on the AMD partner page
- **Scores:** openness 1 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://www.strategicmarketresearch.com/market-report/functional-safety-market
- **Component ref:** https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems

### L1 — Runtime & Middleware (ROS 2, transport, inference runtime)

*67 components checked · 40 gaps*

#### [P0 · 81] No single edge inference optimizer spanning Ryzen AI NPU Radeon iGPU and Kria FPGA

- **Component / trigger:** TensorRT (NVIDIA) — Inference optimizer and runtime
- **AMD status:** `partial` — partial / in progress (nearest: MIGraphX plus ONNX Runtime MIGraphX and Vitis AI execution providers)
- **Who is blocked:** Robot perception teams forced to maintain three separate compile paths
- **Action:** Unify NPU iGPU and FPGA behind one ONNX Runtime edge profile with published latency
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://onnxruntime.ai/docs/execution-providers/MIGraphX-ExecutionProvider.html
- **Component ref:** https://developer.nvidia.com/embedded/jetpack

#### [P0 · 81] No first-party ROS 2 detection nodes with AMD-published accuracy and throughput for YOLO/RT-DETR

- **Component / trigger:** isaac_ros_object_detection (NVIDIA) — 2D object detection nodes
- **AMD status:** `partial` — partial / in progress (nearest: AMD ROS 2 Perception Node plus MIGraphX and Ryzen AI ONNX execution providers)
- **Who is blocked:** Every robot doing 2D detection that is evaluating AMD vs Jetson
- **Action:** Publish a supported isaac_ros_object_detection-equivalent ROS 2 package with per-SKU benchmark numbers
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://newsroom.amd.com/news/aai-2026-robotics-partner-network/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 81] No end-to-end GPU-accelerated manipulation reference workflow bringup on AMD

- **Component / trigger:** isaac_ros_manipulation (NVIDIA) — Arm manipulation workflow bringup
- **AMD status:** `partial` — partial / in progress (nearest: ROS 2 plus MoveIt on ROCm named as supported in Kria AI Robotics Developer Platform)
- **Who is blocked:** Arm and cobot integrators wanting a working pick-place stack out of the box
- **Action:** Publish a MoveIt plus perception plus grasp reference bringup for a common arm on the Kria dev platform
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 81] No low-latency sensor-to-inference streaming graph framework with zero-copy or RDMA sensor bridge equivalent

- **Component / trigger:** Holoscan SDK (NVIDIA) — Streaming sensor AI pipeline SDK
- **AMD status:** `partial` — partial / in progress (nearest: AMD ROS 2 Perception Node accelerated application plus AMD Robotics Software Suite on ROCm and ROS 2)
- **Who is blocked:** Medical imaging, industrial inspection and sensor-streaming ISVs on AMD embedded silicon
- **Action:** Extend the Robotics Software Suite with a documented zero-copy sensor ingest graph API on Versal and Kria
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://docs.nvidia.com/holoscan/

#### [P0 · 81] No drop-in GPU/FPGA-accelerated replacement for the standard image_proc and stereo_image_proc nodes on AMD silicon

- **Component / trigger:** image_pipeline (OSS) — Camera rectification and stereo processing
- **AMD status:** `partial` — partial / in progress (nearest: AMD ROS 2 Perception Node accelerated application plus Vitis Vision libraries)
- **Who is blocked:** ROS 2 perception developers porting Isaac ROS image pipelines who lose rectification and disparity acceleration
- **Action:** Ship ROCm and Vitis backed image_proc and stereo_image_proc nodes with identical topic and parameter contracts to image_pipeline
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-robotics-partner-network/
- **Component ref:** https://github.com/ros-perception/image_pipeline

#### [P0 · 81] MLC-LLM has no CI publishing AMD artifacts for LeRobot VLA models

- **Component / trigger:** MLC-LLM (OSS) — On-device LLM/VLM compilation and serving
- **AMD status:** `partial` — partial / in progress (nearest: ROCm nightly wheels, AMD GPU auto-detect)
- **Who is blocked:** developers wanting prebuilt ACT/SmolVLA/pi0 on gfx942/gfx1100
- **Action:** Stand up the GitHub Actions CI and publish to mlc.ai/wheels — the vLLM CI playbook applies directly
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-9
- **Component ref:** https://github.com/mlc-ai/mlc-llm

#### [P0 · 81] No SDK combines ROS 2 integration, INT8, VLA support, GGUF and low latency

- **Component / trigger:** (whitespace) vendor-neutral robotics inference SDK (NONE) — robotics inference SDK combining ROS 2 + INT8 + VLA + low latency
- **AMD status:** `none` — no AMD path (nearest: Kenning and vla.cpp each miss 2+ criteria)
- **Who is blocked:** anyone deploying VLA policies outside the NVIDIA stack
- **Action:** One ROCm EP for vla.cpp plus one Kenning VLA backend assembles the alternative
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-12
- **Component ref:** derived:grid-sweep

#### [P0 · 81] No single recommended AMD inference execution path; guidance is fragmented across EPs

- **Component / trigger:** (whitespace) inference-path decision tree (NONE) — single recommended inference execution path per accelerator vendor
- **AMD status:** `none` — no AMD path
- **Who is blocked:** developers choosing how to deploy a model on AMD
- **Action:** Publish the decision tree — a documentation action that unblocks several dependent efforts
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-16
- **Component ref:** derived:grid-sweep

#### [P0 · 54] No AMD-supported C++ edge VLM runtime targeted at closed-loop robot control rates

- **Component / trigger:** TensorRT-Edge-LLM (NVIDIA) — Edge LLM/VLM inference runtime
- **AMD status:** `partial` — partial / in progress (nearest: Lemonade Server plus llama.cpp and MLC-LLM on ROCm and Ryzen AI)
- **Who is blocked:** VLA and VLM policy developers needing bounded per-step latency on embedded AMD parts
- **Action:** Turn Lemonade into a supported C++ embeddable runtime with robot-loop latency SLAs
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://rocm.blogs.amd.com/blog/author.html
- **Component ref:** https://github.com/NVIDIA/TensorRT-Edge-LLM

#### [P0 · 54] No published family of ROS 2 inference nodes binding MIGraphX and Vitis AI with perf numbers

- **Component / trigger:** isaac_ros_dnn_inference (NVIDIA) — ROS 2 DNN inference nodes
- **AMD status:** `partial` — partial / in progress (nearest: AMD ROS 2 Perception Node accelerated application)
- **Who is blocked:** ROS 2 developers who need a drop-in accelerated inference node on AMD
- **Action:** Release ROS 2 inference nodes over ONNX Runtime EPs with a published benchmark table
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.crn.com/news/ai/2026/amd-advancing-ai-2026-top-news-on-ai-chips-cpus-robotics
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 54] No GPU TSDF/ESDF volumetric reconstruction library with a ROCm backend

- **Component / trigger:** nvblox (NVIDIA) — GPU TSDF/ESDF 3D reconstruction library
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Navigation and manipulation stacks needing dense 3D costmaps on AMD
- **Action:** Port the Apache-2.0 nvblox core kernels to HIP and land a ROCm CI job
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://github.com/nvidia-isaac/nvblox
- **Component ref:** https://github.com/nvidia-isaac/nvblox

#### [P0 · 54] No shipping AMR perception reference workflow; the AMD equivalent is announced but not yet generally available

- **Component / trigger:** isaac_perceptor (NVIDIA) — AMR perception reference workflow
- **AMD status:** `partial` — partial / in progress (nearest: AMD Robotics Software Suite and Kria AI Robotics Developer Platform, sampling with GA in Q4 2026)
- **Who is blocked:** AMR OEMs choosing a compute platform before Q4 2026
- **Action:** Release an early-access AMR perception reference pipeline with the Nav2 integration already benchmarked by OpenNav
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 54] No ROS 2 runtime that deploys trained RL/IL policies onto real robots on AMD

- **Component / trigger:** isaac_ros_deploy (NVIDIA) — Trained policy deployment runtime
- **AMD status:** `partial` — partial / in progress (nearest: ONNX Runtime MIGraphX and Vitis AI execution providers for policy inference)
- **Who is blocked:** Sim-to-real teams moving learned policies to AMD edge compute
- **Action:** Ship a policy-serving ROS 2 node with ONNX/MIGraphX backend and documented control-loop latency
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://onnxruntime.ai/docs/execution-providers/MIGraphX-ExecutionProvider.html
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 54] No XR/VR demonstration-capture teleoperation stack wired into ROS 2 on AMD

- **Component / trigger:** isaac_ros_teleop (NVIDIA) — XR teleoperation ROS 2 stack
- **AMD status:** `partial` — partial / in progress (nearest: LeRobot leader-follower teleoperation validated on ROCm (AMD ROCm blog), no XR or ROS 2 teleop packages)
- **Who is blocked:** Teams collecting manipulation demonstration data on AMD GPUs and Kria boards
- **Action:** Publish an OpenXR-to-ROS 2 teleop package on top of the already-working LeRobot ROCm teleop path
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://rocm.blogs.amd.com/artificial-intelligence/rocm-blogsblogsartificial-in/README.html
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 54] No AMD-accelerated GStreamer plugin suite or video analytics pipeline SDK layered above raw decode

- **Component / trigger:** DeepStream SDK (NVIDIA) — Video analytics streaming pipelines
- **AMD status:** `partial` — partial / in progress (nearest: rocDecode and rocJPEG expose VCN hardware decode with VA-API and HIP interop, decode only)
- **Who is blocked:** Multi-camera video analytics and robot vision application builders on Radeon and Instinct
- **Action:** Ship a supported set of ROCm GStreamer elements chaining decode, inference and tracking as a reference pipeline
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 3 · confidence high
- **Evidence:** https://rocm.docs.amd.com/projects/rocDecode/en/latest/index.html
- **Component ref:** https://developer.nvidia.com/deepstream-sdk

#### [P0 · 54] No ROS 2 utility and telemetry packages exposing power, thermal, NPU and iGPU load on AMD embedded SoCs

- **Component / trigger:** isaac_ros_jetson (NVIDIA) — Jetson support ROS 2 packages
- **AMD status:** `partial` — partial / in progress (nearest: AMD Kria AI Robotics Developer Platform and Robotics Software Suite provide ROS 2 board support)
- **Who is blocked:** Kria and Ryzen AI Embedded robot integrators doing field diagnostics and thermal budgeting
- **Action:** Publish a rocm-smi and XRT backed ROS 2 diagnostics node inside the Robotics Software Suite
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 54] No AMD accelerated point cloud primitive library equivalent to cuPCL for voxel filter ICP segmentation and normals

- **Component / trigger:** perception_pcl (OSS) — Point cloud message and filter integration
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Mobile robot and 3D perception stacks that bottleneck on CPU PCL filters in the ROS 2 point cloud path
- **Action:** Port the four hottest PCL kernels voxel grid passthrough NDT and ICP to HIP and expose them behind perception_pcl nodelet APIs
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://github.com/ros-perception/perception_pcl
- **Component ref:** https://github.com/ros-perception/perception_pcl

#### [P0 · 54] ONNX Runtime ROCm EP deprecated, fragmenting AMD's inference path with no recommended default

- **Component / trigger:** ONNX Runtime (Microsoft) — Cross-hardware neural network inference
- **AMD status:** `partial` — partial / in progress (nearest: MIGraphX EP / DirectML / Vitis AI VOE)
- **Who is blocked:** every ONNX-based robotics inference deployment on AMD
- **Action:** Publish an AMD-recommended inference-path decision tree before the fragmentation compounds downstream
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-16
- **Component ref:** https://github.com/microsoft/onnxruntime

#### [P0 · 54] Autoware perception nodes depend on CUDA/cuDNN/TensorRT with no ROCm or MIGraphX inference backend

- **Component / trigger:** Autoware (Autoware Foundation) — Full autonomous driving reference stack
- **AMD status:** `partial` — partial / in progress (nearest: CPU-only Autoware install path plus AMD Instinct autonomous-driving training blog)
- **Who is blocked:** AV and AMR integrators wanting an AMD reference autonomy stack
- **Action:** Add a MIGraphX/ONNX Runtime ROCm execution provider option to tensorrt_yolox and the CUDA pointcloud preprocessors
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://docs.autoware.org/main/installation/autoware/source-installation/
- **Component ref:** https://github.com/autowarefoundation/autoware

#### [P0 · 36] Multi-framework serving on AMD is datacenter-only with no embedded robot target

- **Component / trigger:** Triton Inference Server (NVIDIA) — Multi-framework model serving
- **AMD status:** `partial` — partial / in progress (nearest: Triton Inference Server with vLLM and ONNX Runtime backends on ROCm)
- **Who is blocked:** Fleet and edge serving teams deploying models onto robot compute
- **Action:** Publish a Triton or vLLM serving image validated on X100 and Kria class hardware
- **Scores:** openness 2 · fit 3 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://rocm.blogs.amd.com/blog/2025.html
- **Component ref:** https://developer.nvidia.com/embedded/jetpack

#### [P0 · 36] No ROS 2 node publishing GPU-reconstructed 3D costmaps into Nav2 on AMD

- **Component / trigger:** isaac_ros_nvblox (NVIDIA) — ROS 2 3D reconstruction costmap
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Nav2 users on Kria/Ryzen AI who want 3D obstacle avoidance
- **Action:** After a HIP TSDF core exists wrap it as a Nav2 costmap layer plugin
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://developer.nvidia.com/isaac/ros
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 36] No packaged learned stereo disparity ROS 2 node tuned for AMD iGPU or NPU

- **Component / trigger:** isaac_ros_dnn_stereo_depth (NVIDIA) — Learned stereo disparity estimation
- **AMD status:** `partial` — partial / in progress (nearest: AMD ROS 2 Perception Node plus MIGraphX/Vitis AI ONNX inference)
- **Who is blocked:** Stereo-camera robots on Kria and Ryzen AI Embedded
- **Action:** Ship a reference stereo disparity ONNX pipeline in the Robotics Software Suite with published Hz numbers
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-robotics-partner-network/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 36] Hardware video codec exists on AMD but no ROS 2 encode/decode nodes wrapping it

- **Component / trigger:** isaac_ros_compression (NVIDIA) — GPU sensor data compression
- **AMD status:** `partial` — partial / in progress (nearest: AMD Advanced Media Framework and VA-API hardware H.264/HEVC/AV1 encode-decode)
- **Who is blocked:** Robots streaming or recording multi-camera rigs over constrained links
- **Action:** Wrap AMF/VA-API in ROS 2 image_transport encoder and decoder nodes and upstream them
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://github.com/GPUOpen-LibrariesAndSDKs/AMF
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 36] AMD edge inference is split across three toolchains Ryzen AI Vitis AI and MIGraphX with no single OpenVINO-style CPU iGPU NPU device selector

- **Component / trigger:** OpenVINO (Intel) — Edge CPU/iGPU/NPU inference toolkit
- **AMD status:** `partial` — partial / in progress (nearest: AMD Ryzen AI Software with ONNX Runtime Vitis AI EP for NPU plus MIGraphX EP for Radeon)
- **Who is blocked:** Embedded robotics integrators who want one model artifact that retargets across AMD CPU iGPU and NPU without rebuilds
- **Action:** Publish one unified device-string API over the Vitis AI and MIGraphX execution providers with a single quantization flow
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://github.com/openvinotoolkit/openvino
- **Component ref:** https://github.com/openvinotoolkit/openvino

#### [P0 · 36] No HIP/ROCm backend for PCL GPU modules so accelerated filtering and segmentation stays CUDA-only

- **Component / trigger:** PCL (OSS) — Point cloud filtering and segmentation
- **AMD status:** `partial` — partial / in progress (nearest: PCL CPU build on EPYC/Ryzen plus AMD ROS 2 Perception Node)
- **Who is blocked:** Perception teams porting lidar pipelines off Jetson/Isaac to AMD edge parts
- **Action:** Port the pcl_gpu octree, segmentation and surface kernels to HIP and upstream as an optional PCL backend
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://pointclouds.org/
- **Component ref:** https://pointclouds.org/

#### [P0 · 36] OpenCV cudaarithm/cudaimgproc module family has no HIP equivalent so GPU CV ops silently fall back to CPU on AMD

- **Component / trigger:** OpenCV (OSS) — Classical and DNN computer vision ops
- **AMD status:** `partial` — partial / in progress (nearest: OpenCV OpenCL T-API on Radeon/Instinct plus AMD MIVisionX and rocAL primitives)
- **Who is blocked:** Every ROS 2 perception node and VLA data pipeline that assumes cv::cuda
- **Action:** Ship a hipified opencv_contrib cuda-module build in the ROCm robotics container and gate it in CI
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** corpus:rocmblogsamdcom-3f0bd016ae.txt
- **Component ref:** https://github.com/opencv/opencv

#### [P1 · 27] No ROCm-accelerated ROS 2 image preprocessing pipeline for rectify resize and color convert

- **Component / trigger:** isaac_ros_image_pipeline (NVIDIA) — GPU camera image preprocessing
- **AMD status:** `partial` — partial / in progress (nearest: Kria accelerated apps and Vitis Vision Library on PL)
- **Who is blocked:** Every camera-based ROS 2 stack on AMD falls back to CPU image_proc
- **Action:** Port image_proc rectify and resize to ROCm and publish per-node frame rates
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 1 · confidence low
- **Evidence:** https://www.cnx-software.com/2022/05/18/349-amd-kria-kr260-robotics-starter-kit-takes-on-nvidia-jetson-agx-xavier-devkit/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 27] No GPU-accelerated visual-inertial odometry or SLAM on ROCm

- **Component / trigger:** isaac_ros_visual_slam (NVIDIA) — ROS 2 visual SLAM odometry
- **AMD status:** `community` — community-maintained only (nearest: ORB-SLAM3 and RTAB-Map running CPU-side on AMD hosts)
- **Who is blocked:** Mobile robots and drones needing high-rate odometry without a CPU budget blowout
- **Action:** Accelerate one open VIO front end on ROCm and publish accuracy and rate against cuVSLAM
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 1 · confidence low
- **Evidence:** https://developer.nvidia.com/isaac/ros
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 27] No GPU-accelerated visual SLAM library on ROCm or Ryzen AI

- **Component / trigger:** cuVSLAM (NVIDIA) — CUDA visual SLAM library
- **AMD status:** `none` — no AMD path
- **Who is blocked:** AMR and drone teams needing metric VO/VSLAM on AMD edge silicon
- **Action:** Fund a HIP/ROCm port or ROCm-optimized build of an open VSLAM core and publish a ROS 2 wrapper
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://developer.nvidia.com/isaac/ros
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC/repositories

#### [P1 · 24] No humanoid teleoperation and whole-body-control bringup package on AMD

- **Component / trigger:** isaac_ros_physical_ai (NVIDIA) — Humanoid teleop and WBC bringup
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Humanoid teams needing a teleop-to-policy data collection loop on AMD hardware
- **Action:** Fund a LeRobot-style teleop plus WBC reference on a public humanoid using ROCm
- **Scores:** openness 2 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://developer.nvidia.com/isaac/ros
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 24] No AMD reference AMR robot platform packages; the Kria dev platform is a compute board not a whole-robot reference

- **Component / trigger:** nova_carter (NVIDIA) — Reference AMR platform packages
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Developers who want a Nova-Carter-class turnkey robot to benchmark against
- **Action:** Partner with one ODM in the Robotics Partner Network on an open reference AMR with published URDF and bringup
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 24] No published common ROS 2 build, dev-container and CI test harness for AMD targets

- **Component / trigger:** isaac_ros_common (NVIDIA) — Common build and test infrastructure
- **AMD status:** `partial` — partial / in progress (nearest: AMD Robotics Software Suite built on ROCm and ROS 2, plus ROCm and Kria dev containers)
- **Who is blocked:** Anyone trying to reproduce an AMD robotics build across Kria, Ryzen AI and Instinct
- **Action:** Open-source the Robotics Software Suite dev container and a ROS 2 CI template for AMD targets
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://nvidia-isaac-ros.github.io/repositories_and_packages/index.html

#### [P1 · 24] No AMD-maintained TVM ROCm backend or autotuning schedule database so ROCm targets lag CUDA in tuned kernels

- **Component / trigger:** Apache TVM (Apache) — Deep learning compiler and autotuner
- **AMD status:** `community` — community-maintained only (nearest: TVM ROCm and Vulkan targets plus AMD ROCm CI for MLC-LLM built on TVM Unity)
- **Who is blocked:** Edge robotics teams compiling perception models AOT for Ryzen AI and Radeon rather than serving them
- **Action:** Stand up a public AMD-hosted TVM ROCm CI runner and publish pre-tuned schedule logs for gfx1100 and gfx942
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://github.com/apache/tvm
- **Component ref:** https://github.com/apache/tvm

#### [P1 · 18] No AMD-maintained micro-ROS board support package for Zynq/Versal Cortex-R5 or MicroBlaze real-time cores

- **Component / trigger:** micro-ROS (OSS) — ROS 2 client stack for microcontrollers
- **AMD status:** `partial` — partial / in progress (nearest: AMD Kria SOM real-time cores plus Ryzen AI Embedded X100 running ROS 2 on Linux)
- **Who is blocked:** Safety-island and motor-control firmware teams on AMD adaptive SoCs who must hand-roll XRCE-DDS bring-up
- **Action:** Publish and upstream a micro-ROS BSP for the Kria KR260 R5 cores with a CI job in the micro-ROS build farm
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://newsroom.amd.com/news/aai-2026-robotics-partner-network/
- **Component ref:** https://micro.ros.org/

#### [P2 · 16] No validated reference sensor suite with time-synchronized multi-camera drivers and calibration on AMD

- **Component / trigger:** isaac_ros_nova (NVIDIA) — Reference sensor suite support
- **AMD status:** `partial` — partial / in progress (nearest: Kria AI robotics carrier card plus sensor and perception partners in the AMD Robotics Partner Network)
- **Who is blocked:** Integrators assembling camera/IMU/lidar rigs without a known-good reference
- **Action:** Publish a validated sensor bill-of-materials with drivers, sync and calibration tooling for the Kria carrier card
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-robotics-partner-network/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P2 · 12] No first-party ROS 2 CSI camera driver publishing directly into an accelerated buffer

- **Component / trigger:** isaac_ros_argus_camera (NVIDIA) — CSI camera ROS 2 driver
- **AMD status:** `partial` — partial / in progress (nearest: Kria MIPI CSI capture via PL with V4L2 and libcamera on KR260 and KV260)
- **Who is blocked:** Robot builders wiring MIPI sensors into ROS 2 on Kria or X100
- **Action:** Ship a supported ROS 2 CSI driver node for the Kria robotics platform
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://www.cnx-software.com/2022/05/18/349-amd-kria-kr260-robotics-starter-kit-takes-on-nvidia-jetson-agx-xavier-devkit/
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P2 · 12] No structure-from-motion mapping and visual relocalization stack on AMD silicon

- **Component / trigger:** isaac_ros_mapping_and_localization (NVIDIA) — Visual mapping and relocalization
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Teams building persistent visual maps for multi-session operation
- **Action:** Bundle an open SfM (COLMAP/hloc) ROCm build as a mapping reference in the Robotics Software Suite
- **Scores:** openness 1 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://developer.nvidia.com/isaac/ros
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P2 · 12] RTAB-Map optional acceleration paths assume OpenCV CUDA modules with no HIP or ROCm equivalent build

- **Component / trigger:** RTAB-Map (OSS) — RGB-D graph SLAM and appearance mapping
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Warehouse and service robot teams running RGB-D SLAM on AMD APUs who fall back to CPU-only odometry and dense depth
- **Action:** Provide a ROCm-enabled OpenCV container plus an rtabmap build flag validated on Ryzen AI Embedded X100
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://github.com/introlab/rtabmap
- **Component ref:** https://github.com/introlab/rtabmap

#### [P2 · 8] No GPU-accelerated global map-based relocalization package on AMD

- **Component / trigger:** isaac_ros_map_localization (NVIDIA) — Global map-based localization
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Fleet AMRs needing repeatable localization against a prior map
- **Action:** Validate an open CPU relocalizer (AMCL/lidar) on Kria first and document the accuracy gap
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://developer.nvidia.com/isaac/ros
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P3 · 2] No safety-certified automotive camera capture stack equivalent to SIPL

- **Component / trigger:** isaac_ros_sipl_camera (NVIDIA) — SIPL camera ROS 2 driver
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Automotive and safety-rated robot camera integrators
- **Action:** Scope whether Kria PL capture can be taken through a FuSa camera claim
- **Scores:** openness 1 · fit 2 · leverage 1 · evidence 1 · confidence low
- **Evidence:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

### L2 — Simulation, Physics & Motion Planning

*36 components checked · 22 gaps*

#### [P0 · 81] No AMD-backed GPU-resident massively parallel RL and IL environment framework

- **Component / trigger:** Isaac Lab (NVIDIA) — GPU-parallel robot learning framework
- **AMD status:** `community` — community-maintained only (nearest: MuJoCo MJX-JAX runs on AMD GPUs via XLA, plus Gazebo, neither maintained by AMD)
- **Who is blocked:** Reinforcement and imitation learning researchers wanting thousands of parallel envs on Instinct HBM
- **Action:** Fund and CI-validate MJX-JAX on ROCm and publish a parallel-environment RL training reference
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://mujoco.readthedocs.io/en/stable/mjx.html
- **Component ref:** https://developer.nvidia.com/isaac/lab

#### [P0 · 81] No GPU-resident rigid body and articulation solver maintained on ROCm, the open Newton engine depends on NVIDIA Warp

- **Component / trigger:** PhysX (NVIDIA) — Rigid body physics SDK
- **AMD status:** `community` — community-maintained only (nearest: MuJoCo and MJX-JAX on ROCm and Bullet on CPU; Newton and MJWarp are NVIDIA Warp and CUDA only)
- **Who is blocked:** Every simulator and RL stack that needs GPU physics on Instinct or Radeon
- **Action:** Contribute a HIP or Triton solver backend to Newton, or port Warp kernels, to break the CUDA dependency
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://www.linuxjournal.com/content/linux-foundation-welcomes-newton-next-open-physics-engine-robotics
- **Component ref:** https://github.com/NVIDIA-Omniverse/PhysX

#### [P0 · 81] Warp has no merged ROCm backend; AMD PRs are in flight but unlanded

- **Component / trigger:** Warp (NVIDIA) — GPU kernel Python DSL simulation
- **AMD status:** `partial` — partial / in progress (nearest: AMD-authored HIP/ROCm PRs #1770/#1865)
- **Who is blocked:** every downstream of Newton and MuJoCo-Warp
- **Action:** Resource PRs #1770/#1865 to completion and announce — cheapest action in the register
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-1
- **Component ref:** https://github.com/NVIDIA/warp

#### [P0 · 81] No real-capture-to-simulation neural reconstruction pipeline that feeds reconstructed scenes into a robot simulator

- **Component / trigger:** Omniverse NuRec (NVIDIA) — Neural reconstruction gaussian splat rendering
- **AMD status:** `partial` — partial / in progress (nearest: gsplat 3D Gaussian Splatting enabled and documented on ROCm in two AMD ROCm blog posts)
- **Who is blocked:** Teams building simulation scenes from real robot sensor captures on AMD
- **Action:** Publish a ROCm gsplat to Gazebo or MuJoCo scene export reference so captures become simulatable assets
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://rocm.blogs.amd.com/blog/2025.html
- **Component ref:** https://developer.nvidia.com/isaac/sim

#### [P0 · 81] Upstream perf investment has moved to MJX-Warp which is NVIDIA-only leaving the AMD path on the slower JAX branch

- **Component / trigger:** MuJoCo (Google DeepMind) — Contact-rich rigid body physics simulation
- **AMD status:** `partial` — partial / in progress (nearest: MJX-JAX on ROCm JAX runs MuJoCo on AMD GPUs; corpus shows MuJoCo policy work on Ryzen AI MAX+ 395)
- **Who is blocked:** Anyone doing large-scale parallel RL or sim-to-real on AMD GPUs
- **Action:** Fund an MJX-Warp-equivalent HIP/Triton backend or upstream ROCm kernels and publish MI300X env-steps/sec numbers
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** corpus:mujocoreadthedocsio-de76e51bc4.txt
- **Component ref:** https://github.com/google-deepmind/mujoco

#### [P0 · 81] AMD is technically engaged with Genesis but absent from its Robotics Partner Network

- **Component / trigger:** Genesis (Genesis-Embodied-AI) — Unified differentiable robotics simulation
- **AMD status:** `community` — community-maintained only (nearest: ROCm tutorial plus a joint arXiv paper)
- **Who is blocked:** AMD's visibility to Genesis-based robot programs
- **Action:** Enroll in the Genesis partner network (free) and publish an Eno-on-AMD reference guide before NVIDIA moves
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-2,GAP-8
- **Component ref:** https://github.com/Genesis-Embodied-AI/Genesis

#### [P0 · 81] ManiSkill lists GPU simulation as unsupported on AMD GPUs so the flagship parallel manipulation benchmark cannot run on ROCm

- **Component / trigger:** ManiSkill (Hillbot / UCSD) — GPU manipulation benchmark environments
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Robot-learning groups benchmarking policies; AMD has no comparable published env-throughput number
- **Action:** Get ManiSkill CPU-sim CI green on ROCm first, then sponsor a ROCm GPU-sim backend via its SAPIEN dependency
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://github.com/haosulab/ManiSkill
- **Component ref:** https://github.com/haosulab/ManiSkill

#### [P0 · 81] No ROCm-accelerated MoveIt planner plugin; AMD only runs the CPU planners while cuRobo gives NVIDIA order-of-magnitude planning latency wins

- **Component / trigger:** MoveIt 2 (PickNik / OSS) — Manipulation motion planning framework
- **AMD status:** `partial` — partial / in progress (nearest: MoveIt 2 explicitly supported by AMD Kria AI Solutions and the AMD Robotics Software Suite)
- **Who is blocked:** Industrial arm and manipulation vendors choosing compute on planning latency
- **Action:** Ship a HIP/Triton batched collision-checking and trajectory-optimization MoveIt plugin as a cuRobo answer
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://moveit.ai/

#### [P0 · 54] Newton physics has no validated ROCm backend

- **Component / trigger:** Newton (NVIDIA) — GPU differentiable physics engine
- **AMD status:** `partial` — partial / in progress (nearest: ROCm path via in-flight Warp PRs)
- **Who is blocked:** Boston Dynamics, Agility, Figure AI, Toyota, Skild, Samsung (Newton adopters)
- **Action:** Land the Warp ROCm PRs then publish a validated Newton-on-MI300X configuration
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-1
- **Component ref:** https://github.com/newton-physics/newton

#### [P0 · 36] SAPIEN GPU physics is PhysX/CUDA so photoreal parallel sensor rendering degrades to CPU on AMD

- **Component / trigger:** SAPIEN (Hillbot / UCSD) — Simulation with realistic sensor rendering
- **AMD status:** `partial` — partial / in progress (nearest: CPU simulation and rendering fallback only; no ROCm GPU physics backend)
- **Who is blocked:** Manipulation researchers needing photoreal RGB-D sim on AMD workstations
- **Action:** Prototype a Vulkan-compute or HIP rigid-body backend for SAPIEN and validate the Vulkan renderer path on Radeon
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://github.com/haosulab/ManiSkill
- **Component ref:** https://sapien.ucsd.edu

#### [P0 · 36] No AMD-validated Brax build, wheel or throughput benchmark; portability is inherited from XLA not tested by AMD

- **Component / trigger:** Brax (Google) — Massively parallel differentiable physics
- **AMD status:** `community` — community-maintained only (nearest: Brax on ROCm JAX via its mujoco-mjx dependency which supports AMD GPUs)
- **Who is blocked:** JAX-based RL users evaluating AMD as a training substrate
- **Action:** Add a Brax smoke test and env-steps/sec benchmark to the ROCm JAX CI matrix
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** corpus:mujocoreadthedocsio-de76e51bc4.txt
- **Component ref:** https://github.com/google/brax

#### [P0 · 36] No AMD equivalent of nvblox/cuVSLAM costmap and localization plugins, so GPU-accelerated navigation layers remain NVIDIA-only

- **Component / trigger:** Nav2 (Open Navigation) — Mobile robot navigation and behavior trees
- **AMD status:** `partial` — partial / in progress (nearest: Nav2 runs unmodified on AMD ROS 2 hosts alongside the AMD ROS 2 Perception Node)
- **Who is blocked:** AMR and mobile-robot builders comparing Kria/Ryzen against Jetson on navigation stack completeness
- **Action:** Publish a ROCm or Vitis accelerated costmap-layer and 3D reconstruction plugin for Nav2
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** corpus:nvidia-isaac-rosgithubio-b4d3888a39.txt
- **Component ref:** https://nav2.org/

#### [P0 · 36] Differentiable physics is incomplete on every backend including CUDA — an open architectural question, not a port

- **Component / trigger:** (whitespace) production differentiable physics (NONE) — differentiable physics usable for policy gradient training
- **AMD status:** `none` — no AMD path (nearest: AMD JAX/XLA on ROCm is a co-architect position)
- **Who is blocked:** robot learning researchers needing analytic gradients
- **Action:** Approach DeepMind researchers for co-authorship on the ROCm/XLA differentiable path — this is co-architecture, not catch-up
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-7
- **Component ref:** derived:grid-sweep

#### [P1 · 24] No AMD-side equivalent to Isaac Sim as an integrated platform

- **Component / trigger:** Isaac Sim (NVIDIA) — OpenUSD robotics simulator
- **AMD status:** `none` — no AMD path (nearest: Genesis + open renderer covers a slice only)
- **Who is blocked:** teams wanting one bundled authoring+physics+rendering tool
- **Action:** Scope whether Genesis plus an open rendering stack can be positioned as an Isaac Sim equivalent in 12 months
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-15
- **Component ref:** https://developer.nvidia.com/isaac/sim

#### [P1 · 24] No AMD-validated MuJoCo ros2_control bridge with GPU-rendered RGB-D and lidar sensor plugins

- **Component / trigger:** mujoco_ros2_control (NVIDIA) — MuJoCo ros2_control simulation interface
- **AMD status:** `community` — community-maintained only (nearest: Upstream community mujoco_ros2_control runs on AMD CPUs; MuJoCo is Apache 2.0 and hardware agnostic)
- **Who is blocked:** ROS 2 teams doing hardware-in-the-loop and controller simulation on AMD
- **Action:** Add mujoco_ros2_control to AMD Robotics Software Suite CI with ROCm-backed sensor rendering
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://github.com/google-deepmind/mujoco
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 24] No AMD-published versioned simulation-plus-ROS 2 reference workspace or container pinning known-good versions

- **Component / trigger:** IsaacSim-ros_workspaces (NVIDIA) — Sim to ROS 2 bridge workspaces
- **AMD status:** `community` — community-maintained only (nearest: Gazebo ros_gz bridge and community MuJoCo ROS 2 wrappers, hardware agnostic but not AMD maintained)
- **Who is blocked:** ROS 2 developers standing up simulation CI on AMD hardware
- **Action:** Publish a versioned ROCm simulation and ROS 2 workspace container inside the Robotics Software Suite
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-kria-robotics-dev-platform/
- **Component ref:** https://github.com/isaac-sim/IsaacSim-ros_workspaces

#### [P1 · 24] No AMD GPU numbers anywhere in MJX/Warp sim-to-real benchmark literature

- **Component / trigger:** MJX (Google DeepMind) — Batched GPU physics for RL rollouts
- **AMD status:** `community` — community-maintained only (nearest: MJX runs on ROCm through JAX)
- **Who is blocked:** researchers choosing simulation hardware
- **Action:** Publish MJX and Warp throughput benchmarks on MI300X as a ROCm blog post
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-18
- **Component ref:** https://github.com/google-deepmind/mujoco

#### [P1 · 24] Nothing outside Isaac Sim bundles authoring plus physics plus rendering in one platform

- **Component / trigger:** (whitespace) integrated open sim platform (NONE) — integrated authoring + physics + rendering simulation platform (non-NVIDIA)
- **AMD status:** `none` — no AMD path (nearest: Genesis, MuJoCo, Gazebo each cover a slice)
- **Who is blocked:** teams evaluating a full simulation platform rather than a library
- **Action:** Decide explicitly whether to assemble a bundle or stay library-first; do not drift into it
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-15
- **Component ref:** derived:grid-sweep

#### [P1 · 18] SWAGGER mandates CUDA 12.5 so occupancy-grid waypoint graph generation has no AMD GPU path

- **Component / trigger:** SWAGGER (NVIDIA) — Sparse waypoint graph route planning
- **AMD status:** `none` — no AMD path (nearest: Nav2 CPU route planning only; no ROCm sparse waypoint graph generator)
- **Who is blocked:** AMR and warehouse fleet route planning teams standardizing on AMD compute
- **Action:** Port the SWAGGER graph kernels to HIP or contribute a CPU and ROCm backend upstream
- **Scores:** openness 3 · fit 2 · leverage 1 · evidence 3 · confidence med
- **Evidence:** https://github.com/nvidia-isaac/SWAGGER
- **Component ref:** https://github.com/nvidia-isaac/SWAGGER

#### [P2 · 16] No composable simulation-based policy evaluation harness usable on AMD

- **Component / trigger:** Isaac Lab-Arena (NVIDIA) — Composable policy evaluation in simulation
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Teams needing reproducible VLA policy regression scoring before deployment
- **Action:** Adapt an open evaluation harness to LeRobot plus MuJoCo on ROCm and publish it as a reference
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://newsroom.amd.com/news/aai-2026-robotics-partner-network/
- **Component ref:** https://github.com/isaac-sim/IsaacLab-Arena

#### [P2 · 12] No open extensible 3D and digital-twin application runtime AMD can build on without Omniverse Enterprise licensing

- **Component / trigger:** Omniverse Kit (NVIDIA) — Extensible 3D application runtime
- **AMD status:** `none` — no AMD path
- **Who is blocked:** ISVs and simulation partners building digital twin applications on AMD platforms
- **Action:** Back an open runtime such as O3DE or Gazebo with ROCm rendering as a declared Omniverse Kit alternative
- **Scores:** openness 1 · fit 2 · leverage 2 · evidence 3 · confidence high
- **Evidence:** https://github.com/NVIDIA-Omniverse/kit-app-template
- **Component ref:** https://github.com/NVIDIA-Omniverse/kit-app-template

#### [P2 · 8] No medical or surgical robot sensor-physics simulation reference on AMD despite AMD presence in medical imaging silicon

- **Component / trigger:** Isaac for Healthcare (i4h-physics-simulation) (NVIDIA) — Medical robot sensor physics simulation
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Medical robotics ISVs already shipping on AMD embedded imaging platforms
- **Action:** Partner one surgical-simulation ISV through the AMD Robotics Partner Network on a ROCm ultrasound or endoscope sensor sim reference
- **Scores:** openness 2 · fit 2 · leverage 1 · evidence 2 · confidence med
- **Evidence:** https://github.com/isaac-for-healthcare/i4h-physics-simulation
- **Component ref:** https://github.com/isaac-for-healthcare/i4h-physics-simulation

### L3 — Models, Policies & Data (VLA, foundation models, datasets)

*35 components checked · 33 gaps*

#### [P0 · 81] Upstream openpi JAX/CUDA training stack has no ROCm build so AMD users can only reach pi0 through the LeRobot re-implementation

- **Component / trigger:** openpi (Physical Intelligence) — Flow-matching VLA model and training code
- **AMD status:** `partial` — partial / in progress (nearest: Pi0 and Pi0.5 fine-tuning on MI300X plus edge inference on Ryzen AI GPUs via the LeRobot PyTorch port (ROCm edge-to-cloud robotics blog))
- **Who is blocked:** Teams wanting to reproduce or pretrain pi0/pi05 from the official Physical Intelligence repo on AMD silicon
- **Action:** Publish a ROCm-tested openpi container and upstream a ROCm install path plus CI job to Physical-Intelligence/openpi
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** corpus:rocmblogsamdcom-3f0bd016ae.txt
- **Component ref:** https://github.com/Physical-Intelligence/openpi

#### [P0 · 81] No AMD GPU in upstream LeRobot CI so ROCm-only breakages ship unnoticed (uint8 bilinear interpolate NotImplementedError in SmolVLA resize_with_pad)

- **Component / trigger:** SmolVLA (HuggingFace) — Compact VLA for low-cost hardware
- **AMD status:** `partial` — partial / in progress (nearest: SmolVLA training and inference on ROCm through LeRobot on MI300X and Ryzen AI (AMD ROCm blog, AMD Open Robotics Hackathon))
- **Who is blocked:** Every SmolVLA user on Radeon or Instinct hitting silent ROCm-only regressions between releases
- **Action:** Donate a gfx942 and gfx1100 runner to huggingface/lerobot CI and gate policy tests on it
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://github.com/huggingface/lerobot/issues/4205
- **Component ref:** https://huggingface.co/lerobot

#### [P0 · 81] No AMD model cards in the LeRobot hub — AMD is invisible at the developer callsite

- **Component / trigger:** LeRobot (HuggingFace) — Robot dataset format training and eval library
- **AMD status:** `community` — community-maintained only (nearest: pi0 and SmolVLA work on ROCm)
- **Who is blocked:** every LeRobot developer choosing hardware
- **Action:** Publish model cards; this is a documentation gap, not an engineering one
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-5
- **Component ref:** https://github.com/huggingface/lerobot

#### [P0 · 81] Zero published VLA inference Hz benchmarks on AMD silicon; the action-expert stage is memory-bound and unmeasured

- **Component / trigger:** (whitespace) vendor-neutral VLA Hz benchmark suite (NONE) — published VLA inference Hz benchmark on non-NVIDIA silicon
- **AMD status:** `none` — no AMD path
- **Who is blocked:** every buyer comparing edge inference hardware
- **Action:** Publish an official reproducible AMD VLA Hz benchmark — highest-visibility single gap-closer in L3
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-13
- **Component ref:** derived:grid-sweep

#### [P0 · 54] No AMD-runnable world foundation model path; Cosmos ships CUDA-optimized and there is no ROCm first-party equivalent

- **Component / trigger:** Cosmos 3 (NVIDIA) — World foundation model
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Everyone building physical-AI data engines and sim-to-real pipelines on AMD
- **Action:** Fund ROCm inference enablement for one open world foundation model and publish measured generation throughput on MI300X
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Robotics-Leaders-Take-Physical-AI-to-the-Real-World/
- **Component ref:** https://developer.nvidia.com/cosmos

#### [P0 · 54] No AMD-validated OpenVLA training or inference recipe, so the most-cited open VLA has no published gfx942/gfx1100 numbers

- **Component / trigger:** OpenVLA (Stanford / OSS) — Open vision-language-action policy model
- **AMD status:** `community` — community-maintained only (nearest: Runs via PyTorch on ROCm; AMD has published VLA fine-tuning on MI300X for Pi0, Pi0.5, SmolVLA and ACT but not OpenVLA)
- **Who is blocked:** Researchers reproducing OpenVLA baselines who default to NVIDIA for the reference config
- **Action:** Add OpenVLA-7B fine-tune and inference-Hz runs to the existing ROCm LeRobot/VLA CI and blog the numbers
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** corpus:rocmblogsamdcom-3f0bd016ae.txt
- **Component ref:** https://github.com/openvla/openvla

#### [P0 · 54] No AMD-published ACT throughput or bimanual teleop reference bring-up, so AMD-vs-Jetson comparisons for ALOHA-class rigs are guesswork

- **Component / trigger:** ACT (Stanford) — Transformer imitation policy for bimanual tasks
- **AMD status:** `partial` — partial / in progress (nearest: ACT policy training and inference on ROCm via LeRobot; independently replicated on Ryzen AI MAX+ 395 by the Datawhale Every Embodied project)
- **Who is blocked:** Bimanual imitation-learning teams sizing AMD edge parts against Jetson for teleop data collection
- **Action:** Publish ACT train and inference Hz numbers for Ryzen AI MAX and MI300X alongside a reference bimanual arm bring-up guide
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://datawhalechina.github.io/hello-rocm/05-amd-yes/every-embodied
- **Component ref:** https://github.com/tonyzhaozh/act

#### [P0 · 54] No AMD-validated recipe for RLDS-format Open X-Embodiment-scale cross-embodiment pretraining on ROCm

- **Component / trigger:** Open X-Embodiment (Open X-Embodiment Collaboration) — Aggregated cross-embodiment demonstration corpus
- **AMD status:** `partial` — partial / in progress (nearest: MI300X plus LeRobot training pipeline exists, but AMD recipes are demonstrated only on small community LeRobot datasets, not on OXE-scale corpora)
- **Who is blocked:** Teams that want to pretrain cross-embodiment VLAs on Instinct instead of renting A100/H100 capacity
- **Action:** Publish an OXE to LeRobotDataset conversion plus a multi-GPU MI300X pretraining reference on ROCm blogs
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** corpus:rocmblogsamdcom-3f0bd016ae.txt
- **Component ref:** https://robotics-transformer-x.github.io/

#### [P0 · 36] No GPU-accelerated video and episode dataset curation pipeline on ROCm despite AMD shipping VCN decode hardware

- **Component / trigger:** Cosmos Curator (NVIDIA) — Video dataset curation pipeline
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Robot data teams filtering and scoring large demonstration and video corpora
- **Action:** Build a rocDecode-backed curation reference doing dedup, captioning and quality filtering over LeRobot datasets
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.roboticscenter.ai/state-of-robotics-2026
- **Component ref:** https://github.com/NVIDIA/cosmos-curator

#### [P0 · 36] No cross-embodiment navigation policy that can be trained without Isaac Sim

- **Component / trigger:** COMPASS (NVIDIA) — Vision-based mobility foundation model
- **AMD status:** `none` — no AMD path
- **Who is blocked:** AMR and mobility teams training navigation policies on AMD
- **Action:** Reproduce COMPASS inference on ROCm from the Apache-2.0 release and document a non-Isaac-Sim training substitute
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://github.com/NVlabs/COMPASS
- **Component ref:** https://developer.nvidia.com/isaac

#### [P0 · 36] No AMD-hosted or AMD-validated open robotics dataset; the data flywheel accrues entirely to NVIDIA

- **Component / trigger:** NVIDIA Physical AI Dataset (NVIDIA) — Open robotics training dataset
- **AMD status:** `partial` — partial / in progress (nearest: AMD can consume the Hugging Face datasets but ships no first-party robotics dataset)
- **Who is blocked:** policy training teams choosing a compute vendor by data availability
- **Action:** Publish a ROCm-verified loader and training recipe over the open Physical AI datasets and co-release one AMD-collected dataset
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://developer.nvidia.com/isaac/sim
- **Component ref:** https://developer.nvidia.com/isaac/sim

#### [P0 · 36] No vendor-neutral policy benchmark suite runnable on AMD; evaluation standards are being set inside Isaac Sim

- **Component / trigger:** IsaacLabEvalTasks (NVIDIA) — Policy benchmarking task suite
- **AMD status:** `none` — no AMD path
- **Who is blocked:** anyone needing comparable VLA and manipulation policy scores across vendors
- **Action:** Port a subset of the Apache-2.0 eval tasks to a simulator with a ROCm backend so AMD numbers are comparable
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://github.com/isaac-sim/IsaacLabEvalTasks
- **Component ref:** https://github.com/isaac-sim/IsaacLabEvalTasks

#### [P0 · 36] No AMD validation or latency reference for iterative denoising visuomotor policies where the multi-step denoise loop dominates control-loop latency

- **Component / trigger:** Diffusion Policy (Columbia / Stanford) — Denoising diffusion visuomotor policy
- **AMD status:** `community` — community-maintained only (nearest: Runs as stock PyTorch through the LeRobot diffusion policy implementation on ROCm; no AMD-published validation or perf reference)
- **Who is blocked:** Manipulation teams needing real-time diffusion policy inference on AMD edge silicon
- **Action:** Add diffusion policy to the ROCm LeRobot example matrix with per-denoise-step latency numbers
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://github.com/huggingface/lerobot
- **Component ref:** https://github.com/real-stanford/diffusion_policy

#### [P0 · 36] RLDS ingest is bound to tf.data and TFDS whose ROCm support is second-class next to the PyTorch path AMD actually invests in

- **Component / trigger:** RLDS (Google Research) — Standard episodic robot dataset format
- **AMD status:** `partial` — partial / in progress (nearest: TensorFlow-ROCm builds exist and are used in ROCm blog tutorials, but no robotics TFDS/RLDS ingest path is tested or documented)
- **Who is blocked:** Anyone consuming Open X-Embodiment or DROID RLDS shards on AMD hardware
- **Action:** Ship and test an rlds-to-LeRobotDataset converter in the ROCm robotics examples repo
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://rocm.blogs.amd.com/blog/author.html
- **Component ref:** https://github.com/google-research/rlds

#### [P0 · 36] No public non-NVIDIA VLA training case study exists; the training-cluster market defaults to DGX/HGX in every public writeup

- **Component / trigger:** (whitespace) non-NVIDIA VLA training case study (NONE) — published foundation-model training case study on non-NVIDIA cluster
- **AMD status:** `none` — no AMD path (nearest: MI300X 192GB HBM3 suits the memory-bound regime)
- **Who is blocked:** buyers sizing VLA training infrastructure
- **Action:** Publish a VLA foundation model trained on an MI300X cluster as a case study
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-24
- **Component ref:** derived:grid-sweep

#### [P1 · 27] No end-to-end synthetic data generation pipeline reference on ROCm; SDG workflows assume Omniverse and Cosmos

- **Component / trigger:** physical-ai-data-factory (NVIDIA) — Synthetic data generation workflows
- **AMD status:** `none` — no AMD path
- **Who is blocked:** teams needing training data without Omniverse licences or NVIDIA render farms
- **Action:** Publish a reference SDG pipeline on ROCm combining Genesis or Blender rendering with a ROCm diffusion augmentation step
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://github.com/NVIDIA/physical-ai-data-factory
- **Component ref:** https://github.com/NVIDIA/physical-ai-data-factory

#### [P1 · 24] No world-model-driven synthetic trajectory generation path on ROCm

- **Component / trigger:** GR00T-Dreams (DreamGen) (NVIDIA) — World-model synthetic trajectory generation
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Teams trying to scale demonstration data beyond human teleoperation capture
- **Action:** Validate one open video world model on ROCm and publish a trajectory-generation recipe with throughput numbers
- **Scores:** openness 2 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://github.com/NVIDIA/GR00T-Dreams
- **Component ref:** https://github.com/NVIDIA/GR00T-Dreams

#### [P1 · 24] No humanoid loco-manipulation training workflow that runs outside Isaac Lab

- **Component / trigger:** WBC-AGILE (NVIDIA) — Humanoid loco-manipulation training workflow
- **AMD status:** `none` — no AMD path
- **Who is blocked:** humanoid teams needing a reproducible whole-body-control training recipe on AMD
- **Action:** Reproduce a WBC-style loco-manipulation curriculum on a ROCm-capable simulator and publish the config
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://github.com/nvidia-isaac/WBC-AGILE
- **Component ref:** https://github.com/nvidia-isaac/WBC-AGILE

#### [P1 · 24] No AMD reference for consuming the DROID RLDS distribution or for Franka-platform data collection on AMD hosts

- **Component / trigger:** DROID (DROID Collaboration) — Large in-the-wild manipulation dataset
- **AMD status:** `partial` — partial / in progress (nearest: Data itself is vendor-neutral and downloadable; AMD training path is LeRobot on ROCm but no DROID-specific ingest or finetune recipe is published)
- **Who is blocked:** Labs standardising on DROID-style Franka teleop rigs while running AMD compute
- **Action:** Add a DROID subset finetune walkthrough to the ROCm robotics example set using the LeRobot converter
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://droid-dataset.github.io/
- **Component ref:** https://droid-dataset.github.io/

#### [P1 · 24] No vendor-neutral teleop data-collection path; the dataset format is neutral but the tooling is not

- **Component / trigger:** (whitespace) vendor-neutral teleop data collection (NONE) — open teleop data-collection path not tied to one vendor's stack
- **AMD status:** `none` — no AMD path
- **Who is blocked:** teams collecting demonstrations without committing to one vendor
- **Action:** Publish a ROCm-native collection path
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-23
- **Component ref:** derived:grid-sweep

#### [P1 · 18] AMD covers quantize and compile but has no task-level fine-tuning or post-training toolkit for vision models

- **Component / trigger:** TAO (NVIDIA) — Vision model post-training toolkit
- **AMD status:** `partial` — partial / in progress (nearest: AMD Quark plus the Vitis AI quantizer/compiler and Ryzen AI ONNX flow)
- **Who is blocked:** edge vision developers doing transfer learning on Kria and Ryzen AI Embedded
- **Action:** Extend Quark and Vitis AI with fine-tuning recipes for a handful of detection and segmentation backbones
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://onnxruntime.ai/docs/execution-providers/Vitis-AI-ExecutionProvider.html
- **Component ref:** https://developer.nvidia.com/tao-toolkit

#### [P2 · 16] GR00T fine-tuning workflow is documented and supported only on NVIDIA hardware

- **Component / trigger:** Isaac GR00T N1.7 (NVIDIA) — Humanoid VLA foundation model
- **AMD status:** `none` — no AMD path (nearest: smaller open VLAs (SmolVLA, pi0, ACT) run on ROCm)
- **Who is blocked:** teams standardizing on the largest open humanoid policy
- **Action:** Scope porting only the GR00T fine-tuning recipe, not the full Isaac Lab stack
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-22
- **Component ref:** https://github.com/NVIDIA/Isaac-GR00T

#### [P2 · 16] No AMD-side domain-randomized synthetic data generator

- **Component / trigger:** Isaac Sim Replicator (NVIDIA) — Domain-randomized synthetic data generation
- **AMD status:** `none` — no AMD path
- **Who is blocked:** sim-to-real teams generating training data
- **Action:** Fold into the end-to-end synthetic data pipeline reference rather than building standalone
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-4
- **Component ref:** https://developer.nvidia.com/isaac/sim

#### [P2 · 16] Isaac Teleop LeRobot integration implicitly steers data collection onto NVIDIA compute

- **Component / trigger:** Isaac TeleOp / IsaacTeleop (NVIDIA) — Teleop demonstration data collection
- **AMD status:** `none` — no AMD path
- **Who is blocked:** teams collecting teleop demonstrations
- **Action:** Document or publish a ROCm-native teleop data-collection path; the dataset format is already neutral
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-23
- **Component ref:** https://github.com/NVIDIA/IsaacTeleop

#### [P2 · 16] No packaged, ready-to-run humanoid control policies distributed for AMD compute

- **Component / trigger:** isaac_ros_learned_policies (NVIDIA) — Learned humanoid control policies
- **AMD status:** `none` — no AMD path
- **Who is blocked:** humanoid developers wanting a working locomotion baseline out of the box
- **Action:** Republish one open humanoid locomotion checkpoint with a ROCm inference container and a ROS 2 wrapper
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** corpus:nvidia-isaac-rosgithubio-b4d3888a39.txt
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P2 · 16] RT-1-X TF/JAX checkpoints have no verified ROCm inference path and RT-2-X was never released at all

- **Component / trigger:** RT-1-X / RT-2-X (Google DeepMind) — Cross-embodiment transformer control models
- **AMD status:** `unknown` — UNRESOLVED (coverage debt)
- **Who is blocked:** Researchers using RT-1-X as the small cross-embodiment baseline in AMD-based comparisons
- **Action:** Validate RT-1-X inference on TensorFlow-ROCm or convert the checkpoint to a PyTorch/LeRobot path and document it
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence low
- **Evidence:** https://www.roboticscenter.ai/vla-models/best-2026
- **Component ref:** https://robotics-transformer-x.github.io/

#### [P2 · 12] No AMD-validated real-time stereo depth node; the accelerated Fast-FoundationStereo path is TensorRT/NITROS only

- **Component / trigger:** FoundationStereo (NVIDIA) — Zero-shot stereo matching model
- **AMD status:** `partial` — partial / in progress (nearest: Stock PyTorch-ROCm inference of the open FoundationStereo weights)
- **Who is blocked:** stereo-camera robots not built on Jetson
- **Action:** Benchmark FoundationStereo via ONNX/MIGraphX on Ryzen AI and MI300X and wrap it as a ROS 2 node
- **Scores:** openness 1 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://github.com/NVlabs/FoundationStereo
- **Component ref:** https://github.com/NVlabs/FoundationStereo

#### [P2 · 12] No synthetic-data-trained indoor object detector tuned as a pose-estimation front end on AMD NPUs

- **Component / trigger:** SyntheticaDETR (NVIDIA) — Indoor object detection model
- **AMD status:** `partial` — partial / in progress (nearest: Generic detectors in the Vitis AI and Ryzen AI model zoos)
- **Who is blocked:** warehouse and indoor manipulation integrators on Kria and Ryzen AI
- **Action:** Train and publish one synthetic-data detector checkpoint compiled for the Ryzen AI and Kria NPUs
- **Scores:** openness 1 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://onnxruntime.ai/docs/execution-providers/Vitis-AI-ExecutionProvider.html
- **Component ref:** https://developer.nvidia.com/isaac

#### [P2 · 12] No spatial-memory 3D action policy stack on AMD; the mapping backbone it builds on is CUDA-only

- **Component / trigger:** nvblox_mindmap (NVIDIA) — Spatial memory 3D action policies
- **AMD status:** `none` — no AMD path
- **Who is blocked:** research teams combining volumetric mapping with manipulation policies
- **Action:** Track a ROCm volumetric mapping backend first, since the policy layer is blocked on the CUDA map representation
- **Scores:** openness 2 · fit 2 · leverage 1 · evidence 3 · confidence med
- **Evidence:** https://github.com/nvidia-isaac/nvblox_mindmap
- **Component ref:** https://github.com/nvidia-isaac/nvblox_mindmap

#### [P2 · 12] Octo pins a JAX/TPU-oriented dependency stack with no ROCm validation, so Open X-Embodiment generalist baselines are unverified on AMD

- **Component / trigger:** Octo (Octo Model Team) — Generalist transformer robot policy
- **AMD status:** `community` — community-maintained only (nearest: AMD-built ROCm JAX wheels are the only path; no AMD-tested Octo build)
- **Who is blocked:** Robot-learning teams using Octo as an OXE baseline on non-NVIDIA hardware
- **Action:** Reproduce one Octo eval on ROCm JAX and file upstream fixes for any CUDA-pinned dependencies
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://rocm.docs.amd.com/en/latest/install/rocm.html
- **Component ref:** https://github.com/octo-models/octo

#### [P2 · 12] No documented ROCm build or smoke test for RDT-1B whose custom attention kernels are unverified on AMD

- **Component / trigger:** RDT-1B (OSS) — Diffusion foundation policy for bimanual manipulation
- **AMD status:** `unknown` — UNRESOLVED (coverage debt)
- **Who is blocked:** Bimanual diffusion-foundation-model users evaluating AMD for large open-weight policies
- **Action:** Run an RDT-1B inference smoke test on MI300X and publish the kernel and dependency gap list
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://www.roboticscenter.ai/state-of-robotics-2026
- **Component ref:** https://github.com/thu-ml/RoboticsDiffusionTransformer

#### [P2 · 8] No generated-video or rollout quality scoring toolkit available on AMD

- **Component / trigger:** Cosmos Evaluator (NVIDIA) — Generated video quality evaluation
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Teams training or fine-tuning world models and generative sim on AMD
- **Action:** Port open video-quality and physics-plausibility metrics to ROCm as part of a world-model evaluation suite
- **Scores:** openness 2 · fit 2 · leverage 1 · evidence 2 · confidence low
- **Evidence:** https://github.com/NVIDIA/cosmos-evaluator
- **Component ref:** https://github.com/NVIDIA/cosmos-evaluator

#### [P2 · 8] No AMD-maintained or ROCm-validated neural video tokenizer for world models, and the reference repo is archived

- **Component / trigger:** Cosmos-Tokenizer (NVIDIA) — Video neural tokenization
- **AMD status:** `none` — no AMD path
- **Who is blocked:** World foundation model researchers needing latent video tokenization on AMD
- **Action:** Validate one open video tokenizer on ROCm and add it to the ROCm model zoo with benchmark numbers
- **Scores:** openness 2 · fit 2 · leverage 1 · evidence 2 · confidence low
- **Evidence:** https://github.com/NVIDIA/Cosmos-Tokenizer
- **Component ref:** https://github.com/NVIDIA/Cosmos-Tokenizer

### L4 — Fleet, MLOps, Observability & Lifecycle

*45 components checked · 17 gaps*

#### [P0 · 81] No integrated VLA-specific safety-gated MLOps and lifecycle platform exists from any vendor

- **Component / trigger:** (whitespace) VLA lifecycle/MLOps platform (NONE) — VLA-specific model registry + safety-gated rollout
- **AMD status:** `none` — no AMD path
- **Who is blocked:** every team deploying learned policies to a real fleet
- **Action:** Seed an open-source robotics extension to MLflow or Kubeflow — registry, safety-gated rollback, drift detection — ROCm-default but hardware-agnostic
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-27
- **Component ref:** derived:grid-sweep

#### [P0 · 81] No product unifies per-joint latency, Hz, VLA action-drift and model provenance for deployed fleets

- **Component / trigger:** (whitespace) robot inference observability layer (NONE) — robot fleet inference observability (Hz, per-joint latency, action drift)
- **AMD status:** `none` — no AMD path
- **Who is blocked:** fleet operators running learned policies in production
- **Action:** Build on ros-opentelemetry and partner with Foxglove for visualization
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-25
- **Component ref:** derived:grid-sweep

#### [P0 · 81] Zero RocProfiler integration exists anywhere in the robotics or AI observability ecosystem

- **Component / trigger:** (whitespace) RocProfiler/DCGM-to-ROS 2 exporter (NONE) — accelerator profiler exported into ROS 2 tracing
- **AMD status:** `none` — no AMD path
- **Who is blocked:** anyone profiling accelerator behaviour inside a ROS 2 graph
- **Action:** Contribute a RocProfiler-to-ROS 2 exporter to ros-opentelemetry — roughly a 4-week effort with no competing product
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-25
- **Component ref:** derived:grid-sweep

#### [P0 · 54] No ROCm-accelerated routing or decision-optimization solver; only CPU solvers such as OR-Tools and HiGHS are available

- **Component / trigger:** cuOpt (NVIDIA) — GPU route and fleet optimization
- **AMD status:** `none` — no AMD path
- **Who is blocked:** warehouse fleet operators and logistics platforms wanting AMD GPUs
- **Action:** HIPify the Apache-2.0 cuOpt CUDA kernels and publish a ROCm build of the routing solver
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://github.com/NVIDIA/cuopt
- **Component ref:** https://github.com/NVIDIA/cuopt

#### [P0 · 36] No packaged edge AI microservice framework (ingest, inference, storage, REST APIs) for Kria or Ryzen AI Embedded

- **Component / trigger:** Jetson Platform Services (NVIDIA) — Edge AI microservice deployment
- **AMD status:** `partial` — partial / in progress (nearest: Kria app packaging and the announced Kria AI Robotics Developer Platform software libraries)
- **Who is blocked:** integrators deploying camera-AI microservices on AMD edge SoCs
- **Action:** Ship a reference microservice bundle for the Kria AI Robotics Developer Platform before its Q4 2026 GA
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://github.com/NVIDIA-AI-IOT/jetson-platform-services
- **Component ref:** https://github.com/NVIDIA-AI-IOT/jetson-platform-services

#### [P0 · 36] No ROCm-aware ROS 2 tracing that correlates GPU and NPU kernel timelines with node and callback-chain latency

- **Component / trigger:** ros2_tracing / CARET (OSS) — Runtime tracing of node and executor latency
- **AMD status:** `partial` — partial / in progress (nearest: AMD ships rocprofiler-sdk, rocprofv3 and roctx in the ROCm core SDK, but nothing binds them to ROS 2 executor or callback tracing)
- **Who is blocked:** Robotics teams debugging end-to-end control-loop jitter on AMD accelerators
- **Action:** Add roctx instrumentation and a ros2_tracing/CARET analysis recipe that merges rocprofv3 traces with LTTng callback chains
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://rocm.docs.amd.com/en/latest/install/rocm.html
- **Component ref:** https://github.com/orgs/ros2/repositories

#### [P0 · 36] No balenaOS device type for Kria SOMs, Zynq UltraScale+ or Versal while a dozen Jetson variants are first-class

- **Component / trigger:** balenaCloud / balenaOS (Balena) — Container-based device fleet deployment
- **AMD status:** `partial` — partial / in progress (nearest: balenaOS generic-amd64 image runs on Ryzen Embedded x86 but no AMD embedded board device type exists)
- **Who is blocked:** Robot fleet teams wanting container-based OTA on AMD adaptive SoCs; forces them to Jetson or to roll their own Yocto pipeline
- **Action:** Contribute and maintain a balena device type for the Kria K26/K24 SOM starter kits, mirroring the Jetson board support pattern
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://docs.balena.io/reference/hardware/devices/
- **Component ref:** https://www.balena.io/

#### [P0 · 36] No AMD NPU/edge device plugin so Ryzen AI XDNA accelerators are invisible to K8s/KubeEdge fleet schedulers

- **Component / trigger:** KubeEdge (CNCF) — Cloud-edge orchestration for device fleets
- **AMD status:** `partial` — partial / in progress (nearest: AMD GPU Operator and ROCm k8s-device-plugin on standard Kubernetes nodes)
- **Who is blocked:** Robot fleet operators wanting one control plane over mixed cloud GPU and edge NPU nodes
- **Action:** Publish an XDNA/Ryzen AI device plugin and a KubeEdge-verified ROCm edge node reference
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://github.com/ROCm/k8s-device-plugin
- **Component ref:** https://kubeedge.io/

#### [P0 · 36] Robot fleet edge data center is an uncontested emerging category with no incumbent

- **Component / trigger:** (whitespace) robot fleet edge datacenter category (NONE) — robot fleet edge data center / GPU module fleet compute
- **AMD status:** `none` — no AMD path
- **Who is blocked:** robot fleets needing shared compute between edge and cloud
- **Action:** First-mover positioning while the category has no incumbent
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-10
- **Component ref:** derived:grid-sweep

#### [P1 · 24] No accelerated rosbag record/validate/convert tooling on the AMD side

- **Component / trigger:** isaac_ros_data_tools (NVIDIA) — Rosbag inspection and conversion
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Robot data teams logging multi-camera sensor data on AMD edge boxes
- **Action:** Add rosbag2 validation and H.264 conversion utilities using VCU/VA-API decode to the AMD Robotics Software Suite
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/ai.html
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 24] No video-search-and-summarization agent blueprint published on ROCm

- **Component / trigger:** Metropolis VSS Blueprint (NVIDIA) — Video search summarization agents
- **AMD status:** `partial` — partial / in progress (nearest: AMD Solution Blueprints plus AMD Inference Microservice in the Enterprise AI Suite)
- **Who is blocked:** Integrators building camera-fleet Q and A or VLM video analytics on Instinct
- **Action:** Publish a VSS-equivalent blueprint chaining VLM plus vector DB plus ASR on ROCm
- **Scores:** openness 2 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://rocm.blogs.amd.com/blog/2025.html
- **Component ref:** https://developer.nvidia.com/metropolis

#### [P1 · 24] No AMD hardware-accelerated image encoder node for ROS 2 logging, where NVIDIA ships isaac_ros_h264_encoder for the same job

- **Component / trigger:** rosbag2 (OSS) — Time-series recording and replay of ROS topics
- **AMD status:** `partial` — partial / in progress (nearest: rosbag2 itself runs unmodified on AMD hosts, but AMD has no ROS 2 node exposing VCN hardware video encode for high-rate multi-camera recording)
- **Who is blocked:** Fleets recording multi-camera bags on AMD edge boxes and paying CPU cost for compression
- **Action:** Wrap VA-API/AMF VCN encode in a ROS 2 image transport plugin usable as a rosbag2 recording front end
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://nvidia-isaac-ros.github.io/releases/index.html
- **Component ref:** https://github.com/orgs/ros2/repositories

#### [P1 · 24] No commercial fleet-scale data curation layer (dedup, quality scoring, active-learning selection)

- **Component / trigger:** (whitespace) data-intelligence / fleet curation layer (NONE) — fleet-scale demonstration data curation (dedup, quality scoring, active learning)
- **AMD status:** `none` — no AMD path
- **Who is blocked:** teams with large teleop datasets and no way to triage them
- **Action:** Sponsor or seed an open fleet-scale curation toolchain — lower commitment than the MLOps platform
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-26
- **Component ref:** derived:grid-sweep

#### [P2 · 16] No reference robotics sim-train-eval orchestration recipe for ROCm clusters

- **Component / trigger:** OSMO (NVIDIA) — Physical AI workflow orchestration
- **AMD status:** `partial` — partial / in progress (nearest: Generic Kubernetes and Slurm with the ROCm k8s device plugin)
- **Who is blocked:** teams scaling synthetic data, training and evaluation jobs on Instinct clusters
- **Action:** Publish one worked YAML pipeline running sim, train and eval stages on a ROCm Kubernetes cluster
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence low
- **Evidence:** https://www.linkedin.com/pulse/from-experiments-production-how-nvidia-osmo-azure-aaron-schnieder-zpqte
- **Component ref:** https://developer.nvidia.com/osmo

#### [P2 · 12] No AMD-operated secure OTA/lifecycle cloud for Kria SOMs comparable to Torizon Cloud for Toradex modules

- **Component / trigger:** Torizon OS / Torizon Cloud (Toradex) — Commercial Yocto OTA for edge devices
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Industrial customers designing Kria SOMs into products who need signed, Uptane-grade field updates and device management out of the box
- **Action:** Publish a reference Kria SOM + RAUC/Uptane A/B update integration in the Kria app store, or partner with an existing OTA vendor for a supported Kria offering
- **Scores:** openness 1 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/k24.html
- **Component ref:** https://www.toradex.com/torizon

#### [P2 · 8] No AMD-maintained robot health monitor and no amd-smi to ROS 2 telemetry bridge for accelerated pipelines

- **Component / trigger:** greenwave_monitor (NVIDIA) — ROS 2 topic health monitoring
- **AMD status:** `community` — community-maintained only (nearest: Generic ROS 2 tooling (ros2 topic hz, diagnostics, Foxglove) with no AMD-maintained equivalent)
- **Who is blocked:** fleet operators debugging dropped-frame and stalled-pipeline failures on AMD compute
- **Action:** Publish a small ROS 2 node exposing amd-smi GPU and NPU telemetry as diagnostics topics
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P2 · 8] No ROCm or XDNA accelerated inference component for managed edge runtimes; only CPU path on AMD

- **Component / trigger:** AWS IoT Greengrass (AWS) — Managed edge runtime and component deploy
- **AMD status:** `partial` — partial / in progress (nearest: Greengrass runs on x86-64 Linux so AMD EPYC and Ryzen Embedded gateways are supported hosts)
- **Who is blocked:** Teams shipping OTA-managed robot edge inference on AWS-managed fleets
- **Action:** Publish a Greengrass custom component recipe that runs ROCm/Lemonade inference on Ryzen AI Embedded
- **Scores:** openness 1 · fit 2 · leverage 2 · evidence 2 · confidence low
- **Evidence:** https://aws.amazon.com/greengrass/
- **Component ref:** https://aws.amazon.com/greengrass/

### L5 — Certification, Standards & Compliance

*32 components checked · 21 gaps*

#### [P0 · 81] No safety-certifiable RTOS image or certification artifact package that runs on AMD adaptive SoCs and Kria SOMs

- **Component / trigger:** Zephyr Safety Certification (IEC 61508 SIL 3) (Linux Foundation) — Safety certification path for open RTOS
- **AMD status:** `partial` — partial / in progress (nearest: AMD Functional Safety design flow for Zynq UltraScale+ and Versal adaptive SoCs (IEC 61508 / ISO 26262 certified flow and safety IP))
- **Who is blocked:** Industrial cobot and AMR OEMs that need SIL 3 software on AMD silicon and today buy a certified RTOS bundled with another vendor
- **Action:** Fund an upstream Zephyr board port plus safety-scope certification evidence for Kria K24/K26 so customers inherit the artifacts
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/functional-safety.html
- **Component ref:** https://docs.zephyrproject.org/latest/safety/safety_overview.html

#### [P0 · 81] No functional-safety certification covers AMD AI-inference/XDNA tiles — only the deterministic fabric

- **Component / trigger:** (whitespace) certified AI-inference safety envelope (NONE) — functional-safety certification covering AI-inference tiles (not just fabric)
- **AMD status:** `none` — no AMD path (nearest: TUV SUD design-flow cert covers FPGA fabric only)
- **Who is blocked:** anyone putting a learned policy on AMD silicon in a safety context
- **Action:** Scope extending the existing TUV SUD design-flow certification to Kria X100 AI-engine tiles — an extension, not a new program
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-19
- **Component ref:** derived:grid-sweep

#### [P0 · 36] No formal runtime safety-envelope monitor mapped onto AMD lockstep R5F or an FPGA safety partition

- **Component / trigger:** ad-rss-lib (Intel / OSS) — Formal safety envelope for motion decisions
- **AMD status:** `none` — no AMD path (nearest: AMD Isolation Design Flow safety partitioning only, no motion envelope monitor)
- **Who is blocked:** Humanoid and AMR builders needing a certifiable last-line motion veto on AMD silicon
- **Action:** Port ad-rss-lib onto Kria Cortex-R5F lockstep and publish it as a reference safety-partition design
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/functional-safety.html
- **Component ref:** https://github.com/intel/ad-rss-lib

#### [P0 · 36] No public evidence of AMD participation in ISO TC 299 for the humanoid safety standard

- **Component / trigger:** ISO 25785-1 (Working Draft) (ISO) — Safety for dynamically stable walking robots
- **AMD status:** `none` — no AMD path
- **Who is blocked:** AMD's future safety-certification requirements
- **Action:** Confirm whether any AMD employee or Alliance Partner sits on ISO TC 299; if not, nominate one — costs headcount-hours, not engineering
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-21
- **Component ref:** https://theresarobotforthat.com/blog/humanoid-robot-safety-standards-2026/

#### [P0 · 36] The humanoid safety standard is still at committee draft — participation window is open and uncontested

- **Component / trigger:** (whitespace) humanoid safety standard participation (NONE) — safety standard for dynamically-balanced humanoids
- **AMD status:** `none` — no AMD path
- **Who is blocked:** AMD's future certification obligations
- **Action:** Nominate a participant to ISO TC 299 now; cheapest and longest-horizon action in the register
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-21
- **Component ref:** derived:grid-sweep

#### [P1 · 27] No integrated AI-compute-plus-safety-island robotics SoC or safety-certified AI runtime

- **Component / trigger:** Jetson AGX Thor functional safety (NVIDIA) — Integrated functional safety compute
- **AMD status:** `partial` — partial / in progress (nearest: TUV SUD certified AMD functional safety design flow plus Zynq-7000 SIL3 on-chip redundancy concept)
- **Who is blocked:** Cobot and AMR OEMs needing SIL2/SIL3 alongside VLA inference on one module
- **Action:** Publish a safety concept architecture pairing X100 AI compute with a Spartan/Zynq safety island
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/functional-safety.html
- **Component ref:** https://developer.nvidia.com/isaac/gr00t

#### [P1 · 27] SIL evidence stops at the adaptive SoC/FPGA line; no IEC 61508 artifacts for ROCm, Instinct or Ryzen AI compute running robot autonomy

- **Component / trigger:** IEC 61508 (IEC) — Generic functional safety lifecycle and SIL
- **AMD status:** `partial` — partial / in progress (nearest: AMD TUV SUD certified functional safety design flow, Isolation Design Flow, SEM IP, Zynq-7000 SIL3 safety concept)
- **Who is blocked:** Robot OEMs who need the AI compute itself inside the safety argument, not just an FPGA safety island
- **Action:** Scope and publish an IEC 61508 safety element out of context concept for Ryzen AI Embedded plus a ROCm safety manual
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** corpus:amdcom-5013f693ca.txt
- **Component ref:** https://en.wikipedia.org/wiki/IEC_61508

#### [P1 · 27] No ASIL-rated AMD GPU or NPU compute path; automotive-grade evidence covers FPGA fabric not the AI accelerator stack

- **Component / trigger:** ISO 26262 (ISO) — Road vehicle functional safety and ASIL
- **AMD status:** `partial` — partial / in progress (nearest: AMD adaptive SoC design flow certified for ISO 26262 by TUV SUD)
- **Who is blocked:** Autonomous mobile robot and AV builders evaluating AMD against ASIL-B/D rated NVIDIA parts
- **Action:** Publish ASIL decomposition guidance pairing a Versal/Zynq safety island with a Ryzen AI or Radeon inference channel
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** corpus:amdcom-5013f693ca.txt
- **Component ref:** https://en.wikipedia.org/wiki/ISO_26262

#### [P1 · 27] No PL d/e rated reference design for a ROS 2 motion safety controller on Kria or Ryzen AI Embedded

- **Component / trigger:** ISO 13849-1 (ISO) — Performance level for safety control systems
- **AMD status:** `partial` — partial / in progress (nearest: ISO 13849 listed among standards covered by AMD certified industrial design flow)
- **Who is blocked:** Cobot and AMR integrators who must show a performance level for the control channel
- **Action:** Ship a Kria-based safety controller reference design with a PL d gap analysis and TUV report
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** corpus:amdcom-5013f693ca.txt
- **Component ref:** https://www.iso.org/standard/73481.html

#### [P1 · 24] Safety story stops at the adaptive SoC; no safety-certifiable Linux, ROCm driver or NPU runtime evidence package and no visible AMD role in ELISA

- **Component / trigger:** ELISA (Linux Foundation) — Safety-certifiable Linux enablement
- **AMD status:** `partial` — partial / in progress (nearest: AMD Functional Safety design flow and safety-certified adaptive SoCs covering IEC 61508 and ISO 26262 at the silicon and FPGA level)
- **Who is blocked:** Integrators needing a certifiable Linux plus accelerator stack for SIL-rated robot compute
- **Action:** Join ELISA and contribute an amdgpu/ROCm kernel driver safety analysis to the workgroup evidence set
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/functional-safety.html
- **Component ref:** https://elisa.tech/

#### [P1 · 24] No AMD reference target or hardware abstraction contribution in the open ASIL-B software-defined-vehicle core stack that robotics middleware is converging on

- **Component / trigger:** Eclipse S-CORE (Eclipse Foundation) — Open safety-certified vehicle software platform
- **AMD status:** `partial` — partial / in progress (nearest: AMD Functional Safety certification flow for adaptive SoCs (IEC 61508, ISO 26262) gives silicon-level ASIL support but no S-CORE platform participation is visible)
- **Who is blocked:** Automotive-adjacent robotics vendors picking an ASIL-B compute platform for S-CORE-based stacks
- **Action:** Register an AMD reference board as an S-CORE supported target and contribute the hardware abstraction layer for it
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://projects.eclipse.org/projects/automotive.score
- **Component ref:** https://projects.eclipse.org/projects/automotive.score

#### [P1 · 24] No AMD equivalent to the Halos AI Systems Inspection Lab or its 40-company ecosystem

- **Component / trigger:** Halos AI Systems Inspection Lab (NVIDIA) — Vendor safety inspection lab for physical AI
- **AMD status:** `none` — no AMD path
- **Who is blocked:** robot OEMs needing third-party AI safety inspection
- **Action:** Partner with an existing ANAB-accredited body (TUV SUD, exida) rather than building an inspection lab from scratch
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-20
- **Component ref:** https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/

#### [P1 · 24] No accredited third-party AI-robotics inspection lab exists outside one vendor's own program

- **Component / trigger:** (whitespace) independent AI systems inspection lab (NONE) — accredited third-party AI-robotics systems inspection lab
- **AMD status:** `none` — no AMD path
- **Who is blocked:** robot OEMs needing independent AI safety assessment
- **Action:** Partner with an accredited body rather than building the lab
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-20
- **Component ref:** derived:grid-sweep

#### [P1 · 18] No published sensor-to-actuation latency measurement and V and V tool for AMD robotics platforms

- **Component / trigger:** Holoscan Sensor Bridge Latency Measurement Tool (NVIDIA) — Latency verification and validation tooling
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Safety and real-time engineers who must certify camera-to-control timing
- **Action:** Ship an FPGA-timestamped latency measurement reference design on the Kria AI Robotics Developer Platform
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 1 · confidence low
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/ai/robotics-developer-platform.html
- **Component ref:** https://docs.nvidia.com/holoscan/

#### [P1 · 18] No AMD-specific certified hypervisor BSP or mixed-criticality reference partitioning safety and ROCm AI workloads on one AMD device

- **Component / trigger:** PikeOS (SYSGO) — Certified RTOS and hypervisor in one
- **AMD status:** `partial` — partial / in progress (nearest: PikeOS supports x86 and Arm v8 with TUV SUD DO-178C DAL A, IEC 61508 SIL 3 and ISO 26262 ASIL D, reachable on AMD x86-64 and Zynq/Versal Arm cores)
- **Who is blocked:** Robot platform teams consolidating safety control and AI inference onto a single AMD SoC
- **Action:** Fund a PikeOS or Xen-based mixed-criticality reference on Versal/Ryzen Embedded with published isolation evidence
- **Scores:** openness 1 · fit 3 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://www.sysgo.com/pikeos
- **Component ref:** https://www.sysgo.com/pikeos

#### [P2 · 16] No published qualification kit or test-suite evidence for the LLVM/GCC toolchains in Vitis or for ROCm amdclang

- **Component / trigger:** GCC + Validas Compiler Test Suite (Validas + OSS GCC) — Qualification kit for open-source compiler
- **AMD status:** `partial` — partial / in progress (nearest: AMD certified compiler tools shipped in the functional safety package cover the GCC-based embedded toolchain)
- **Who is blocked:** Safety teams wanting to reuse open toolchains on AMD targets without buying a proprietary compiler
- **Action:** Engage a qualification-kit vendor to run a compiler test suite against the Vitis GCC and publish the report
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence low
- **Evidence:** https://wrocpp.github.io/toolset/qualified-compilers/
- **Component ref:** https://wrocpp.github.io/toolset/qualified-compilers/

#### [P2 · 12] AMD collateral references DO-178B not the current DO-178C, and no DAL evidence exists for ROCm or AI runtime software in aerial robotics

- **Component / trigger:** DO-178C (RTCA / EUROCAE) — Airborne software certification objectives
- **AMD status:** `partial` — partial / in progress (nearest: AMD aerospace and defense design flow lists DO-254 and DO-178B support)
- **Who is blocked:** Drone and UAS builders needing certifiable onboard autonomy compute
- **Action:** Refresh the avionics collateral to DO-178C/DO-330 and state what tool qualification data AMD supplies
- **Scores:** openness 1 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** corpus:amdcom-5013f693ca.txt
- **Component ref:** https://en.wikipedia.org/wiki/DO-178C

#### [P2 · 12] No AMD-published safety-certified RTOS BSP or safety manual for Ryzen AI Embedded or Kria, so the certified reflex layer has no AMD reference

- **Component / trigger:** QNX OS for Safety (BlackBerry QNX) — Certified RTOS variant for safety products
- **AMD status:** `partial` — partial / in progress (nearest: QNX lists AMD among its silicon partners so QNX runs on AMD x86-64 and Arm cores)
- **Who is blocked:** Humanoid and cobot builders needing a certified real-time reflex partition next to an AI compute partition
- **Action:** Co-publish with QNX or a peer RTOS vendor a certified BSP and safety manual for Ryzen AI Embedded X100 and Kria
- **Scores:** openness 1 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://qnx.software/
- **Component ref:** https://blackberry.qnx.com/en/products/safety-certified

#### [P2 · 8] No Holoscan-equivalent low-latency sensor-to-inference SDK packaged for regulated medical pipelines

- **Component / trigger:** IGX + Holoscan platform (NVIDIA) — Medical-grade edge platform compliance
- **AMD status:** `partial` — partial / in progress (nearest: AMD adaptive SoC medical portfolio plus TUV-certified FuSa flow plus Imaging Solution Blueprint on Radeon)
- **Who is blocked:** Medical device OEMs building endoscopy/ultrasound/surgical edge products
- **Action:** Package the Kria plus ROCm sensor pipeline as a documented medical reference platform with FuSa artifacts
- **Scores:** openness 1 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/functional-safety.html
- **Component ref:** https://docs.nvidia.com/holoscan/

#### [P2 · 8] No safety-qualified compiler for AIE kernels, HIP/ROCm device code or XDNA NPU graphs; qualification stops at the scalar Arm/MicroBlaze toolchain

- **Component / trigger:** MULTI compiler with TCL-3 kit (Green Hills Software) — Safety-qualified C/C++ compiler toolchain
- **AMD status:** `partial` — partial / in progress (nearest: Certified compiler and design/verification tools bundled in the AMD functional safety package for adaptive SoCs)
- **Who is blocked:** Anyone trying to place AMD AI acceleration inside an ASIL D or DAL A software item
- **Action:** State exactly which AMD compilers are qualified and to what level, then start a tool qualification plan for the AIE/HIP compiler
- **Scores:** openness 1 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** corpus:amdcom-5013f693ca.txt
- **Component ref:** https://wrocpp.github.io/toolset/qualified-compilers/

#### [P3 · 6] No published IEC 62443-4-2 component security level claim for AMD embedded/robotics compute platforms

- **Component / trigger:** IEC 62443 (IEC) — Industrial automation and control system security
- **AMD status:** `unknown` — UNRESOLVED (coverage debt)
- **Who is blocked:** OT integrators putting AMD compute into certified robot cells under EU CRA and NIS-2
- **Action:** Confirm whether any AMD embedded platform holds a 62443-4-2 SL claim and publish it alongside the functional safety collateral
- **Scores:** openness 1 · fit 2 · leverage 3 · evidence 1 · confidence low
- **Evidence:** corpus:amdcom-5013f693ca.txt
- **Component ref:** https://webstore.iec.ch/publication/7029

### L6 — Developer Experience, Distribution & Community

*29 components checked · 26 gaps*

#### [P0 · 81] No AMD-published VLA policy checkpoints or LeRobot datasets despite an active and large HF org

- **Component / trigger:** Hugging Face Hub (HuggingFace) — Model and dataset hosting and distribution
- **AMD status:** `partial` — partial / in progress (nearest: huggingface.co/amd org with 686 mostly LLM and quantized models plus 15 non-robotics datasets)
- **Who is blocked:** Robot learning users looking for ROCm-validated policy weights they can pull and run
- **Action:** Publish ROCm-validated ACT, SmolVLA and pi0 checkpoints and one teleop dataset under huggingface.co/amd
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://huggingface.co/amd
- **Component ref:** https://huggingface.co/lerobot

#### [P0 · 81] No CI publishes prebuilt robot-policy wheels for AMD targets

- **Component / trigger:** (whitespace) VLA policy CI/wheel pipeline (NONE) — CI publishing prebuilt robot-policy wheels per accelerator target
- **AMD status:** `none` — no AMD path
- **Who is blocked:** developers who will not build from source
- **Action:** Reuse the vLLM CI playbook for LeRobot policies on gfx942/gfx1100
- **Scores:** openness 3 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-9
- **Component ref:** derived:grid-sweep

#### [P0 · 54] rosdistro carries nvidia-cuda, nvidia-cuda-dev and nvidia-cudnn keys but zero rocm, hip, hsa or amdgpu rosdep keys

- **Component / trigger:** rosdep (Open Robotics) — System dependency resolution across distros
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Any ROS 2 package author who wants to declare a ROCm or HIP runtime dependency
- **Action:** Submit rosdep base.yaml keys for rocm-hip-runtime, rocm-libs and amdgpu-dkms
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/base.yaml
- **Component ref:** https://github.com/ros-infrastructure/rosdep

#### [P0 · 54] No AMD-maintained ROS 2 release pipeline or apt channel publishing ROCm-accelerated packages

- **Component / trigger:** bloom / ros_buildfarm (Open Robotics) — Release automation into binary distributions
- **AMD status:** `none` — no AMD path (nearest: Kria Robotics Stack shipped as Vitis overlays and Kria App Store images, not as released ROS debs)
- **Who is blocked:** ROS 2 integrators who expect apt-installable AMD accelerated nodes like the Isaac ROS apt repo
- **Action:** Bloom-release one AMD ROS 2 package into rosdistro to stand up the release pipeline end to end
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://raw.githubusercontent.com/ros/rosdistro/master/jazzy/distribution.yaml
- **Component ref:** https://github.com/ros-infrastructure/bloom

#### [P0 · 54] Zero AMD, Xilinx, Kria or ROCm repositories appear in the ROS 2 distribution index while NVIDIA-ISAAC-ROS entries do

- **Component / trigger:** index.ros.org (Open Robotics) — Canonical package and API index for ROS 2
- **AMD status:** `none` — no AMD path (nearest: Kria App Store and scattered AMD GitHub repos that sit outside the ROS index)
- **Who is blocked:** ROS 2 developers discovering which hardware acceleration options exist for their distro
- **Action:** Register Kria Robotics Stack packages in rosdistro so they surface on index.ros.org
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://raw.githubusercontent.com/ros/rosdistro/master/jazzy/distribution.yaml
- **Component ref:** https://index.ros.org/packages/

#### [P0 · 54] AMD ships robotics compute boards but no complete reference mobile robot with a maintained ROS 2 nav/SLAM stack and curriculum like TurtleBot 4

- **Component / trigger:** TurtleBot 4 (Clearpath Robotics / OSRF) — Standard reference mobile robot for ROS 2
- **AMD status:** `partial` — partial / in progress (nearest: AMD Kria KR260 Robotics Starter Kit and the Kria AI Robotics Developer Platform (Ryzen AI Embedded X100 plus Kria FPGA, CPU/GPU/NPU/FPGA))
- **Who is blocked:** Educators, evaluators and new ROS 2 developers who need a buyable end-to-end AMD robot rather than a carrier board
- **Action:** Partner with one AMR vendor on a TurtleBot-class SKU built on Kria AI SOM with a maintained ROS 2 bringup repo
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://ucadvanced.com/amd-kria-ai-solutions-launched-for-physical-ai/
- **Component ref:** https://turtlebot.github.io/turtlebot4-user-manual/

#### [P0 · 54] AMD has no presence on the model hub developers actually browse

- **Component / trigger:** (whitespace) vendor model cards at the callsite (NONE) — accelerator-vendor presence on the model hub developers actually use
- **AMD status:** `none` — no AMD path (nearest: working ROCm code exists but is not surfaced)
- **Who is blocked:** developers choosing hardware at the moment of model selection
- **Action:** Publish model cards — documentation, not engineering
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-5
- **Component ref:** derived:grid-sweep

#### [P0 · 54] Zero AMD GPU/NPU certified design wins in the Windows industrial IPC market; the technical barrier is already closed

- **Component / trigger:** (whitespace) industrial automation platform certification (NONE) — industrial IPC / PLC vendor certification for AI accelerators
- **AMD status:** `none` — no AMD path (nearest: AMD CPU design wins exist (CX20x3, K4131-Px); zero GPU/NPU wins)
- **Who is blocked:** industrial automation integrators on TwinCAT and SIMATIC
- **Action:** Pursue TwinCAT 3 ML and SIMATIC Edge GPU/NPU certification — commercial motion, not engineering
- **Scores:** openness 3 · fit 3 · leverage 2 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-3
- **Component ref:** derived:grid-sweep

#### [P0 · 36] No reusable AMD-maintained ROS 2 graph benchmark harness or per-node published numbers

- **Component / trigger:** ros2_benchmark (NVIDIA) — ROS 2 graph performance benchmarking
- **AMD status:** `partial` — partial / in progress (nearest: OpenNav Robotics Workload Benchmark commissioned by AMD; ros2_benchmark itself runs on AMD hosts)
- **Who is blocked:** Buyers comparing AMD versus Jetson and developers tuning ROS 2 graphs
- **Action:** Contribute AMD plugins and reproducible configs plus results back to ros2_benchmark
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 3 · confidence med
- **Evidence:** https://opennav.org/news/opennav-robotics-workload-benchmark
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P0 · 36] No apt channel shipping prebuilt ROCm-accelerated ROS 2 packages per ROS distro so AMD users build from source

- **Component / trigger:** packages.ros.org apt repositories (ros-infrastructure) — Binary apt distribution of ROS packages
- **AMD status:** `partial` — partial / in progress (nearest: repo.radeon.com ROCm apt repositories and amdgpu-install for Debian/Ubuntu)
- **Who is blocked:** ROS 2 integrators on Ryzen and Radeon hosts who get CPU-only debs from packages.ros.org
- **Action:** Publish a ros-rocm apt suite on repo.radeon.com pinned to one active ROS distro with a handful of accelerated nodes
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://rocm.docs.amd.com/en/latest/install/rocm.html
- **Component ref:** https://index.ros.org/

#### [P0 · 36] No official ros image variant with ROCm runtime preinstalled equivalent to the CUDA-enabled robotics base images

- **Component / trigger:** Docker Hub official ros images (Docker Inc / OSRF) — Official prebuilt container images for ROS
- **AMD status:** `partial` — partial / in progress (nearest: rocm/ Docker Hub organization images (rocm/dev-ubuntu, rocm/pytorch, rocm/vllm) maintained by AMD)
- **Who is blocked:** Robotics teams containerizing ROS 2 workloads for AMD GPUs who must hand-layer ROCm onto the ros base image
- **Action:** Publish a ros-rocm tag pairing the current ROS LTS with a supported ROCm runtime and keep it in the rocm Docker Hub org
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://hub.docker.com/u/rocm
- **Component ref:** https://hub.docker.com/_/ros

#### [P0 · 36] No curated robotics section in the AMD catalog: no validated VLA/perception containers, pretrained policies or deployment charts per AMD part

- **Component / trigger:** NGC Catalog (NVIDIA) — Curated accelerated container and model catalog
- **AMD status:** `partial` — partial / in progress (nearest: AMD Infinity Hub containerized application catalog plus ROCm Docker Hub org and AMD models on Hugging Face)
- **Who is blocked:** Robotics developers evaluating AMD who find HPC and LLM containers but nothing robotics-shaped to start from
- **Action:** Add a robotics collection to Infinity Hub with ROCm-validated LeRobot, ACT/SmolVLA and perception containers and per-GPU tested tags
- **Scores:** openness 2 · fit 3 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://en.wikipedia.org/wiki/ROCm
- **Component ref:** https://catalog.ngc.nvidia.com/

#### [P0 · 36] AMD and ROCm appear nowhere in the community census of cloud-robotics and RobOps tooling across all its categories

- **Component / trigger:** awesome-cloud-robotics curated list (Airbotics / OSS) — Open-source deployment platform listing
- **AMD status:** `none` — no AMD path
- **Who is blocked:** Fleet-ops and robot-MLOps teams surveying the tooling landscape, who see no AMD-aware option
- **Action:** Land ROCm support in one or two listed fleet/data-infrastructure projects and open a PR adding them to the list
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 3 · confidence med
- **Evidence:** https://github.com/Airbotics/awesome-cloud-robotics
- **Component ref:** https://github.com/Airbotics/awesome-cloud-robotics

#### [P0 · 36] No validated end-to-end AMD synthetic-data pipeline; components exist but orchestration is unowned

- **Component / trigger:** (whitespace) synthetic data pipeline reference (NONE) — end-to-end validated synthetic-data pipeline reference (non-NVIDIA)
- **AMD status:** `none` — no AMD path (nearest: Genesis World is ROCm-native; Cosmos 3 Nano community-confirmed on ROCm)
- **Who is blocked:** teams building sim-to-real data pipelines on AMD
- **Action:** Own and publish the end-to-end reference — an integration and authorship gap, not a components gap
- **Scores:** openness 2 · fit 3 · leverage 2 · evidence 3 · confidence high
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-4
- **Component ref:** derived:grid-sweep

#### [P1 · 27] GitHub-hosted GPU runners are NVIDIA Tesla T4 only, so open-source robotics repos have no free hosted path to test on ROCm

- **Component / trigger:** GitHub-hosted larger runners (GitHub) — Hosted ARM and GPU CI runners
- **AMD status:** `partial` — partial / in progress (nearest: AMD Developer Cloud MI300X instances and self-hosted GitHub Actions runners on AMD GPUs)
- **Who is blocked:** Maintainers of open robotics and VLA repos who therefore only gate merges on CUDA
- **Action:** Sponsor a hosted AMD GPU runner pool or a free ROCm CI credit program for named upstream robotics repos
- **Scores:** openness 1 · fit 3 · leverage 3 · evidence 3 · confidence high
- **Evidence:** https://docs.github.com/en/actions/reference/runners/larger-runners
- **Component ref:** https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners

#### [P1 · 24] No single maintained dev-environment CLI for reproducible ROS 2 container build and flash on AMD

- **Component / trigger:** isaac-ros-cli (NVIDIA) — Dev environment management CLI
- **AMD status:** `partial` — partial / in progress (nearest: Kria Robotics Stack colcon acceleration plus PetaLinux/Vitis plus AMD Robotics Software Suite)
- **Who is blocked:** ROS 2 developers onboarding to Kria and ROCm targets
- **Action:** Ship one amd-robotics CLI wrapping container build, flash, deploy and cross-compile
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/ai.html
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 24] No composed multi-node accelerated perception graph examples end to end

- **Component / trigger:** isaac_ros_examples (NVIDIA) — Multi-GEM composition examples
- **AMD status:** `partial` — partial / in progress (nearest: AMD Robotics Software Suite reference applications plus Vitis Vision and KRS accelerated examples)
- **Who is blocked:** Developers assembling full perception pipelines on ROCm or Kria fabric
- **Action:** Publish end-to-end ROS 2 launch examples chaining several accelerated nodes with measured throughput
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://www.amd.com/en/products/system-on-modules/kria/ai.html
- **Component ref:** https://github.com/orgs/NVIDIA-ISAAC-ROS/repositories?type=all

#### [P1 · 24] No ROCm packages on conda-forge, so a GPU-accelerated conda ROS 2 environment cannot be solved

- **Component / trigger:** RoboStack (OSS) — Conda-based cross-platform ROS distribution
- **AMD status:** `community` — community-maintained only (nearest: ROCm ships via apt, amdgpu-install, tarball or pip; RoboStack conda ROS runs on AMD CPUs unaccelerated)
- **Who is blocked:** Windows, macOS and HPC users who install ROS 2 through conda rather than apt
- **Action:** Publish ROCm runtime feedstocks to conda-forge so RoboStack environments can link HIP
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://rocm.docs.amd.com/en/latest/install/rocm.html
- **Component ref:** https://robostack.github.io/

#### [P1 · 24] No AMD-published bring-up, BOM or validated teleop latency numbers for Dynamixel leader-follower arms on Ryzen or Radeon hosts

- **Component / trigger:** Koch v1.1 arm (OSS (Jess Moss)) — Dynamixel-based leader-follower teaching arm
- **AMD status:** `community` — community-maintained only (nearest: LeRobot on ROCm (AMD Instinct/Radeon VLA training and inference blogs); the Dynamixel arm itself is USB and host-neutral)
- **Who is blocked:** Teleop data-collection teams choosing a host box for imitation-learning rigs
- **Action:** Publish a one-page Koch-class arm bring-up on a Ryzen AI Embedded host with measured teleop and record loop rates
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://github.com/huggingface/lerobot
- **Component ref:** https://github.com/jess-moss/koch-v1-1

#### [P1 · 24] No AMD reference mobile-manipulation kit pairing a LeKiwi-class base with AMD embedded compute and an onboard policy runtime

- **Component / trigger:** LeKiwi (SIGRobotics UIUC / OSS) — Low-cost mobile manipulation reference platform
- **AMD status:** `community` — community-maintained only (nearest: LeKiwi is natively supported in LeRobot which AMD runs on ROCm; the base and arm hardware are host-agnostic)
- **Who is blocked:** Labs and students building low-cost mobile manipulators who default to Jetson for the onboard box
- **Action:** Publish a LeKiwi plus Ryzen AI Embedded reference integration with onboard ROCm/NPU policy inference numbers
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://github.com/huggingface/lerobot
- **Component ref:** https://github.com/SIGRobotics-UIUC/LeKiwi

#### [P1 · 24] Legged and humanoid platforms ship Jetson-class onboard compute, and there is no AMD-validated onboard integration or ROCm policy runtime for Unitree-class robots

- **Component / trigger:** unitree_sdk2 / unitree_ros2 (Unitree Robotics) — Vendor SDK for legged and humanoid robots
- **AMD status:** `community` — community-maintained only (nearest: unitree_sdk2 is C++/DDS and builds on AMD x86_64 Linux hosts; Unitree G1 is listed as LeRobot-supported hardware)
- **Who is blocked:** Humanoid and quadruped researchers who want AMD silicon on the robot rather than only in the training cluster
- **Action:** Demonstrate unitree_sdk2 low-level control plus a ROCm/NPU VLA policy loop on a Ryzen AI Embedded compute payload and publish the loop rates
- **Scores:** openness 2 · fit 2 · leverage 3 · evidence 2 · confidence med
- **Evidence:** https://github.com/unitreerobotics/unitree_sdk2
- **Component ref:** https://github.com/unitreerobotics/unitree_sdk2

#### [P1 · 24] No AMD-validated CAN-FD and torque-control host stack or latency characterization for backdrivable QDD research arms

- **Component / trigger:** OpenArm 2 (Enactic / WowRobo) — Research-grade open bimanual arm platform
- **AMD status:** `community` — community-maintained only (nearest: OpenARM is a natively supported LeRobot device and LeRobot policies train and run on ROCm per AMD blogs)
- **Who is blocked:** Research groups standardizing on 7-DoF backdrivable arms who need a deterministic host for high-rate torque control
- **Action:** Validate a CAN-FD OpenArm control loop on Kria/Ryzen AI Embedded and publish jitter numbers against an x86 plus USB-CAN baseline
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://www.roboticscenter.ai/state-of-robotics-2026
- **Component ref:** https://openelab.io/blogs/learn/lerobot-hardware-buying-guide-so-arm101-vs-koch-v1-1-vs-openarm-vs-lekiwi-vs-xlerobot

#### [P1 · 24] No sustained AMD technical presence at ROSCon (tutorials, workshop, archived accelerated-robotics talks) comparable to the incumbent accelerator vendor

- **Component / trigger:** ROSCon (Open Robotics / OSRA) — Annual developer conference for the ecosystem
- **AMD status:** `partial` — partial / in progress (nearest: AMD Robotics Innovation Challenge with MassRobotics, whose winners showcase at ROSCon, plus Kria kit distribution)
- **Who is blocked:** ROS developers whose default mental model of hardware acceleration is formed at ROSCon and its talk archive
- **Action:** Submit a ROSCon workshop on ROCm and Kria accelerated ROS 2 nodes with runnable material published alongside the talk
- **Scores:** openness 3 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** https://www.massrobotics.org/amd-and-massrobotics-announce-winners-of-the-amd-robotics-innovation-challenge/
- **Component ref:** https://roscon.ros.org/

#### [P1 · 18] No AMD hardware or ROCm-variant jobs in the public ROS 2 build and release farm so accelerated packages never get regression-tested at release time

- **Component / trigger:** ROS 2 build farm (build.ros2.org) (Open Robotics / OSS) — Continuous build and release farm for ROS
- **AMD status:** `partial` — partial / in progress (nearest: ROCm release CI and AMD Developer Cloud build infrastructure used internally for ROCm packages)
- **Who is blocked:** ROS package maintainers who cannot get AMD build status and users who hit breakage only at runtime
- **Action:** Donate one MI-class and one Ryzen AI Embedded node to the ROS build farm and add a nightly ROCm job
- **Scores:** openness 3 · fit 2 · leverage 3 · evidence 1 · confidence low
- **Evidence:** https://build.ros2.org/
- **Component ref:** https://build.ros2.org/

#### [P2 · 16] No one-click cloud deployment of GPU simulation workstations on AMD instances

- **Component / trigger:** IsaacAutomator (NVIDIA) — Cloud deployment of simulation workstations
- **AMD status:** `partial` — partial / in progress (nearest: AMD Developer Cloud GPU instances used for LeRobot Pi0 training)
- **Who is blocked:** Teams wanting cloud sim or RL farms without local Instinct hardware
- **Action:** Publish Terraform and CLI recipes that stand up a ROCm simulation workstation on a major cloud
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence low
- **Evidence:** https://rocm.blogs.amd.com/artificial-intelligence/rocm-blogsblogsartificial-in/README.html
- **Component ref:** https://github.com/isaac-sim/IsaacAutomator

#### [P2 · 16] No robotics-specific AMD developer portal or forum surface

- **Component / trigger:** (whitespace) accelerator robotics developer portal (NONE) — robotics developer forum / docs portal for a non-NVIDIA accelerator
- **AMD status:** `none` — no AMD path (nearest: ROCm docs exist but are not robotics-facing)
- **Who is blocked:** developers looking for a robotics entry point into AMD
- **Action:** Create a robotics landing surface rather than scattering content across ROCm docs
- **Scores:** openness 2 · fit 2 · leverage 2 · evidence 2 · confidence med
- **Evidence:** prior:flow_graph/robotics-ecosystem/gap_register.md#GAP-17
- **Component ref:** derived:grid-sweep

## Unresolved (coverage debt)

These were enumerated but not settled. They are *not* claims of a gap — they are the honest remainder.

- `C165` RT-1-X / RT-2-X (L3) — RT-1-X checkpoints open; RT-2-X not released
- `C163` RDT-1B (L3) — no evidence found either way
- `C203` PROFINET IRT (L0) — Isochronous real-time class
- `C242` IEC 62443 (L5) — Security levels for OT and robot cells
- `C191` VxWorks (L0) — Proprietary; aerospace and industrial robot arms

