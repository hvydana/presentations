## Model Card — smolVLA_v1

### Model

**Model:** smolVLA_v1
**Path:** [OneDrive](https://amdcloud-my.sharepoint.com/:u:/g/personal/hvydana_amd_com/IQAYhhsqkucCRo9G2cctrW5vASmjdj3VblPt-T-BZCZNlvI?e=iKNqxm)

- **Base model:** `smolvla-gesture6-trainall-evaltest\checkpoints\014000\pretrained_model`
- **Performant model:** `smolvla-gesture6-trainall-evaltest\checkpoints\014000\pretrained_model\compile_cache`

### Training Data

1000 episodes from:

1. `AMD-PAVS-AI/multigesture_mimic_train`
2. `AMD-PAVS-AI/extended_gesture_mimic_train`
3. `AMD-PAVS-AI/Action-per-video-multigesture-mimic`
4. `AMD-PAVS-AI/Action-per-video-multigesture-mimic-2`
5. `AMD-PAVS-AI/Action-per-video-multigesture-mimic-3`

### Validation Data

9 episodes (Seen Speaker)
**Dataset:** [AMD-PAVS-AI/multigesture_mimic_test](https://huggingface.co/datasets/AMD-PAVS-AI/multigesture_mimic_test)
**HF token:** `REDACTED`

### Released Features

- Diffusion steps reduced from 30 → 2
- Optimized graph execution mode (replaces default eager execution)
- Lower precision: FP32 → FP16

**GitHub:** [smolvla-15fps-robotics-release-v1.0_13_06_2026](https://github.com/AMD-PAVS/physical_ai_sdk/releases/tag/smolvla-15fps-robotics-release-v1.0_13_06_2026)

---

### Validation Results

| FPS | Latency | Action States | MAE Score |
|:---:|:-------:|:-------------:|:---------:|
| 30  | --      | 1             | 3.00      |
| 15  | ~65 ms  | 1             | 3.27      |
| 15  | ~65 ms  | 2             | 3.43      |
| 15  | ~65 ms  | 4             | 4.29      |
| 15  | ~65 ms  | 5             | 4.55      |
| 15  | ~65 ms  | 10            | 4.79      |
| 15  | ~65 ms  | 20            | 6.20      |
| 15  | ~65 ms  | 30            | 12.09     |
| 15  | ~65 ms  | 40            | 23.00     |

> **Note:** 30 FPS row is fp32, not real-time on GPK. 15 FPS rows are fp16.