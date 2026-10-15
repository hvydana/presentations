# CitySemSegFormer
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/citysemsegformer

## Model Name
CitySemSegFormer

## Description/Overview
"CitySemSegFormer segments classes within an image. This model segments the urban cityscapes into 19 classes" including road, sidewalk, building, vegetation, sky, person, car, bicycle, and others. The model is ready for commercial use.

## Use Case
The primary use case involves "segmenting urban city classes in a color (RGB) image. The model can be used to segment urban city transport/setting from photos and videos." It performs semantic segmentation rather than instance-based segmentation.

## Model Architecture
- **Architecture Type:** Transformer
- **Network Architecture:** SegFormer

## Input/Output Format

**Input:**
- Type: Image
- Format: RGB (Red, Green, Blue)
- Resolution: 1024x1024x3 (Width x Height x Channels)
- Parameters: 3D

**Output:**
- Type: Semantic Segmentation Mask
- Format: 2D vector

## Training Data
A proprietary dataset of 178,000 images collected from dashcams (128,000 images at 5ft height) and traffic signal content (50,000 images). Data was automatically collected via sensors and human-labeled. The dataset includes 2.8M cars, 773,500 persons, 538,127 road signs, and 65,000 two-wheelers.

## Evaluation Data
"300 proprietary images that were hand labeled across a variety of environments."

## Intended Users
Developers using "NVIDIA Hardware and Software" who work with TAO Toolkit, DeepStream SDK, or TensorRT for deployment on NVIDIA GPUs and Jetson devices.

## License
No specific license name or clause is displayed on this page.

## Tags
AI, Computer Vision, Deep Learning, DeepStream, Smart City, TAO Toolkit, Transfer Learning

## Version/Date
- **Latest Version:** deployable_onnx_v1.0
- **Updated:** November 27, 2024 UTC
- **Compressed Size:** 331.08 MB

## Download/Getting Started Instructions
Use "the NGC CLI to download" or access via the NGC Catalog. For DeepStream deployment (v6.1+), download the SDK, then use provided config files (nvinfer_config.txt and labels.txt) with the command: `ds-tao-segmentation -c configs/segformer_tao/nvinfer_config.txt -i [input_file]`
