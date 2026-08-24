# Iteration Log — Robotics & Physical AI KFG
*Mode: checkpoint | Iteration cap: 3 new iterations (iter 2–4) | Topic: robotics-ecosystem | Started: 2026-08-11 | Resumed: 2026-08-13*

---

## Setup

- Seed reports ingested: 3 (initial), 4 (resumed 2026-08-13)
  - `embedded-robotics-market-analysis.md`
  - `physical-ai-robotics-market-analysis.md`
  - `robotics-ecosystem-market-analysis.md`
  - `edge-inference-ecosystem-for-robotics-market-analysis.md` ← added 2026-08-13
- Seed nodes created: N1–N8 (initial), N30–N34 (new from edge-inference)
- Question nodes created: N9–N16 (initial), N36–N40 (new from edge-inference)
- Max iterations: 3 new checkpoint iterations (checkpoint pause after each)

---

## Iteration 1 — Question Scoring

Scoring axes (1–3 each, max 12):
- **A** = AMD leverage (would the answer reveal something AMD can act on?)
- **B** = Gap size / whitespace (does it point at an unserved layer/segment?)
- **C** = Novelty / branching (opens a new direction vs. confirms a known one?)
- **E** = Evidence thinness (current claim under-cited or speculative?)

| Node | Question (shortened) | A | B | C | E | Total |
|------|---------------------|---|---|---|---|-------|
| N11 | How many devs blocked by Warp gap? | 3 | 3 | 2 | 3 | **11** ← selected |
| N14 | What abstracts AMD FPGA into dev-friendly SDK? | 3 | 2 | 3 | 3 | **11** ← selected |
| N9  | Which upper-stack layer most defensible for non-NVIDIA? | 3 | 3 | 2 | 2 | **10** ← selected |
| N12 | What would AMD synthetic data factory require? | 3 | 3 | 2 | 2 | **10** ← selected |
| N15 | Who's winning tactile sensing? AMD play? | 1 | 3 | 3 | 3 | **10** |
| N10 | Western actuator whitespace for AMD? | 1 | 3 | 3 | 2 | **9** |
| N13 | Open data infra investments for AMD? | 3 | 3 | 1 | 2 | **9** |
| N16 | Which ROCm packages for robotics adoption? | 3 | 2 | 2 | 2 | **9** |

**Frontier selected (top 4 — highest AMD leverage among tied scores):** N11, N14, N9, N12

Tie-breaking rationale: N15 dropped (AMD leverage=1); N10/N13/N16 dropped (lower AMD leverage or novelty).

---

## Iteration 1 — Agents Dispatched

| Agent | Frontier node | Question |
|-------|--------------|---------|
| Agent-1 | N11 | How many devs blocked from AMD by the Warp gap? |
| Agent-2 | N14 | What abstracts AMD's FPGA advantage into a dev-friendly SDK? |
| Agent-3 | N9  | Which upper-stack layer is most defensible for non-NVIDIA? |
| Agent-4 | N12 | What would an AMD-compatible synthetic data factory require? |

Status: **COMPLETE** (2026-08-11)

---

## Iteration 1 — Results

| Metric | Value |
|--------|-------|
| Nodes added | 13 (N17–N29) |
| Findings (new Finding nodes) | 3 (N17, N21, N26) |
| GAP-AMD nodes confirmed | 3 (N18, N22, N27) |
| New Q nodes surfaced | 7 (N19, N20, N23, N24, N25, N28, N29) |
| Agent failures | 1 — N11 agent hit AMD internal API auth wall (market_fetch.py requires NTID header for physicalAI app); re-dispatch iter 2 using WebSearch-only |
| Convergence check | Not triggered — 3 new GAP-AMD nodes added, 7 new high-scoring questions surfaced |

**Key findings summary:**
- N17 (from N14): AMD has all SDK building blocks for FPGA abstraction (KRS, REP 2008, Xen) — the gap is last-mile packaging, not foundational engineering. ROBOTCORE (Zynq UltraScale+) is a licensable blueprint.
- N21 (from N9): LeRobot/HuggingFace gateway is AMD's highest-feasibility entry point. Working code exists (Pi0, SmolVLA on ROCm) but no model cards are in the LeRobot hub — AMD is invisible at the callsite.
- N26 (from N12): AMD's synthetic data factory path is technically confirmed — Genesis World 1.0 Quadrants is ROCm-native; Cosmos 3 Nano is community-confirmed on ROCm. The gap is orchestration and first-party ownership, not components.

