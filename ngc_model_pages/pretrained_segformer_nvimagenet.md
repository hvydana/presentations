# Pre-trained SegFormer NvImageNet weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_nvimagenet

## Description/Overview
"Pre-trained SegFormer weights trained on NvImageNet to facilitate transfer learning using TAO Toolkit." These are pretrained weights for the FAN (Fully Attentional Network) family of transformer-based backbone models designed for image classification and downstream computer vision tasks.

## Use Case
The primary application is classifying objects in color (RGB) images from photos and videos. Additionally suitable for downstream tasks including object detection and segmentation. Recommended when test datasets have domain gaps from training data, as FAN provides robustness against various corruptions, noise, and blur.

## Model Architecture
"FAN (Fully Attentional Network) is a transformer-based family of backbone from NVIDIA research that achieves SOTA in robustness against various corruptions." The architecture features an attentional channel processing module enabling robust representation learning.

## Input/Output Format
**Input:** B X 3 X 224 X 224 or B X 3 X 384 X 384 (Batch, Channels, Height, Width)

**Output:** Category labels (1000 classes) for the input image

## Training Data
"The FAN models were trained on the NVImageNet dataset."

## Model Versions
- fan_small_hybrid_nvimagenet (224 resolution)
- fan_base_hybrid_nvimagenet (224 resolution)
- fan_large_hybrid_nvimagenet (224 resolution)

## Intended Users
Developers using NVIDIA Hardware with TAO Toolkit, DeepStream SDK, or TensorRT for transfer learning and edge deployment applications in smart cities, retail, healthcare, and industrial inspection.

## License
"License to use these models is covered by the NVIDIA Open Model License." Full terms available at: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest: fan_large_hybrid_nvimagenet | Updated: October 16, 2023 UTC | Compressed Size: 293.76 MB

## Getting Started
Access the TAO Container at: https://ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit and refer to TAO Toolkit documentation for implementation instructions.
