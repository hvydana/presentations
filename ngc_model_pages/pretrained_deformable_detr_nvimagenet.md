# Pre-trained Deformable DETR NvImageNet Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_deformable_detr_nvimagenet

## Model Name
Pre-trained Deformable DETR NvImageNet weights

## Description/Overview
"Pre-trained deformable_detr weights trained on NvImageNet to facilitate transfer learning using TAO Toolkit." These are backbone models designed to serve as starting points for object detection tasks using the Deformable-DETR architecture within NVIDIA's TAO ecosystem.

## Use Case
Object detection applications that identify and localize individual objects in images by placing bounding boxes around them. Suitable for deployment in smart cities, retail, healthcare, and industrial inspection scenarios.

## Model Architecture
Deformable-DETR based object detection networks supporting multiple backbone architectures:
- ResNet-50
- GCViT variants (xxTiny, xTiny, Tiny, Small, Base, Large, Large_384)

## Available Model Versions
- **resnet50**: "NVImageNet pre-trained ResNet-50 model for finetune"
- **gcvit_xxtiny_nvimagenet** through **gcvit_base_nvimagenet**: Various Vision Transformer variants pre-trained on NVImageNet

## Training Data
NvImageNet dataset, "permitted for commercial uses"

## Input/Output Format
Configuration requires specification in TAO experiment spec file with parameters including backbone selection, feature levels, encoder/decoder layers, and dropout ratio.

## Intended Users
Developers using NVIDIA's Train Adapt Optimize (TAO) Toolkit for customizing pre-trained models with proprietary data for transfer learning applications.

## License
"Model EULA" covering use rights. Users must accept terms at: https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest Version: resnet50 | Updated: October 16, 2023 UTC | Compressed Size: 292.89 MB

## Download Instructions
"Use the NGC CLI to download" (specific command shown as copyable snippet on NGC platform at the model's registry page)
