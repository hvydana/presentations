## Model Card — smolVLA_v1.1

### Model

**Model:** smolVLA_v1.1
**Path:** [MS Teams](https://teams.microsoft.com/l/message/19:6ebf3a72-0355-4dcc-8671-e076bae5a601_d2a8aeb1-8521-4db8-8bd7-d449b9aa36c3@unq.gbl.spaces/1781423333999)

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

- Reduced smolVLA 3-channel processing → single-channel processing
- *(+ all smolVLA_v1 features)*: diffusion steps 30→2, optimized graph execution, FP32→FP16

**GitHub:** [smolvla-15fps-robotics-release-v1.0_13_06_2026](https://github.com/AMD-PAVS/physical_ai_sdk/releases/tag/smolvla-15fps-robotics-release-v1.0_13_06_2026) *(no changes from v1 release)*

---

### Validation Results — v1 vs v1.1

| Action States | FPS v1  | Latency v1 | FPS v1.1 | Latency v1.1 | MAE v1 | MAE v1.1 |
|:-------------:|:-------:|:----------:|:--------:|:------------:|:------:|:--------:|
| 1             | 30      | --         | 30       | ~31 ms       | NA     | 3.08     |
| 1             | 15      | ~65 ms     | 30       | ~31 ms       | 3.27   | 3.08     |
| 2             | 15      | ~65 ms     | 30       | ~31 ms       | 3.43   | 3.26     |
| 4             | 15      | ~65 ms     | 30       | ~31 ms       | 4.29   | 3.71     |
| 5             | 15      | ~65 ms     | 30       | ~31 ms       | 4.55   | 3.89     |
| 10            | 15      | ~65 ms     | 30       | ~31 ms       | 4.79   | 4.66     |
| 20            | 15      | ~65 ms     | 30       | ~31 ms       | 6.20   | 5.87     |
| 30            | 15      | ~65 ms     | 30       | ~31 ms       | 12.09  | 12.02    |
| 40            | 15      | ~65 ms     | 30       | ~31 ms       | 23.00  | 22.57    |