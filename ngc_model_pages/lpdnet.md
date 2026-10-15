# LPDNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/lpdnet

## Model Name
**LPDNet** (License Plate Detection Network)

## Description/Overview
"LPDNet detects license plates from an image. This model is ready for commercial use."

## Use Case
Primary use case involves detecting license plates in color (RGB) images from photos and videos using appropriate video/image decoding and preprocessing.

## Model Architecture
Two architecture options are available:

- **DetectNet_v2**: CNN-based GridBox object detection using ResNet18 as feature extractor. Divides input images into grids predicting normalized bounding-box parameters (xc, yc, w, h) and confidence values per output class.

- **YOLOv4-tiny**: Based on YOLOv4-tiny detector with CSPDarkNet_tiny as feature extractor.

## Input Format
**Type**: RGB color images
**Dimensions**:
- US license plates: 640 x 480 x 3 (W x H x C)
- Chinese license plates: 720 x 1168 x 3 (W x H x C)

**Channel Ordering**: NCHW format
**Input Scale**: 1/255.0
**Mean Subtraction**: None

## Output Format
"Label: Text String(s); Bounding Box: (x-coordinate, y-coordinate, width, height), Confidence Scores: Floating Point"

Outputs include license plate labels, bounding box coordinates, and confidence scores.

## Training Data
Two datasets were used:

1. Internal proprietary dataset containing 45,000 US license plate images captured at various angles and illumination levels from vehicle dash and side cameras

2. 172,000 images from the "Chinese City Parking Dataset (CCPD)" from a provincial capital of China

## Evaluation Dataset
42,000 images from CCPD dataset at different angles, illumination, and sharpness levels.

## Performance Metrics

**Version 1.0 (DetectNet_v2) Accuracy**:
- USA unpruned: 98.58%
- USA pruned: 98.46%
- CCPD unpruned: 99.24%
- CCPD pruned: 99.22%

**Version 2.0 (YOLOv4-Tiny) Accuracy**:
- USA trainable: 99.53%
- USA deployable: 99.61%
- CCPD trainable: 99.99%
- CCPD deployable: 99.98%

## Intended Users
Developers using NVIDIA hardware and software, specifically those working with:
- TAO (Train Adapt Optimize) Toolkit
- DeepStream SDK
- TensorRT

## Supported Hardware
Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, and Volta architectures

## Supported Operating Systems
- Linux
- Linux 4 Tegra

## License
No specific license name or clause is displayed on this page. Terms of use are referenced but the actual license text is not provided in the model card.

## Tags
Computer Vision, CV, Deep Learning, TAO, TAO Toolkit, NSPECT-2A4D-MPST

## Version Information
**Latest Version**: pruned_v2.2.1
**Updated**: November 12, 2024 UTC
**Compressed Size**: 1.7 MB

## Available Model Versions
- unpruned_v1.0 (ResNet18, intended for training)
- pruned_v1.0 (ResNet18 deployment)
- unpruned_v2.0 (YOLOv4-Tiny, intended for training)
- pruned_v2.0, v2.1, v2.2, v2.2.1, v2.3, v2.3.1 (deployment variants)

## Getting Started / Download Instructions

**For Training (Version 1.0 DetectNet_v2)**:
Include pretrained model in TAO experiment spec configuration:
```
model_config {
  num_layers: 18
  pretrained_model_file: "/path/to/the/model.tlt"
  use_batch_norm: true
  arch: "resnet"
}
```

**For Deployment with DeepStream**:
1. Download and install DeepStream SDK
2. Create label file: `echo lpd > labels_lpdnet.txt`
3. Configure inference settings in `config_infer_secondary_lpdnet.txt`
4. Run: `deepstream-app -c deepstream_app_source1_trafficcamnet_lpdnet.txt`

**Model Decryption Key**: `nvidia_tlt`

## Technical Resources
- TAO Toolkit documentation and getting started guide available at developer.nvidia.com
- DeepStream SDK: https://developer.nvidia.com/deepstream-sdk
- Related blog: "Creating a real-time license plate detection and recognition app"

## Ethical Considerations
"NVIDIA believes Trustworthy AI is a shared responsibility." Model Card++ sections address explainability, bias, safety, security, and privacy considerations.
