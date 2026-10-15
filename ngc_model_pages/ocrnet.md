# Optical Character Recognition (OCRNet)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/ocrnet

## Model Name
Optical Character Recognition (OCRNet)

## Description/Overview
"Model to recognise characters from a preceding OCDNet model." The OCRNet is an optical character recognition network that recognizes characters from gray images.

## Use Case
The primary use case is character recognition from text images, particularly from scene text detection outputs. The model processes cropped text regions and outputs recognized character sequences.

## Model Architecture
- **Architecture Type:** Convolutional Neural Network (CNN)
- **Backbone Options:**
  - ResNet50 (v1.0 versions)
  - FAN (Fully Attentional Networks) for v2.0+ versions
- **Multiple versions optimized for different domains:** scene text recognition and PCB text recognition

## Input/Output Format

**Input:**
- Type: Gray images
- Format: 1 × 32 × 100 (C H W) for v1.0 models
- Format: 1 × 64 × 200 (C H W) for v2.0+ models

**Output:**
- Type: Sequence of characters
- Format: Character ID sequence converted to text strings

## Training Data
The model was trained on the Uber-Text and TextOCR datasets, containing 805,007 training images and 24,388 validation images. Only alphanumeric text with maximum length of 25 characters was retained.

## Intended Users
Developers and organizations using NVIDIA hardware and software ecosystem who need character recognition capabilities.

## License
"License to use these models is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these licenses" (https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)

## Tags
- AI
- Computer Vision
- Deep Learning
- DeepStream
- TAO Toolkit
- Transfer Learning

## Version/Date
Latest: deployable_v2.1.1 | Updated: November 27, 2024 UTC | Compressed Size: 44.27 MB

## Getting Started
Models can be deployed using TensorRT, NVIDIA TAO Toolkit, DeepStream SDK, or nvOCDR. The TAO Container provides Jupyter notebooks for retraining on custom datasets.
