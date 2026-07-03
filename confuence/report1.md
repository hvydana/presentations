 s**Model:** smolVLA_v1 | **Date:** 13-06-2026 | **Training:** 1000 episodes | **Validation:** 9 episodes (seen speaker)

**Model path (v1.0):** [smolvla-gesture6-trainall-evaltest.zip](https://amdcloud-my.sharepoint.com/:u:/r/personal/hvydana_amd_com/Documents/smolvla-gesture6-trainall-evaltest.zip?csf=1&web=1&e=cpcDRTYour)

**Runs dir:** [OneDrive](https://amdcloud-my.sharepoint.com/:u:/g/personal/hvydana_amd_com/IQDZtrdZYZgERa9tPqIn3WW4AYe1h6lp0RDg9Z51rLdpefY?e=suJiCy) — contains states (`.npz`), `loss.json` (MAE per joint/episode, median latency), `summary_*.csv`

**Release commit:** `physical_ai_sdk/models/smolVLA` @ `7d9e868c351812287fef3a7339ab8ae78f85c4a3`
**Release tarball:** [smolvla-15fps-robotics-release-v1.0_13_06_2026.tar.gz](https://github.com/AMD-PAVS/physical_ai_sdk/archive/refs/tags/smolvla-15fps-robotics-release-v1.0_13_06_2026.tar.gz)
**Dataset:** [AMD-PAVS-AI/multigesture_mimic_test](https://huggingface.co/datasets/AMD-PAVS-AI/multigesture_mimic_test) | **HF token:** `REDACTED`
**Reproduce:** `/home/amd/Workspace/physical_ai_sdk/models/smolVLA/README_lerobot_setup.md`

---

> **Note on max-action states:** In the RTC model the cap is 10 states, but if the model produces the next state before that, the previous one is overwritten. This means faster models (lower latency) tend to show better MAE numbers.

---

## 1. Main Results — `compile-mode=max-autotune-no-cudagraphs, compile_full=1`

| FPS (appx) | Precision | max-Action States | Avg MAE | Latency (ms) |
|:-----------:|:---------:|:-----------------:|:-------:|:------------:|
| 30          | fp32      | 1                 | 3.059   | --           |
| 15          | fp16      | 1                 | 3.276   | 65.16        |
| 15          | fp16      | 2                 | 3.426   | 65.37        |
| 15          | fp16      | 4                 | 4.291   | 67.72        |
| 15          | fp16      | 5                 | 4.558   | 66.81        |
| 15          | fp16      | 10                | 4.795   | 65.00        |
| 15          | fp16      | 20                | 6.206   | 64.05        |
| 15          | fp16      | 30                | 12.090  | 62.83        |
| 15          | fp16      | 40                | 23.070  | 64.33        |

> **Warning:** Using too many action steps from stale predictions can cause very bad performance (MAE → 20+).

---

## 2. Compile Mode Comparison — Action Steps = 10

### fp16

| Compile Mode                            | Avg MAE | Standalone Latency (ms) |
|:----------------------------------------|:-------:|:-----------------------:|
| compile-max-autotune-no-cudagraphs-full | 4.795   | 65.00                   |
| compile-reduce-overhead                 | 4.596   | 77.20                   |
| eager                                   | 5.018   | 85.61                   |

### bf16

| Compile Mode                            | Avg MAE | Standalone Latency (ms) |
|:----------------------------------------|:-------:|:-----------------------:|
| compile-max-autotune-no-cudagraphs-full | 5.005   | 103.25                  |
| compile-reduce-overhead                 | 4.747   | 76.81                   |
| eager                                   | 5.028   | 90.53                   |

> Compiling the full graph for the first time (cold start) takes significant extra time.

---

## Raw Tables

> For analysis of trends and compiled-graph properties. Very detailed — not meant for general reading.

### compile-max-autotune-no-cudagraphs

| Precision | Action Steps | Avg MAE | Standalone Latency (ms) |
|:---------:|:------------:|:-------:|:-----------------------:|
| fp16      | 1            | 3.359   | 80.47                   |
| fp16      | 2            | 3.525   | 84.11                   |
| fp16      | 4            | 4.053   | 80.45                   |
| fp16      | 5            | 4.388   | 79.91                   |
| fp16      | 10           | 4.833   | 76.65                   |
| fp16      | 20           | 6.137   | 75.58                   |
| fp16      | 30           | 12.311  | 75.56                   |

### compile-max-autotune-no-cudagraphs-full

| Precision | Action Steps | Avg MAE | Standalone Latency (ms) |
|:---------:|:------------:|:-------:|:-----------------------:|
| bf16      | 1            | 3.467   | 105.54                  |
| bf16      | 2            | 3.571   | 108.77                  |
| bf16      | 4            | 4.497   | 107.97                  |
| bf16      | 5            | 4.655   | 104.94                  |
| bf16      | 10           | 5.005   | 103.25                  |
| bf16      | 20           | 5.971   | 102.56                  |
| bf16      | 30           | 12.132  | 103.15                  |
| bf16      | 40           | 23.545  | 101.88                  |
| fp16      | 1            | 3.276   | 65.16                   |
| fp16      | 2            | 3.426   | 65.37                   |
| fp16      | 4            | 4.291   | 67.72                   |
| fp16      | 5            | 4.558   | 66.81                   |
| fp16      | 10           | 4.795   | 65.00                   |
| fp16      | 20           | 6.206   | 64.05                   |
| fp16      | 30           | 12.090  | 62.83                   |
| fp16      | 40           | 23.070  | 64.33                   |

### compile-reduce-overhead

| Precision | Action Steps | Avg MAE | Standalone Latency (ms) |
|:---------:|:------------:|:-------:|:-----------------------:|
| bf16      | 1            | 3.388   | 87.32                   |
| bf16      | 2            | 3.371   | 87.33                   |
| bf16      | 4            | 3.878   | 86.01                   |
| bf16      | 5            | 4.392   | 87.26                   |
| bf16      | 10           | 4.747   | 76.81                   |
| bf16      | 20           | 5.717   | 78.12                   |
| bf16      | 30           | 12.137  | 77.34                   |
| bf16      | 40           | 23.439  | 77.07                   |
| fp16      | 1            | 3.374   | 81.76                   |
| fp16      | 2            | 3.508   | 86.46                   |
| fp16      | 4            | 4.258   | 83.47                   |
| fp16      | 5            | 4.276   | 86.53                   |
| fp16      | 10           | 5.319   | 133.17                  |
| fp16      | 20           | 5.674   | 76.02                   |
| fp16      | 30           | 12.091  | 75.02                   |
| fp16      | 40           | 23.293  | 75.55                   |

### eager

| Precision | Action Steps | Avg MAE | Standalone Latency (ms) |
|:---------:|:------------:|:-------:|:-----------------------:|
| bf16      | 1            | 3.560   | 120.36                  |
| bf16      | 2            | 3.641   | 120.88                  |
| bf16      | 4            | 4.427   | 120.32                  |
| bf16      | 5            | 4.978   | 118.56                  |
| bf16      | 10           | 5.028   | 90.53                   |
| bf16      | 20           | 6.225   | 95.42                   |
| bf16      | 30           | 13.150  | 94.72                   |
| bf16      | 40           | 23.886  | 94.55                   |
| fp16      | 1            | 3.534   | 108.23                  |
| fp16      | 2            | 3.714   | 119.86                  |
| fp16      | 4            | 4.424   | 121.00                  |
| fp16      | 5            | 5.144   | 116.59                  |
| fp16      | 10           | 5.018   | 85.61                   |
| fp16      | 20           | 6.377   | 93.27                   |
| fp16      | 30           | 13.194  | 92.83                   |
| fp16      | 40           | 23.836  | 93.25                   |

---

## Configs Sorted by Latency (Fastest First)

> **Observation:** Fastest model tends to be more accurate.

### Action Steps = 2

| Config               | Standalone Latency (ms) | Avg MAE |
|:---------------------|:-----------------------:|:-------:|
| nocg-full/fp16       | 65.37                   | 3.426   |
| nocg/fp16            | 84.11                   | 3.525   |
| nocg/bf16            | 85.09                   | 3.379   |
| reduce-overhead/fp16 | 86.46                   | 3.508   |
| reduce-overhead/bf16 | 87.33                   | 3.371   |
| nocg-full/bf16       | 108.77                  | 3.571   |
| eager/fp16           | 119.86                  | 3.714   |
| eager/bf16           | 120.88                  | 3.641   |

### Action Steps = 4

| Config               | Standalone Latency (ms) | Avg MAE |
|:---------------------|:-----------------------:|:-------:|
| nocg-full/fp16       | 67.72                   | 4.291   |
| nocg/fp16            | 80.45                   | 4.053   |
| nocg/bf16            | 83.10                   | 4.086   |
| reduce-overhead/fp16 | 83.47                   | 4.258   |
| reduce-overhead/bf16 | 86.01                   | 3.878   |
| nocg-full/bf16       | 107.97                  | 4.497   |
| eager/bf16           | 120.32                  | 4.427   |
| eager/fp16           | 121.00                  | 4.424   |

### Action Steps = 10

| Config               | Standalone Latency (ms) | Avg MAE |
|:---------------------|:-----------------------:|:-------:|
| nocg-full/fp16       | 65.00                   | 4.795   |
| nocg/fp16            | 76.65                   | 4.833   |
| reduce-overhead/bf16 | 76.81                   | 4.747   |
| reduce-overhead/fp16 | 76.85                   | 4.596   |
| nocg/bf16            | 78.98                   | 4.705   |
| eager/fp16           | 85.61                   | 5.018   |
| eager/bf16           | 90.53                   | 5.028   |
| nocg-full/bf16       | 103.25                  | 5.005   |