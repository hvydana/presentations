# Pre-trained GCViT NVImageNet Classification Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_gcvit_classification_nvimagenet

## Description/Overview
"Pre-trained GcViT weights trained on NVImageNet to facilitate transfer learning using TAO Toolkit." These are commercial pretrained models from NVIDIA's TAO (Train Adapt Optimize) Toolkit for image classification tasks.

## Use Case
The primary use case involves classifying objects in RGB images from photos and videos. Applications extend to smart cities, retail, healthcare, industrial inspection, and downstream tasks such as object detection.

## Model Architecture
GCViT (Global Context Vision Transformer) represents a transformer-based backbone architecture from NVIDIA research. The model "leverages global context self-attention, joint with standard local self-attention" to model spatial interactions efficiently. Five variants exist: xxTiny, xTiny, Tiny, Small, and Base.

## Input/Output Format

**Input:** B X 3 X 224 X 224 (B C H W)

**Output:** "Category labels (1000 classes) for the input image."

## Training Data
Models were trained on the NVImageNet dataset, which contains categories aligned with ImageNet-1K but sourced from 84 commercially-licensed websites and Bing image search to ensure commercial usability.

## Intended Users
Organizations requiring image classification models compatible with NVIDIA hardware (GPUs and Jetson devices) and software (TAO Toolkit, DeepStream SDK, TensorRT).

## License
"The licenses to use this model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these licenses" (https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
**Latest Version:** gcvit_base_nvimagenet
**Updated:** October 16, 2023 UTC
**Compressed Size:** 319.6 MB

## Getting Started Instructions
Implement pretrained weights in TAO experiments by configuring the `model` and `train` components with checkpoint paths and backbone specifications. For deployment, utilize DeepStream or TensorRT with appropriate documentation references provided in the TAO User Guide.
