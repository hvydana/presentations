# Pre-trained EfficientDet NvImageNet Backbones
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_efficientdet_tf2_nvimagenet

## Description/Overview
"Pre-trained EfficientNet backbone weights trained on NvImageNet to facilitate transfer learning using TAO Toolkit." These are feature extractors based on the EfficientNet architecture designed for object detection applications.

## Use Case
Object detection that "can detect one or multiple objects in a frame" and "places bounding boxes around the object." Applicable for smart cities, retail, healthcare, and industrial inspection.

## Model Architecture
"The models in this instance are feature extractors based on the EfficientNet architecture." Six backbone versions are supported: efficientnet-b0, efficientnet-b1, efficientnet-b2, efficientnet-b3, efficientnet-b4, and efficientnet-b5.

## Input/Output Format
Models expect data in COCO format for training with the EfficientDet application in TAO Toolkit.

## Training Data
Trained on NVImageNet-v2.

## Intended Users
Developers using NVIDIA's Train Adapt Optimize (TAO) Toolkit for customizing pre-trained models with their own data.

## License
"This work is licensed under the Creative Commons Attribution 4.0 International License." Full details available at: http://creativecommons.org/licenses/by/4.0/

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest Version: efficientnet-b0 | Updated: April 26, 2024 UTC | Compressed Size: 45.6 MB

## Getting Started Instructions
1. Install NGC CLI from ngc.nvidia.com
2. Run: `ngc config set`
3. Download model: `ngc registry model download-version nvidia/tao/pretrained_efficientde_tf2:<template> --dest <path>`
4. Configure NGC API key and download sample notebooks via NGC
5. Run Jupyter notebook on local or remote machine
