# Optical Character Detection (OCDNet)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/ocdnet

## Model Name
**Optical Character Detection** (OCDNet)

## Description/Overview
"Network to detect characters in an image." The model is "an optical characters detection network, which aims to detect text in images." Both trainable and deployable versions are provided, trained on Uber-Text and ICDAR2015 datasets.

## Use Case
The primary use case involves detecting text within images, particularly for optical character recognition applications.

## Model Architecture
The architecture is "based on a relatively sophisticated text detection network called DBNet," which is designed for real-time scene text detection with differentiable binarization. The system "inserts the binarization operation into the segmentation network and jointly optimizes it" to improve foreground/background separation.

## Input/Output Format
- **Input:** "Images of C x H x W (H and W should be multiples of 32.)"
- **Output:** "BBox or polygon coordinates for each detected text in the input image"

## Training Data
Models were trained on two datasets:
- **Uber-Text Dataset:** 107,812 images for training and 10,157 for validation
- **ICDAR2015 Dataset:** 1,000 training images and 500 test images

## Intended Users
Organizations needing text detection capabilities who can work with NVIDIA hardware and software including TAO Toolkit, DeepStream SDK, or TensorRT.

## License
The license is covered by the Model EULA. "By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)."

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
- **Latest Version:** deployable_onnx_v2.4
- **Updated:** November 27, 2024 UTC
- **Compressed Size:** 33.99 MB

## Getting Started/Download Instructions
Use the NGC CLI to download. The model is available through NVIDIA NGC Catalog. Instructions specify using TAO Container, and deployment via DeepStream SDK with detailed documentation at official NVIDIA channels.
