# ReIdentificationNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/reidentificationnet

## Description/Overview
"Re-Identification network to generate embeddings for identifying persons in different scenes."

## Primary Use Case
The model generates embeddings for objects, then performs similarity matching to identify people across different camera views and scenes.

## Model Architecture
- **Type:** Convolutional Neural Network (CNN)
- **Backbone:** ResNet50
- **Feature Dimensions:** Available in 64, 128, 256, 512, 1024, and 2048

## Input Format
- **Type:** Image (Red, Green, Blue)
- **Resolution:** Fixed at B x 3 x 256 x 128 pixels
- **Parameters:** 2D

## Output Format
- **Type:** Embeddings
- **Format:** Numpy (.npy)
- **Precision:** Billionths

## Training Data
The model was trained on:
- 14,737 images from Market-1501 dataset (751 real people)
- 29,533 images of 156 people (148 synthetic) from 2023 AI City Challenge MTMC dataset
- Total: 44,070 training images across 907 identities

## Intended Users
Developers deploying person re-identification applications using NVIDIA hardware and software ecosystems, particularly for smart city and infrastructure monitoring.

## License
No explicit license name or clause was provided in the fetched page content.

## Tags
AI, Computer Vision, Deep Learning, DeepStream, TAO Toolkit, Smart City, Transfer Learning

## Version/Date
- **Latest:** deployable_v1.2 (November 27, 2024)
- **Compressed Size:** 91.93 MB

## Getting Started
Users can deploy via:
- TAO Toolkit (training/fine-tuning)
- DeepStream SDK
- TensorRT
- Triton Inference Server

Model load key: `nvidia_tao`