---

## Iteration 2 — Frontier (Re-scored with new nodes from edge-inference)

Scoring all open Q nodes including N36–N40 from edge-inference:

| Node | Question (shortened) | A | B | C | E | Total |
|------|---------------------|---|---|---|---|-------|
| N29 | AMD partnership/acquisition of Genesis AI for integrated data factory? | 3 | 3 | 3 | 3 | **12** ← selected |
| N39 | AMD as compute anchor for physical AI edge data center / fleet deployment? | 3 | 3 | 3 | 3 | **12** ← selected |
| N11 | How many devs blocked by Warp gap? (re-dispatch WebSearch-only) | 3 | 3 | 2 | 3 | **11** ← selected |
| N28 | MI300X throughput ceiling for Genesis+Cosmos Nano? | 3 | 3 | 2 | 3 | **11** ← selected |
| N38 | AMD Windows ROCm/DirectML path + excluded industrial market size? | 3 | 3 | 3 | 2 | **11** ← selected |
| N36 | Vendor-neutral C++ robotics inference SDK (TensorRT-equivalent)? | 3 | 3 | 3 | 2 | **11** |
| N23 | AMD SmolVLA checkpoint in LeRobot hub shifts developer defaults? | 3 | 3 | 2 | 2 | **10** |
| N25 | First-mover window for Cosmos 3 ROCm before NVIDIA integration ships? | 3 | 2 | 3 | 2 | **10** |
| N19 | Pre-baked bitstream + ROS 2 hardware_interface plugin for Kria? | 3 | 2 | 3 | 2 | **10** |
| N20 | ROBOTCORE layer OEM'd by AMD as first-party FPGA SDK? | 3 | 2 | 3 | 2 | **10** |
| N24 | Which CUDA ops block official Cosmos 3 ROCm guide? | 3 | 2 | 2 | 3 | **10** |
| N37 | Hardware-agnostic 50+ Hz fast-path policy runtime on AMD? | 3 | 2 | 2 | 3 | **10** |
| N15 | Who's winning tactile sensing? AMD play? | 1 | 3 | 3 | 3 | **10** |
| N40 | MI300X HBM3 enabling MARL past 100 agents? | 2 | 2 | 2 | 3 | **9** |
| N10 | Western actuator whitespace for AMD? | 1 | 3 | 3 | 2 | **9** |
| N13 | Open data infra investments for AMD? | 3 | 3 | 1 | 2 | **9** |
| N16 | Which ROCm packages for robotics adoption? | 3 | 2 | 2 | 2 | **9** |

**Selected frontier (top 5 — dispatching now):** N29, N39, N11, N28, N38

Tie-breaking rationale: N39 and N38 promoted over N36/N23 because they open genuinely new directions (edge data center; Windows industrial market) vs. confirming existing hypotheses.

---

## Iteration 2 — Results

| Metric | Value |
|--------|-------|
| Nodes added | 14 (N41–N54) |
| Findings (new Finding nodes) | 5 (N41, N43, N45, N47, N49) |
| GAP-AMD nodes confirmed | 4 (N42, N44, N46, N48) |
| New Q nodes surfaced | 5 (N50, N51, N52, N53, N54) |
| Agent failures | 0 — all 5 returned findings |
| Convergence check | Not triggered — 4 new GAP-AMD nodes, 5 new high-scoring questions surfaced |

