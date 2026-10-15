# Pre-trained GCViT ImageNet Classification Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_gcvit_classification_imagenet

## Description/Overview
"Image Classification is a popular computer vision technique in which an image is classified into one of the designated classes based on the image features." These pretrained weights facilitate transfer learning using TAO Toolkit.

## Use Case
Primary applications include classifying objects in color (RGB) images from photos and videos. The model is intended for training and fine-tuning with user datasets for image classification tasks, as well as edge deployment.

## Model Architecture
"GCViT (Global Context Vision Transformer) is a transformer-based family of backbone from NVIDIA research that achieves SOTA in ImageNet-1K classification." It leverages global context self-attention combined with standard local self-attention to model both long and short-range spatial interactions effectively.

## Input/Output Format
**Input:**
- B X 3 X 224 X 224 (B C H W)
- B X 3 X 384 X 384 (B C H W) for ImageNet22K trained model

**Output:**
Category labels (1000 classes) for the input image

## Training Data
Most GCViT models were trained on the ImageNet1K dataset. The GCViT-Large variant was trained on ImageNet22k dataset.

## Intended Users
Developers and practitioners requiring NVIDIA hardware and software (TAO Toolkit, DeepStream SDK, or TensorRT) for training, fine-tuning, and deploying vision AI models.

## License
**Name:** Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)

**Link:** https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest Version: gcvit_large_imagenet22k_384
Updated: October 16, 2023 UTC
Compressed Size: 824.03 MB

## Getting Started/Download Instructions
Use NGC CLI to download. Jupyter notebooks available in the TAO container for retraining. Refer to TAO Toolkit User Guide for experiment spec file configuration and deployment documentation.
