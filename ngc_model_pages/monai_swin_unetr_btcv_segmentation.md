# MONAI Swin UNETR BTCV Segmentation Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_swin_unetr_btcv_segmentation

## Model Name
monai_swin_unetr_btcv_segmentation

## Description/Overview
A pre-trained Swin UNETR model designed for "volumetric (3D) multi-organ segmentation using CT images from Beyond the Cranial Vault (BTCV) Segmentation Challenge dataset."

## Use Case
Multi-organ segmentation in abdominal CT imaging for medical applications.

## Model Architecture
The model employs Swin Transformers within a UNETR framework. Input dimensions are 96 × 96 × 96 voxels, processed with AMP enabled, using an Adam optimizer with 2e-4 learning rate.

## Input/Output Format

**Input:** Single channel CT image

**Output:** 14 channels representing:
- 0: Background
- 1: Spleen
- 2: Right Kidney
- 3: Left Kidney
- 4: Gallbladder
- 5: Esophagus
- 6: Liver
- 7: Stomach
- 8: Aorta
- 9: IVC
- 10: Portal and Splenic Veins
- 11: Pancreas
- 12: Right adrenal gland
- 13: Left adrenal gland

## Training Data
The BTCV dataset containing "30 3D volumes (24 Training + 6 Testing)" of abdominal CT scans requiring preprocessing from the source Synapse repository.

## Intended Users
Researchers and developers working with medical imaging segmentation, particularly those using MONAI toolkit.

## Performance
Mean Dice score of 0.82 achieved on validation data with documented training loss curves.

## License
Apache License 2.0. "Licensed under the Apache License, Version 2.0" with full terms available at http://www.apache.org/licenses/LICENSE-2.0

## Tags
Bundle, CT, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, PyTorch, Segmentation

## Version & Date
Version 0.5.6 | Updated November 12, 2024 UTC | Compressed Size: 244.5 MB

## Getting Started Instructions

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
python -m monai.bundle run --config_file configs/inference.json
```

**TensorRT Inference:**
```
python -m monai.bundle run --config_file "['configs/inference.json', 'configs/inference_trt.json']"
```
