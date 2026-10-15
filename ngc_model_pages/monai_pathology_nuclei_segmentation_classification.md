# MONAI Pathology Nuclei Segmentation Classification Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_pathology_nuclei_segmentation_classification

## Model Name
**monai_pathology_nuclei_segmentation_classification**

## Description/Overview
A pre-trained model for "simultaneous segmentation and classification of nuclei within multi-tissue histology images based on CoNSeP data." The model employs a two-stage training approach: decoder-only training for 50 epochs using pre-trained weights, followed by 50 epochs of full-layer fine-tuning.

## Use Case
Instance-level nuclei segmentation and nuclei type classification in histopathology RGB images.

## Model Architecture
The architecture supports two training modes:
- **Original mode**: patch_size [270, 270], out_size [80, 80]
- **Fast mode**: patch_size [256, 256], out_size [164, 164]

The model is initialized with pre-trained weights and utilizes a HoVerNetLoss function during training.

## Input/Output Format

**Input:** RGB histopathology images

**Output:** Dictionary containing three predictions:
1. nucleus_prediction: pixel-level nuclei vs. background classification
2. horizontal_vertical: distances from nuclear pixels to mass centers
3. type_prediction: nucleus type classification per pixel

## Training Data
CoNSeP dataset from Warwick University (https://warwick.ac.uk/fac/cross_fac/tia/data/hovernet/):
- 41 image tiles (2009 patches total)
- 27 tiles for training, 14 for testing
- RGB histology images with instance-level nuclei annotations

## Training Configuration
- GPU: ≥24GB memory
- Model input: 256 × 256
- Optimizer: Adam
- Learning rate: 1e-4
- AMP: Enabled
- Dataset manager: CacheDataset

## Performance Metrics (Fast Mode)
- Binary Dice: 0.8291
- Panoptic Quality (PQ): 0.4973
- F1d: 0.7417

## Intended Users
Healthcare and medical imaging professionals using MONAI toolkit for digital pathology applications.

## License
**Apache License 2.0**

"Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License."

Full text available at: http://www.apache.org/licenses/LICENSE-2.0

## Tags
Bundle, Classification, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, Nuclei, PyTorch, Segmentation

## Version & Date
- **Latest Version:** 0.2.6
- **Updated:** November 12, 2024 UTC
- **Compressed Size:** 288.51 MB

## Getting Started

**Download dataset:**
```
wget https://warwick.ac.uk/fac/cross_fac/tia/data/hovernet/consep_dataset.zip
unzip consep_dataset.zip
```

**Prepare patches:**
```
python scripts/prepare_patches.py --root <your consep dataset path>
```

**Run first stage training:**
```
python -m monai.bundle run --config_file configs/train.json --stage 0 --dataset_dir <actual dataset path>
```

**Run second stage training:**
```
python -m monai.bundle run --config_file configs/train.json --network_def#freeze_encoder False --stage 1 --dataset_dir <actual dataset path>
```

**Execute inference:**
```
python -m monai.bundle run --config_file configs/inference.json
```

**TensorRT accelerated inference:**
```
python -m monai.bundle run --config_file "['configs/inference.json', 'configs/inference_trt.json']"
```

## References
Graham, S., Vu, Q.D., Raza, S.E.A., et al. (2019). Hover-Net: Simultaneous segmentation and classification of nuclei in multi-tissue histology images. Medical Image Analysis. https://doi.org/10.1016/j.media.2019.101563
