# MONAI Spleen CT Segmentation Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_spleen_ct_segmentation

## Model Name
**monai_spleen_ct_segmentation**

## Description/Overview
"A pre-trained model for volumetric (3D) segmentation of the spleen from CT images." The model employs the UNet architecture and was trained using the runner-up awarded pipeline from the Medical Segmentation Decathlon Challenge 2018.

## Use Case
Automated identification and segmentation of the spleen organ in computed tomography scans for clinical imaging analysis.

## Model Architecture
UNet-based deep learning architecture optimized for three-dimensional medical image segmentation tasks.

## Input/Output Format

**Input:**
- Single channel CT image with dimensions 96 x 96 x 96 voxels

**Output:**
- Two channels: Label 1 indicates spleen tissue; Label 0 represents all other structures

## Training Data
The Medical Segmentation Decathlon Spleen Task dataset containing:
- 61 total 3D volumes (41 training, 20 testing)
- Source: Memorial Sloan Kettering Cancer Center
- Challenge addressed: "Large-ranging foreground size"

## Training Configuration
- Optimizer: Novograd
- Learning rate: 0.002
- Loss function: DiceCELoss
- Automatic mixed precision (AMP): Enabled
- GPU requirement: minimum 12GB memory
- Performance metric: mean Dice score of 0.961

## Intended Users
Medical imaging professionals, healthcare institutions, and researchers working with CT image analysis and organ segmentation.

## License
**Apache License, Version 2.0** - "Licensed under the Apache License, Version 2.0 (the 'License')" with full text available at: http://www.apache.org/licenses/LICENSE-2.0

## Tags
Bundle, CT, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, PyTorch, Segmentation, Spleen

## Version/Date
Latest Version: 0.5.9 | Updated: November 12, 2024 UTC | Compressed Size: 36.96 MB

## Getting Started Instructions

**Execute training:**
```
python -m monai.bundle run --config_file configs/train.json
```

**Execute inference:**
```
python -m monai.bundle run --config_file configs/inference.json
```

**Export to TensorRT:**
```
python -m monai.bundle trt_export --net_id network_def --filepath models/model_trt.ts --ckpt_file models/model.pt --meta_file configs/metadata.json --config_file configs/inference.json --precision <fp32/fp16> --dynamic_batchsize "[1, 4, 8]" --use_onnx "True" --use_trace "True"
```

Download via NGC CLI available on the model's NGC Catalog page.
