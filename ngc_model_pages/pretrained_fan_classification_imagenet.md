# Pre-trained FAN based ImageNet Classification Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_fan_classification_imagenet

## Description/Overview
"Pre-trained FAN weights trained on ImageNet to facilitate transfer learning using TAO Toolkit." These weights serve as starting points for the classification application within NVIDIA's Train Adapt Optimize toolkit.

## Use Case
The primary applications include classifying objects in RGB images from photos and videos. The models are designed for object detection, classification, and segmentation tasks across various domains including smart cities, retail, healthcare, and industrial inspection.

## Model Architecture
FAN (Fully Attentional Network) represents "a transformer-based family of backbone from NVIDIA research that achieves SOTA in robustness against various corruptions." The architecture features an attentional channel processing module that enables robust representation learning with strong generalization to new domains and resilience to noise and blur.

## Input/Output Format
**Input:**
- B X 3 X 224 X 224 (B C H W)
- B X 3 X 384 X 384 (B C H W)

**Output:** Category labels (1000 classes) for the input image

## Training Data
Models were trained on ImageNet1K and ImageNet22K datasets.

## Intended Users
Organizations requiring image classification with robust performance across domain variations. Users must have NVIDIA hardware and software (TAO Toolkit, DeepStream SDK, or TensorRT).

## License
Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0). Link to full license: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, TAO Toolkit, Transfer Learning

## Version/Date
Latest: fan_hybrid_Xlarge_in22k | Updated October 16, 2023 UTC | Compressed Size: 513.27 MB

## Getting Started
Access the TAO Container (https://ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit), then use the NGC CLI to download models. Detailed deployment instructions available in the TAO Toolkit User Guide (https://docs.nvidia.com/tao/tao-toolkit/index.html).