**Key findings summary:**
- N41 (from N11): Warp blocked developer population quantified: Newton adopted by Boston Dynamics, Agility, Figure AI, Toyota, Skild, Samsung; 7K+5.1K+1.7K stars across Warp/Newton/cuRobo; no ROCm commitment from any entity → Linux Foundation path available for AMD
- N43 (from N29): AMD already technically engaged with Genesis (ROCm tutorial Feb 2026 + arXiv paper); Genesis raising $500M at $3B; not in AMD Robotics Partner Network → free enrollment closes the gap before NVIDIA moves
- N45 (from N38): AMD ROCm 7.2.2 (CES 2026) unified Windows+Linux — Windows exclusion technically closed; but AMD has zero certified design wins in $6.1B Windows industrial IPC market → gap is commercial certification (Beckhoff, Siemens, Advantech)
- N47 (from N39): ModulEdge robot fleet edge data centers exclusively NVIDIA but GPU-agnostic container (ModulEdge=enclosure, Comino=GPU); OTA market $1.42B→$5.85B by 2033; AMD MI300X fits the compute tier → MI300X qualification is the displacement vector
- N49 (from N28): MI300X ~50–80% of H100 per-GPU for Cosmos pipeline; NATTEN sparse attention (Cosmos Predict2 2.6×) locked to Hopper/Blackwell; AMD VSA (3.31×, MLPerf 6.0) potentially closeable; Wan2.2 is AMD-native alternative

---

## Iteration 3 — Proposed Frontier

Scoring all open Q nodes (updated after Iteration 2 findings):

| Node | Question (shortened) | A | B | C | E | Total |
|------|---------------------|---|---|---|---|-------|
| N50 | AMD Linux Foundation Newton member contributing ROCm Warp backend? | 3 | 3 | 3 | 3 | **12** ← proposed |
| N51 | Genesis Robotics Partner Network enrollment before NVIDIA claims Genesis? | 3 | 3 | 3 | 3 | **12** ← proposed |
| N52 | IPC vendor cert for AMD X100 Windows ML — which vendors, what process? | 3 | 3 | 3 | 2 | **11** ← proposed |
| N53 | MI300X + ROCm vLLM qualifying inside ModulEdge GPU-agnostic containers? | 3 | 3 | 3 | 2 | **11** ← proposed |
| N54 | Wan2.2 as drop-in for Cosmos Predict2 in AMD data pipeline? | 3 | 2 | 3 | 2 | **10** ← proposed |
| N23 | AMD SmolVLA checkpoint in LeRobot hub shifts developer defaults? | 3 | 3 | 2 | 2 | **10** |
| N25 | First-mover window for Cosmos 3 ROCm before NVIDIA integration ships? | 3 | 2 | 3 | 2 | **10** |
| N19 | Pre-baked bitstream + ROS 2 hardware_interface plugin for Kria? | 3 | 2 | 3 | 2 | **10** |
| N24 | Which CUDA ops block official Cosmos 3 ROCm guide? | 3 | 2 | 2 | 3 | **10** |
| N37 | Hardware-agnostic 50+ Hz fast-path policy runtime on AMD? | 3 | 2 | 2 | 3 | **10** |

**Proposed frontier (top 5):** N50, N51, N52, N53, N54

---

## Iteration 3 — Results

| Metric | Value |
|--------|-------|
| Nodes added | 12 (N55–N66) |
| Findings (new Finding nodes) | 5 (N55, N56, N57, N58, N59) |
| GAP-AMD nodes confirmed | 2 (N60, N61) |
| Pivot nodes | 1 (N62 — upgrades N48 confidence M→H) |
| New Q nodes surfaced | 4 (N63, N64, N65, N66) |
| Agent failures | 0 — all 5 returned findings |
| Convergence check | Not triggered — 2 new GAP-AMD nodes, 4 new Q nodes scoring ≥10; cap (iter 2–4) not yet reached (iter 3 = 2nd of 3) |

**Key findings summary:**
- N55 (from N50): MJWarp differentiable physics not complete on ANY backend (CUDA or ROCm); AMD JAX/XLA on ROCm = co-architect path alongside DeepMind, not a port
- N56 (from N51): Genesis Eno robot (LG CNS June 2026 deployment, end-2026 commercial launch) is choosing silicon NOW; no NVIDIA-Genesis relationship; "Eno on AMD" guide > enrollment as commercial signal
- N57 (from N52): AMD CPU wins in TwinCAT ML (CX20x3, K4131-Px) confirmed; zero GPU/NPU certified wins in TwinCAT 3 ML or SIMATIC Edge — specific certification action identified
- N58 (from N53): **Key pivot** — Comino already lists AMD MI300X; ModulEdge blog already lists AMD GPU servers; gap is GTM-only (not OEM engineering)
- N59 (from N54): MI355X 93–108% of B200 on Wan2.2 (MLPerf 6.0); FlashAR+ one-engineer AMD CK port confirmed feasible; Wan2.2 = AMD-native Cosmos alternative

