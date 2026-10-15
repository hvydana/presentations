# MixNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/mixnet

## Model Name
**MixNet**

## Description/Overview
"MixNet is an optical character detection model that aims to detect text in images." It is specifically designed for accurate detection of challenging scene text in natural images, with particular focus on small and irregularly positioned text under diverse lighting and orientations. The model is ready for commercial and non-commercial use.

## Use Case
"This model can be used in any computer vision application, which aims to detect text characters in images."

## Model Architecture
- **Type:** Convolution Neural Network + Transformer Block
- **Network Basis:** Based on the MixNet architecture from GitHub (D641593/MixNet)
- **Key Features:**
  - FSNet (Feature Shuffle Network) backbone with novel feature shuffling strategy across multiple scales
  - CTBlock (Central Transformer Block) exploiting 1D manifold constraint of scene text by focusing on center line features

## Input/Output Format

**Input:**
- Type: Image
- Format: "Red, Green, Blue (RGB)"
- Parameters: Two-Dimensional (2D)
- Requirement: "Width and height are multiples of 32"

**Output:**
- Type: Image
- Format: "Red, Green, Blue (RGB)"
- Parameters: Two-Dimensional (2D)
- Description: "Spatial maps or coordinates indicating detected text regions"

## Training Data
Total: 77,000 images across 3 datasets
- ICDAR2015 training dataset (oversampled to 20K images)
- Uber-Text dataset (41,304 images from filtered train_4Kx4K and train_1Kx1K subsets)
- Synthetic dataset based on SynthText (15,005 generated images)

## Evaluation Data
- ICDAR15 test dataset (500 images)
- Uber-Text 1Kx1K dataset (7,461 images)

**Performance Metrics (F1-Score):**
- MixNet on ICDAR15: 86.5%
- MixNet on Uber-Text: 88.0%

## Intended Users
Developers and organizations seeking to deploy text detection capabilities in computer vision applications, particularly those using NVIDIA hardware and software ecosystems.

## License
**Name:** NVIDIA Open Model License

**Exact License Link/Clause:** "License to use these models is covered by the NVIDIA Open Model License. By downloading the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)."

## Tags/Labels
- AI
- English
- Object Detection
- Smart Cities / Spaces
- TAO Toolkit

## Version & Date
- **Latest Version:** deployable_v1.0
- **Updated:** August 5, 2025 UTC
- **Release Date:** NGC [06/30/2025]
- **Compressed Size:** 112.63 MB

## Download & Getting Started Instructions

**Download via NGC CLI:**
The page indicates using the NGC CLI to download, with a "Copied!" option provided (exact command not shown in excerpt).

**Runtime & Compatibility:**
- Runtime Engine: TAO 5.5.0
- Supported Hardware: NVIDIA Ampere, Jetson, Hopper, Volta
- Operating System: Linux
- Model Format: ONNX (deployable version)

**Deployment Options:**
"The `deployable` models can be deployed in TensorRT and nvOCDR, or onnxruntime" or with the NVIDIA-Optical-Character-Detection-and-Recognition-Solution referenced on GitHub.

**Reference Implementation:**
"Please refer to the [C++ Sample](https://github.com/NVIDIA-AI-IOT/NVIDIA-Optical-Character-Detection-and-Recognition-Solution/tree/tao-5.5-ocr-v3)" for usage instructions with nvOCDR.

## Notable Limitations
The model's "generalization performance may be inadequate in scenarios that differ significantly from the training data, such as images containing numerous small text elements on PCB boards." Fine-tuning with domain-specific data is recommended for specialized applications.
