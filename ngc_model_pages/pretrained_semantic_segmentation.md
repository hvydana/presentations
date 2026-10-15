# TAO Pretrained Semantic Segmentation
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_semantic_segmentation

## Description/Overview
"The Semantic Segmentation model assigns every pixel in an image to a class label." This model is ready for commercial use and facilitates transfer learning via NVIDIA's Transfer Learning Toolkit.

## Use Cases
The model supports applications in:
- Computer Vision (CV)
- Industrial inspection
- Public safety
- Smart cities and spaces
- Retail analytics
- Robotics
- Smart infrastructure

## Model Architecture
**Architecture Type:** UNet

**Supported Backbones:**
- ResNet10, ResNet18, ResNet34, ResNet50, ResNet101
- VGG16, VGG19

## Input/Output Format

**Input:** RGB images with specifications of "Minimum Resolution: B X 3 X 224 X 224; Maximum Resolution: B X 3 X 518 X 518"

**Output:** "Label: Text String(s); Semantic Segmentation Mask: 2D"

## Training Data
Roughly 400,000 images across thousands of classes from the Google OpenImages Version Three dataset, with annotations from Google in-house staff and crowdsourced verification.

## Evaluation Data
15,000 test images from Google OpenImages Version Three dataset.

## Intended Users
Developers using TAO Toolkit for custom model training and deployment.

## License
Not explicitly stated in the fetched page content.

## Tags
CV, DeepStream, Industrial, Inspection, Metropolis, Public Safety, Retail, Robotics, Semantic Segmentation, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit, UNet

## Version/Date
Latest Version: vgg19 | Updated: August 19, 2024 UTC | Compressed Size: 515.09 MB

## Getting Started Instructions

1. Install NGC CLI from ngc.nvidia.com
2. Configure with: `ngc config set`
3. Download model: `ngc registry model download-version nvidia/tao/pretrained_semantic_segmentation:<template> --dest <path>`
4. Download sample notebooks: `ngc registry resource download-version "nvidia/tao_cv_samples:v1.0.2"`
5. Run Jupyter: `jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root`

**Runtime:** TAO 5.2, DeepStream 6.1 or later | **Supported Hardware:** Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta
