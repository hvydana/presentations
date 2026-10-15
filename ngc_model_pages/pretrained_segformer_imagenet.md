# Pre-trained SegFormer ImageNet weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_imagenet

## Description/Overview
"Pre-trained SegFormer weights trained on ImageNet to facilitate transfer learning using TAO Toolkit."

The model serves as pre-trained starting weights for SegFormer semantic segmentation tasks, with weights trained via image classification on an internal ImageNet dataset.

## Use Case
These models enable transfer learning for semantic segmentation applications across various domains including smart cities, retail, healthcare, and industrial inspection. Primary use involves classifying objects in RGB images for photos and videos.

## Model Architecture
The architecture combines two key components:

**FAN (Fully Attentional Network):** "FAN is a transformer-based family of backbone from NVIDIA research that achieves SOTA in robustness against various corruptions." It features an attentional channel processing module for robust representation learning.

**SegFormer:** "SegFormer is a real-time state of the art transformer based semantic segmentation model" that "unifies Transformers with lightweight multilayer perception (MLP) decoders" to predict class labels for every pixel.

## Input/Output Format
**Input:**
- B X 3 X 224 X 224 (B C H W)
- B X 3 X 384 X 384 (B C H W)

**Output:** Category labels (1000 classes) for the input image

## Training Data
Models were trained on ImageNet1K and ImageNet22K datasets.

## Intended Users
Organizations requiring semantic segmentation capabilities who have access to NVIDIA hardware and software (TAO Toolkit, DeepStream SDK, or TensorRT).

## License
**Name:** NVIDIA Open Model License

**Clause/Link:** "License to use these models is covered by the NVIDIA Open Model License. By downloading the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)."

Additionally: "This work is licensed under the Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)."

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
**Latest Version:** fan_hybrid_tiny
**Updated:** April 26, 2024 UTC
**Compressed Size:** 28.64 MB

## Download/Getting Started Instructions
Use NGC CLI with the command provided on the page. Access the TAO Container from NGC catalog. Available model variants include fan_hybrid_tiny, fan_hybrid_small, fan_hybrid_base_in22k, fan_hybrid_large_in22k, and others with various resolutions (224x224 or 384x384).
