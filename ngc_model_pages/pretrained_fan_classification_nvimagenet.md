# Pre-trained FAN based NVImageNet Classification Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_fan_classification_nvimagenet

## Description/Overview
"Image Classification is a popular computer vision technique in which an image is classified into one of the designated classes based on the image features." These pretrained weights facilitate transfer learning using TAO Toolkit.

## Use Case
Primary use involves classifying objects in RGB images from photos and videos. Models support downstream tasks including object detection and segmentation. Suitable for smart cities, retail, healthcare, and industrial inspection applications.

## Model Architecture
FAN (Fully Attentional Network) represents "a transformer-based family of backbone from NVIDIA research that achieves SOTA in robustness against various corruptions." The key design element is "the attentional channel processing module that leads to robust representation learning."

## Input/Output Format
**Input:** B X 3 X 224 X 224 or B X 3 X 384 X 384 (B C H W format)

**Output:** "Category labels (1000 classes) for the input image"

## Training Data
Models were trained on the NVImageNet dataset with 1000 object categories.

## Intended Users
Developers using NVIDIA hardware and software platforms. Requires Train Adapt Optimize (TAO) Toolkit, DeepStream SDK, or TensorRT for deployment.

## License
"The licenses to use this model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these licenses" (https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest Version: fan_large_hybrid_nvimagenet | Updated October 16, 2023 UTC | Compressed Size: 293.76 MB

## Model Versions Available
- FAN-Base-Hybrid_nvimagenet
- fan_large_hybrid_nvimagenet
- FAN-Small-Hybrid_nvimagenet

## Getting Started
Download via NGC CLI or access TAO Container (https://ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit). Consult TAO Toolkit documentation (https://docs.nvidia.com/tao/tao-toolkit/index.html) for implementation details.
