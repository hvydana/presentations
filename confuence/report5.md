## Model Card — smolVLA_v3.0

### Model

**Model:** smolVLA_v3.0
**Path:** [OneDrive](https://amdcloud-my.sharepoint.com/:u:/r/personal/hvydana_amd_com/Documents/AAI_Model_Release/smolVLA_3.0/smolvla-v3.0.zip?csf=1&web=1&e=VFtrSi)

- **Base model:** `smolvla-v3.0/009000/pretrained_model`
- **Performant model:** `smolvla-v3.0/009000/pretrained_model\compile_cache`

### Training Data

2000 episodes from:

1. `AMD-PAVS-AI/multigesture_mimic_train`
2. `AMD-PAVS-AI/extended_gesture_mimic_train`
3. `AMD-PAVS-AI/Action-per-video-multigesture-mimic`
4. `AMD-PAVS-AI/Action-per-video-multigesture-mimic-2`
5. `AMD-PAVS-AI/Action-per-video-multigesture-mimic-3`
6. `AMD-PAVS-AI/Action-per-video-multigesture-mimic-4`
7. `AMD-PAVS-AI/Action-per-video-multigesture-mimic-3-gradient-yolo`
8. `AMD-PAVS-AI/Action-per-video-multigesture-mimic-4-gradient-yolo`

### Validation Data

10 episodes (Seen Speaker)
**Dataset:** [AMD-PAVS-AI/multigesture_mimic_test](https://huggingface.co/datasets/AMD-PAVS-AI/multigesture_mimic_test)
**HF token:** `REDACTED`

### Released Features

- Trained with 2k RAW dataset
- Finetuned on gradient-background data (YOLO used for background segmentation)
- *(+ all smolVLA_v2 features)*: single-channel processing, diffusion steps 30→2, optimized graph execution, FP32→FP16

**GitHub:** [smolvla-15fps-robotics-release-v1.0_13_06_2026](https://github.com/AMD-PAVS/physical_ai_sdk/releases/tag/smolvla-15fps-robotics-release-v1.0_13_06_2026)

---

### Validation Results — v1.1 vs v2 (MAE without Wrist Roll, 30 FPS ~31 ms)

| Action States | MAE v1.1 | MAE v2 |
|:-------------:|:--------:|:------:|
| 1             | 2.08     | 2.05   |
| 2             | 2.26     | 2.26   |
| 4             | 2.65     | 2.68   |
| 5             | 3.18     | 2.97   |
| 10            | 3.94     | 2.78   |
| 20            | 4.87     | 4.06   |
| 30            | 10.76    | 10.82  |
| 40            | 18.84    | 18.86  |