---

## Iteration 4 — Proposed Frontier (STEERED — Edge Inference SDK Focus)

**User steering applied (2026-08-13):** Redirect Iteration 4 from DeepMind/Eno/ModulEdge co-announces to **edge inference SDK gap analysis** — specifically: (1) which NVIDIA-proprietary edge inference SDKs have no AMD/open equivalent, and (2) which open-source inference frameworks need minimal AMD contributions to enable community self-porting. N63/N64/N65/N66 deferred (gaps confirmed H-confidence; actions are BD/GTM, not research). N36/N37 promoted to active dispatch alongside new N67/N68/N69.

Scoring all open Q nodes after steering:

| Node | Question (shortened) | A | B | C | E | Total |
|------|---------------------|---|---|---|---|-------|
| N67 | NVIDIA-proprietary edge inference SDKs (TensorRT/GXF/Isaac) with no open/AMD equivalent? | 3 | 3 | 3 | 3 | **12** ← selected |
| N68 | Open-source inference (ONNX RT/TVM/MLC-LLM): minimal AMD contribution to unlock community self-porting? | 3 | 3 | 3 | 3 | **12** ← selected |
| N69 | MLC-LLM/Apache TVM on AMD Kria/Versal NPU — what backend is missing for edge robotics? | 3 | 3 | 3 | 2 | **11** ← selected |
| N36 | Vendor-neutral C++ robotics inference SDK (TensorRT-equivalent)? | 3 | 3 | 3 | 2 | **11** ← selected |
| N63 | AMD approach DeepMind researcher-level for differentiable MJWarp co-authorship? | 3 | 3 | 3 | 2 | **11** — deferred |
| N64 | Min viable "Eno on AMD" guide: Ryzen AI MAX + Real2Sim2Real + GENE-26.5? | 3 | 3 | 3 | 2 | **11** — deferred |
| N37 | Hardware-agnostic 50+ Hz fast-path policy runtime on AMD? | 3 | 2 | 2 | 3 | **10** ← selected |
| N65 | Co-announce AMD MI300X in ModulEdge units alongside NVIDIA B200? | 3 | 3 | 2 | 2 | **10** — deferred |
| N66 | AMD Composable Kernel port of FlashAR+ anti-diagonal decoding on CDNA3? | 3 | 2 | 3 | 2 | **10** — deferred |
| N23 | AMD SmolVLA checkpoint in LeRobot hub shifts developer defaults? | 3 | 3 | 2 | 2 | **10** |
| N25 | First-mover window for Cosmos 3 ROCm before NVIDIA integration ships? | 3 | 2 | 3 | 2 | **10** |
| N19 | Pre-baked bitstream + ROS 2 hardware_interface plugin for Kria? | 3 | 2 | 3 | 2 | **10** |
| N24 | Which CUDA ops block official Cosmos 3 ROCm guide? | 3 | 2 | 2 | 3 | **10** |

**Selected frontier (top 5 — steered to edge inference):** N67, N68, N69, N36, N37

Steering rationale: N67/N68 are new nodes targeting exactly the taxonomy the user named (NVIDIA-locked vs. open-source-with-AMD-gap). N69 narrows MLC-LLM/TVM to AMD embedded NPU targets (Kria/Versal) — highest-leverage community porting entry point. N36/N37 (from edge-inference seed report, scored 11 and 10 in Iteration 2 frontier but never dispatched) align perfectly with the new direction. N63/N64/N65/N66 are deferred — their gaps are confirmed H-confidence in the register and the actions are GTM/BD (not research); they don't need another agent round to be actionable.

---

## Iteration 4 — Results

