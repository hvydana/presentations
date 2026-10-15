# MONAI Pathology Tumor Detection Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_pathology_tumor_detection

## Model Name
**monai_pathology_tumor_detection**

## Description/Overview
"A pre-trained model for automated detection of metastases in whole-slide histopathology images."

## Use Case
The model performs automated tumor detection in whole-slide images (WSIs) from histopathology samples, identifying areas of metastatic disease.

## Model Architecture
The model is "trained based on ResNet18 with the last fully connected layer replaced by a 1x1 convolution layer." Input dimensions are 224 x 224 x 3 pixels.

## Input/Output Format
**Input:** Histopathology image patches extracted from whole-slide images

**Output:** "A probability number of the input patch being tumor or normal"

## Training Data
The dataset consists of images from the Camelyon-16 Challenge:
- 270 WSIs for training/validation
- 48 WSIs for testing
- Location and annotation information sourced from NCRF repositories

## Training Configuration
- GPU requirement: at least 16 GB memory
- Optimizer: Novograd
- Learning Rate: 1e-3
- Loss function: BCEWithLogitsLoss
- AMP: True
- WSI reader: cuCIM (or OpenSlide for Windows/Mac)

## Performance Metrics
- "0.90 accuracy on validation patches"
- "FROC of 0.72 on the 48 Camelyon testing data"

## Intended Users
Researchers and practitioners in digital pathology and medical imaging analysis requiring automated tumor detection capabilities.

## License
**Apache License 2.0**

"Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License."

Full license available at: http://www.apache.org/licenses/LICENSE-2.0

## Tags
Bundle, Deep Learning, Detection, Healthcare, Imaging, Medical, Medical Imaging, MONAI, Pathology, PyTorch

## Version & Date
**Version:** 0.6.2
**Updated:** November 12, 2024 UTC
**Compressed Size:** 64.45 MB

## Getting Started / Download Instructions

**Download via NGC CLI:**
Use the NGC CLI to download the model from the NVIDIA NGC Catalog.

**Training:**
```
python -m monai.bundle run --config_file configs/train.json
```

**Multi-GPU Training:**
```
torchrun --standalone --nnodes=1 --nproc_per_node=2 -m monai.bundle run --config_file "['configs/train.json','configs/multi_gpu_train.json']"
```

**Inference:**
```
CUDA_LAUNCH_BLOCKING=1 python -m monai.bundle run --config_file configs/inference.json
```

**Evaluate FROC Metric:**
```
cd scripts && source evaluate_froc.sh
```
