# Pre-trained Segformer - CityScapes
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_cityscapes

## Description/Overview
"The model described in this card segments cityscapes urban city classes within an image and returns a semantic segmentation mask."

## Use Case
The model is designed for segmenting urban city classes in RGB images. Primary deployment is intended through DeepStream for analyzing photos and videos in urban transport settings.

## Model Architecture
"Segformer is a real-time state of the art transformer based semantic segmentation model." The framework unifies Transformers with lightweight multilayer perception decoders to predict class labels for every pixel. The model identifies 19 urban CityCapes classes including road, sidewalk, building, vegetation, sky, person, car, truck, bus, train, motorcycle, and bicycle.

## Input/Output Format

**Input:** Color images at 1024x1024x3 resolution (any resolution can be processed)

**Output:** Semantic segmentation mask of urban city classes for the input image

## Training Data
Trained on the CityCapes dataset, which provides urban scene understanding annotations for semantic segmentation tasks.

## Intended Users
Developers building AI-based video analytics applications requiring semantic segmentation of urban environments using NVIDIA hardware and software ecosystems.

## License
"This work is licensed under the Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)."

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest Version: deployable_fan_tiny_hybrid_v1.0 | Updated: October 16, 2023 | Compressed Size: 39.54 MB

## Getting Started
Download via NGC CLI or deploy using DeepStream 6.1 with provided configuration files (nvinfer_config.txt and labels.txt) following TAO User Guide deployment instructions.
