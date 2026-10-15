# ImageNet NV-DINOv2
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/imagenet_nv_dinov2

## Model Name
ImageNet NV-DINOv2

## Description/Overview
"Image Classification is a popular computer vision technique in which an image is classified into one of the designated classes based on the image features."

## Use Case
The model serves multiple purposes: classifying objects from photos and videos, functioning as a foundation model for downstream tasks with limited labeled examples, and enabling edge deployment through DeepStream SDK for video analytics applications.

## Model Architecture
NV-Dinov2 is described as "a visual foundational model trained on NVIDIA proprietary large scale dataset." It employs self-supervised learning combining DINO and iBOT techniques. The specific implementation uses "the NVDinov2 pre-trained ViT-L backbone and fine-tunes a Linear Regression Classifier on ImageNet dataset."

## Input/Output Format

**Input:**
- RGB image dimensions: B X 3 X 224 X 224 or B X 3 X 518 X 518 (NCHW format)
- N = Batch Size, C = 3 channels, H = Height, W = Width

**Output:**
- "1000 x 1 output where each value is the confidence score of respective class"

## Training Data
Pre-training occurred on "NVIDIA proprietary collected data that are of commercial license." Fine-tuning used the "ImageNet1K dataset" for the linear probe head.

## Intended Users
Developers deploying AI applications on NVIDIA hardware, particularly those using DeepStream SDK for video analytics pipelines on edge devices including Jetson platforms.

## License
"Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)"

**License Link:** https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

## Tags
- Computer Vision
- NVIDIA AI
- TAO Toolkit

## Version/Date
**Latest Version:** deployable_v1.1 (Signed)
**Updated:** August 5, 2025 UTC

## Download Instructions
Use NGC CLI to download. Detailed deployment instructions require downloading DeepStream SDK 6.1 and supporting configuration files from NVIDIA-AI-IOT repository, including label files and DeepStream configuration files for integration.
