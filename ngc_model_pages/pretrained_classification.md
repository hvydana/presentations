# TAO Pretrained Classification
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_classification

## Description/Overview
"TAO Pretrained Classification classifies an image into one of the designated thousands of classes. This model is ready for commercial use."

## Use Cases
The model supports applications in:
- Computer Vision (CV)
- Industrial inspection
- Public safety
- Retail analytics
- Smart cities and infrastructure
- DeepStream deployment scenarios

## Model Architecture
**Architecture Type:** Convolutional Neural Network (CNN)

**Available Network Architectures:**
- ResNet (10, 18, 34, 50, 101)
- VGG (16, 19)
- GoogleNet
- MobileNet (v1, v2)
- SqueezeNet
- DarkNet (19, 53)
- EfficientNet (b0, b1 with SWISH and ReLU variants)
- CSPDarkNet (19, 53, tiny)

## Input/Output Format

**Input:**
- Type: Image
- Format: RGB (Red, Green, Blue)
- Parameters: 4D tensor with batch size
- Resolution range: Minimum B × 3 × 224 × 224; Maximum B × 3 × 518 × 518

**Output:**
- Type: Label(s)
- Format: "Text String" category labels for designated classes

## Training Data
"Roughly 400,000 images and 7,000 validation images across thousands of classes" from the Google OpenImages Version 3 dataset. Annotations verified by Google in-house annotators and crowdsourced verification via the Image Labeler app.

## Evaluation Data
"15,000 test images from Google OpenImages Version Three (3) dataset."

## Intended Users
Developers and organizations implementing vision AI applications across industrial, retail, public safety, and smart infrastructure sectors using NVIDIA's TAO Toolkit.

## License
No specific license name or clause is displayed in the fetched content. The page references "Terms of Use" but does not provide explicit licensing information for the model itself.

## Tags
CV, DeepStream, EfficientNet, Industrial, Inspection, Metropolis, Public Safety, ResNet, Retail, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit, VGG

## Version/Date
**Latest Version:** cspdarknet_tiny
**Updated:** August 19, 2024 UTC
**Compressed Size:** 28.57 MB

## Download & Getting Started Instructions

1. Install NGC CLI from ngc.nvidia.com
2. Configure CLI: `ngc config set`
3. List supported backbones: `ngc registry model list nvidia/tao_pretrained_classification:*`
4. Download model: `ngc registry model download-version nvidia/tao_pretrained_classification:<template> --dest <path>`

**For Jupyter Notebooks:**
- Obtain NGC API key from setup tab
- Download samples: `ngc registry resource download-version "nvidia/tao_cv_samples:v1.0.2"`
- Launch Jupyter: `jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root`

## Software Integration
- **Runtime Engine:** TAO 5.2, DeepStream 6.1 or later
- **Supported Hardware:** Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta
- **Supported OS:** Linux, Linux 4 Tegra
