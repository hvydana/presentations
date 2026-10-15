# MONAI Lung Nodule CT Detection Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_lung_nodule_ct_detection

## Model Name
**monai_lung_nodule_ct_detection**

## Description/Overview
"A pre-trained model for volumetric (3D) detection of the lung nodule from CT image." The model employs RetinaNet architecture trained on the LUNA16 dataset.

## Use Case
Detection of lung lesions in CT scans, identifying locations of possible nodules and assigning probability scores to potential findings.

## Model Architecture
RetinaNet-based 3D detection network (Lin et al., "Focal loss for dense object detection," ICCV 2017)

**Input Specifications:**
- Single channel 3D CT patches
- Actual model input: 192 x 192 x 80

**Output Specifications:**
- Training mode: Dictionary containing classification and box regression loss
- Evaluation mode: List of dictionaries with predicted boxes, classification labels, and scores

## Training Data
LUNA16 dataset (based on LIDC-IDRI database), which contains "a public dataset of CT lung nodule detection" with raw CT scans. The model was trained on fold 0 using 10-fold cross-validation splits.

**Data Resampling:** Images resampled to 0.703125 x 0.703125 x 1.25 mm voxel size

## Training Configuration
- GPU: Minimum 16GB memory (32GB required for TensorRT export)
- Optimizer: Adam
- Learning Rate: 1e-2
- Loss Functions: BCE loss and L1 loss
- AMP: Enabled

## Performance Metrics
Using COCO evaluation: mAP=0.852, mAR=0.998, AP(IoU=0.1)=0.858, AR(IoU=0.1)=1.0

TensorRT acceleration provides "speedup ratios observed on an A100 80G GPU" with up to 11.88x improvement for model computation in fp16 mode.

## Intended Users
Researchers and practitioners working with medical imaging, particularly those using MONAI toolkit for lung nodule detection applications.

## License
**Apache License 2.0**

"Licensed under the Apache License, Version 2.0 (the 'License'); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0"

## Tags
Bundle, CT, Deep Learning, Detection, Healthcare, Imaging, Lung, Medical, Medical Imaging, MONAI, PyTorch

## Version/Date
**Version:** 0.6.8
**Updated:** November 12, 2024 UTC
**Compressed Size:** 159.82 MB

## Getting Started Instructions

**Execute training:**
```
python -m monai.bundle run --config_file configs/train.json
```

**Execute evaluation:**
```
python -m monai.bundle run --config_file "['configs/train.json','configs/evaluate.json']"
```

**Execute inference (resampled images):**
```
python -m monai.bundle run --config_file configs/inference.json
```

**Export to TensorRT (fp32/fp16):**
```
python -m monai.bundle trt_export --net_id network_def --filepath models/model_trt.ts --ckpt_file models/model.pt --meta_file configs/metadata.json --config_file configs/inference.json --precision <fp32/fp16> --input_shape "[1, 1, 512, 512, 192]" --use_onnx "True" --use_trace "True" --onnx_output_names "['output_0', 'output_1', 'output_2', 'output_3', 'output_4', 'output_5']" --network_def#use_list_output "True"
```

**Inference with TensorRT model:**
```
python -m monai.bundle run --config_file "['configs/inference.json', 'configs/inference_trt.json']"
```
