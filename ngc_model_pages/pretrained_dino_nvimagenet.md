# Pre-trained DINO NvImageNet Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_dino_nvimagenet

## Model Name
Pre-trained DINO NvImageNet weights

## Description/Overview
"Pre-trained DINO weights trained on NvImageNet to facilitate transfer learning using TAO Toolkit." These are pretrained backbone models for the DINO object detection architecture, available through NVIDIA's NGC catalog.

## Use Case
Object detection in computer vision applications. "Object detection will recognize the individual objects in an image and places bounding boxes around the object." Suitable for smart cities, retail, healthcare, industrial inspection, and related domains.

## Model Architecture
Supported backbones include:
- ResNet-50
- GCViT variants (xxTiny, xTiny, Tiny, Small, Base, Large)
- FAN variants (Tiny, Small, Base, Large Hybrid)

Configuration example specifies: "num_feature_levels: 4, dec_layers: 6, enc_layers: 6, num_queries: 900"

## Training Data
NVImageNet (permitted for commercial uses) and ImageNet22k variants

## Input/Output Format
Not explicitly detailed in provided content

## Intended Users
Developers using NVIDIA's "Train Adapt Optimize (TAO) Toolkit" for customizing pre-trained models with their own datasets.

## License
"The licenses to use this model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these licenses" - [NVIDIA AI Enterprise EULA](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)

## Tags
AI, Computer Vision, Deep Learning, TAO Toolkit, Transfer Learning, Smart City

## Version/Date
Latest Version: resnet50 | Updated: October 16, 2023 UTC | Compressed Size: 292.89 MB

## Download Instructions
Access via NGC CLI tool from NVIDIA NGC catalog at the model page URL
