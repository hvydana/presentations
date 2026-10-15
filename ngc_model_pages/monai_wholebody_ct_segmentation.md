# MONAI Whole Body CT Segmentation Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_wholebody_ct_segmentation

## Model Name
**monai_wholebody_ct_segmentation**

## Description/Overview
"A pre-trained SegResNet model for volumetric (3D) segmentation of the 104 whole body segments." The model represents an evolution in body CT segmentation, expanding from abdominal multi-organ approaches to hundreds of target anatomies across the entire body.

## Use Case
This model enables automated identification and delineation of 104 anatomical structures within CT scans of the complete body, supporting medical imaging workflows including diagnosis, treatment planning, and research applications.

## Model Architecture
The model employs SegResNet, trained using the TotalSegmentator datasets containing 104 whole-body structures from CT imaging.

## Input/Output Format

**Input:** "One channel - CT image"

**Output:** "105 channels - Label 0: Background (everything else); label 1-105: Foreground classes (104)"

The model generates multi-label segmentation predictions using softmax and argmax operations.

## Training Data
The training dataset comprises "the 104 whole-body structures from the TotalSegmentator released datasets," accessible at https://github.com/wasserth/TotalSegmentator.

## Intended Users
Medical imaging professionals, researchers, and healthcare institutions utilizing CT analysis workflows, particularly those integrating with MONAI Label and 3D Slicer platforms.

## License
**Name:** Apache License, Version 2.0

**Clause/Link:** "Licensed under the Apache License, Version 2.0... You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0"

## Tags
Bundle, CT, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, PyTorch, Segmentation, Whole Body

## Version/Date
**Version:** 0.2.5
**Updated:** November 12, 2024 UTC
**Compressed Size:** 143.54 MB

## Getting Started Instructions

**Training execution:**
```
python -m monai.bundle run --config_file configs/train.json
```

**Inference execution:**
```
python -m monai.bundle run --config_file configs/inference.json
```

**TensorRT export:**
```
python -m monai.bundle trt_export --net_id network_def --filepath models/model_trt.ts --ckpt_file models/model.pt --meta_file configs/metadata.json --config_file configs/inference.json --precision <fp32/fp16> --use_trace "True"
```

Sample datasets are available via Google Drive links provided in the documentation for immediate experimentation.
