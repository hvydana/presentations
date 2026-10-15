# MONAI Pancreas CT DiNTS Segmentation Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_pancreas_ct_dints_segmentation

## Model Name
**monai_pancreas_ct_dints_segmentation**

## Description/Overview
"A neural architecture search algorithm for volumetric (3D) segmentation of the pancreas and pancreatic tumor from CT image." The model employs the DiNTS neural architecture search technique for identifying optimal network configurations.

## Use Case
Medical image segmentation focused on identifying pancreatic structures and tumors within CT scans, applicable to clinical diagnostic workflows and research applications.

## Model Architecture
The system uses a neural architecture search (NAS) algorithm called DiNTS to discover optimal network topologies. The architecture discovery process involves:
- **AMP**: True
- **Optimizer**: SGD
- **Initial Learning Rate**: 0.025
- **Loss Function**: DiceCELoss

The model formulates pancreas segmentation as "voxel-wise 3-class classification" with soft dice loss and cross-entropy optimization.

## Input/Output Format

**Input:**
- Single channel: CT image
- Model input dimensions: 96 x 96 x 96

**Output:**
- Three channels representing:
  - Label 0: Background (everything else)
  - Label 1: Pancreas
  - Label 2: Pancreatic tumor

## Training Data
The dataset originates from the "Medical Segmentation Decathlon" Pancreas Task:
- **Size**: 420 3D volumes (282 training, 139 testing)
- **Source**: Memorial Sloan Kettering Cancer Center
- **Modality**: Portal venous phase CT
- **Challenge**: Label imbalance with large background, medium pancreas, and small tumor structures

## Intended Users
Medical imaging researchers, clinical institutions, and healthcare organizations utilizing deep learning for diagnostic pancreatic imaging analysis.

## Performance
The model achieves "a mean dice score of 0.62." TensorRT acceleration demonstrates speedup ratios up to 5.03x for model computation on A100 80G GPUs.

## License
**Apache License 2.0**

"Copyright (c) MONAI Consortium. Licensed under the Apache License, Version 2.0... you may not use this file except in compliance with the License."

Full license available at: http://www.apache.org/licenses/LICENSE-2.0

## Tags
Bundle, CT, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, Pancreas, PyTorch, Segmentation

## Version and Date
- **Latest Version**: 0.5.0
- **Updated**: November 12, 2024 UTC
- **Compressed Size**: 1.03 GB

## Getting Started Instructions

**Model Searching (Single GPU):**
```
python -m scripts.search run --config_file configs/search.yaml
```

**Multi-GPU Model Searching (Recommended):**
```
torchrun --nnodes=1 --nproc_per_node=8 -m scripts.search run --config_file configs/search.yaml
```

**Training:**
```
python -m monai.bundle run --config_file configs/train.yaml
```

**Multi-GPU Training:**
```
torchrun --nnodes=1 --nproc_per_node=8 -m monai.bundle run --config_file "['configs/train.yaml','configs/multi_gpu_train.yaml']"
```

**Inference:**
```
python -m monai.bundle run --config_file configs/inference.yaml
```

**TensorRT Export (FP32/FP16):**
```
python -m monai.bundle trt_export --net_id network_def --filepath models/model_trt.ts --ckpt_file models/model.pt --meta_file configs/metadata.json --config_file configs/inference.yaml --precision <fp32/fp16> --use_trace "True" --dynamic_batchsize "[1, 4, 8]" --converter_kwargs "{'truncate_long_and_double':True, 'torch_executed_ops': ['aten::upsample_trilinear3d']}"
```

**Data Preparation:**
```
python scripts/prepare_datalist.py --path /path-to-Task07_Pancreas/ --output configs/dataset_0.json
```
