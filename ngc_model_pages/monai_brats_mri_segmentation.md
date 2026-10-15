# MONAI BraTS MRI Segmentation Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_brats_mri_segmentation

## Model Name
**monai_brats_mri_segmentation**

## Description/Overview
A pre-trained model designed for volumetric (3D) segmentation of brain tumor subregions from multimodal MRIs, trained on BraTS 2018 data. The model segments three nested primary brain tumor (glioma) subregions: enhancing tumor (ET), tumor core (TC), and whole tumor (WT) using four aligned input MRI scans.

## Use Case
Clinical brain tumor analysis and surgical planning by identifying tumor subregions from MRI imaging data.

## Model Architecture
The model utilizes "a similar approach described in 3D MRI brain tumor segmentation using autoencoder regularization," which was a winning BraTS2018 method. Key specifications:
- **Input dimensions:** 224 x 224 x 144
- **Optimizer:** Adam
- **Learning rate:** 1e-4
- **Loss function:** DiceLoss
- **Precision:** Supports FP32, AMP, and FP16 modes
- **GPU requirement:** At least 16GB of GPU memory

## Input Format
"4 channel aligned MRIs at 1 x 1 x 1 mm":
- T1c
- T1
- T2
- FLAIR

## Output Format
"3 channels":
- Label 0: TC tumor subregion
- Label 1: WT tumor subregion
- Label 2: ET tumor subregion

## Training Data
"The training data is from the Multimodal Brain Tumor Segmentation Challenge (BraTS) 2018" with:
- Target: 3 tumor subregions
- Task: Segmentation
- Modality: MRI
- Size: 285 3D volumes (4 channels each)
- Partition: 200 training, 42 validation, 43 testing studies

## Performance Metrics
Dice scores on validation data:
- Tumor core (TC): 0.8559
- Whole tumor (WT): 0.9026
- Enhancing tumor (ET): 0.7905
- Average: 0.8518

## Intended Users
Healthcare and medical imaging professionals, researchers in brain tumor analysis, and deep learning practitioners working with medical imaging.

## License
**Apache License 2.0**

"Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0"

## Tags
Brain, Bundle, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, MR, Pytorch, Segmentation

## Version & Date
- **Latest Version:** 0.5.2
- **Updated:** November 12, 2024 UTC
- **Compressed Size:** 36.05 MB

## Download/Getting Started
Using NGC CLI for download. Key commands include:

**Training:** `python -m monai.bundle run --config_file configs/train.json`

**Multi-GPU training:** `torchrun --standalone --nnodes=1 --nproc_per_node=8 -m monai.bundle run --config_file "['configs/train.json','configs/multi_gpu_train.json']"`

**Inference:** `python -m monai.bundle run --config_file configs/inference.json`

**TensorRT export:** `python -m monai.bundle trt_export --net_id network_def --filepath models/model_trt.ts --ckpt_file models/model.pt --meta_file configs/metadata.json --config_file configs/inference.json --precision <fp32/fp16>`
