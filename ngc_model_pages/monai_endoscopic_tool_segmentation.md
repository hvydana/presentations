# MONAI Endoscopic Tool Segmentation Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_endoscopic_tool_segmentation

## Model Name
**monai_endoscopic_tool_segmentation**

## Description/Overview
"A pre-trained model for the endoscopic tool segmentation task, trained using a flexible unet structure with an efficientnet-b2 as the backbone and a UNet architecture as the decoder."

## Use Case
Medical image segmentation specifically for identifying surgical instruments in endoscopic video frames.

## Model Architecture
- **Encoder:** EfficientNet-B2
- **Decoder:** UNet architecture
- **Input dimensions:** 736 x 480 x 3 (three-channel video frame)
- **Output:** Two channels (Label 1: tools; Label 0: everything else)

## Training Data
Private surgical samples from Activ Surgical. The documentation notes that public datasets like EndoVis 2017 can be used as alternatives since the proprietary data is unavailable.

## Training Configuration
- GPU requirement: At least 12GB memory
- Optimizer: Adam
- Learning rate: 1e-4
- Dataset manager: CacheDataset

## Performance Metrics
- Mean IoU score: 0.86
- TensorRT support available with measured speedup ratios on A100 80G GPU

## Intended Users
Researchers and developers working on medical imaging and surgical tool segmentation tasks.

## License
"Licensed under the Apache License, Version 2.0" with full text available at http://www.apache.org/licenses/LICENSE-2.0

## Tags
Bundle, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, PyTorch, Segmentation

## Version & Date
- Latest version: 0.6.0
- Updated: November 12, 2024 UTC
- Compressed size: 88.54 MB

## Getting Started Instructions

**Execute training:**
```
python -m monai.bundle run --config_file configs/train.json
```

**Execute inference:**
```
python -m monai.bundle run --config_file configs/inference.json
```

**Export to TensorRT (fp32/fp16):**
```
python -m monai.bundle trt_export --net_id network_def --filepath models/model_trt.ts --ckpt_file models/model.pt --meta_file configs/metadata.json --config_file configs/inference.json --precision <fp32/fp16>
```

The model files (PyTorch and TorchScript) are hosted on Google Drive and referenced in the `large_files.yml` configuration file.