| Metric | Value |
|--------|-------|
| Nodes added | 14 (N70–N83) |
| Findings (new Finding nodes) | 5 (N70, N71, N72, N73, N74) |
| GAP-AMD nodes confirmed | 4 (N76, N77, N78, N79) |
| Pivot nodes | 1 (N75 — N70's GXF/NITROS "unbuilt gap" reframed to "AMD announce-ready asset") |
| New Q nodes surfaced | 4 (N80, N81, N82, N83) — post-cap, not dispatched |
| Agent failures | 0 — all 5 returned findings |
| Convergence check | **TRIGGERED — max iterations reached** (cap=3 new; iter 4 = 3rd new) → Step 8 finalization executed |

**Key findings summary:**
- N70 (from N67): NVIDIA-proprietary SDK taxonomy confirmed — Isaac ROS+NITROS/GXF (2M+ devs, 7K+ Jetson Orin commercial customers), TensorRT Plugin API (20–30% throughput advantage batch 1–4; no ROCm), cuVSLAM (232–386 fps CUDA-only), GXF — all have no open/AMD equivalent. **User correction pivoted GXF/NITROS finding:** AMD is internally building a ROCm-native NITROS equivalent feature-comparable to Isaac ROS 4.0 on Jetson Thor (unreleased) → N75 Pivot
- N71 (from N68): MLC-LLM already ships ROCm nightly wheels (`mlc-llm-nightly-rocm62`) and auto-detects AMD GPU targets at compile time; gap is one GitHub Actions CI pipeline for LeRobot VLA models (ACT/SmolVLA/Pi0) on AMD gfx942/gfx1100 + publishing `.so` to `mlc.ai/wheels` — the community self-porting flywheel path; vLLM CI playbook applies directly
- N72 (from N69): MLC-LLM confirmed not deploying on AMD Kria/Versal; Vitis AI DPU is CNN-only; Versal AIE requires MLIR-AIE/closed AMD AIE Compiler with no TVM frontend; AMD Vitis AI 3.0+ pivoted to ONNX Runtime VOE; Ryzen AI NPU via ONNX RT VOE is the more tractable embedded path
- N73 (from N36): No vendor-neutral robotics inference SDK exists combining all 5 criteria — Kenning (ROS2+INT8, no VLA) + vla.cpp (VLA+GGUF, no ROS2; ~150ms) are near-misses each missing 2+ criteria; AMD is one ROCm EP to vla.cpp + one Kenning VLA backend from assembling the alternative
- N74 (from N37): Zero published Hz benchmarks for VLA inference on AMD; AMD internal claim "~92ms/~10 Hz" on Ryzen AI MAX+ 395 (unverified); VOTE-MLP4 on Jetson AGX Orin = 55.57 Hz (NVIDIA); action expert stage is memory-bound (54 FLOPs/Byte) — AMD MI300X 5.3 TB/s HBM3 vs. Jetson 204 GB/s LPDDR5 advantage entirely unmeasured

---

## Finalization — Step 8 (Cap Reached; 2026-08-13)

**Convergence trigger:** Max iterations reached (cap=3 new; iterations 2–4 completed).

**Total graph summary:**
- Seed reports ingested: 4
- Total nodes created: 83 (N1–N83, excluding N35 which was never used)
- Seed nodes: 13 (N1–N8, N30–N34)
- Q nodes: 33 (including deferred and post-cap)
- Finding nodes: 15
- GAP-AMD nodes: 13 confirmed
- Pivot nodes: 3 (N62, N75, and implicit in N55)
- Agents dispatched: 20 total (5 × Iter 1 partial + 5 × Iter 2 + 5 × Iter 3 + 5 × Iter 4; 1 Iter 1 failure re-dispatched in Iter 2)

See `gap_register.md` for the finalized synthesis, 13 confirmed gaps, and top 10 ranked actions.

---

## Convergence Tracking

| Criterion | Iteration 1 | Iteration 2 | Iteration 3 | Iteration 4 |
|-----------|------------|------------|------------|------------|
| Max iterations reached (cap=3 new) | No | No | No (2nd of 3) | **YES — TRIGGERED** |
| Frontier starvation (<2 Q ≥ 8/12) | No | No (5 @ ≥10) | No (4 @ ≥10) | No (4 post-cap Q ≥ 10) |
| Gap saturation (no new GAP-AMD for 2 rounds) | No (3 added) | No (4 added) | No (2 added) | No (4 added) |
| Evidence saturation | No | No | No | No |
| User stop | No | No | No | No |