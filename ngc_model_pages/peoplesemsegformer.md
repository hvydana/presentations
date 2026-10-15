# PeopleSemSegFormer Model Card
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplesemsegformer

## Description/Overview
"The model described in this card segments one or more 'person' object within an" image and produces semantic segmentation masks for people detected within images.

## Use Case
The primary intended use case involves segmenting people in color (RGB) images from photos and videos. The model supports convenience-store retail analytics and pose-estimation workflows.

## Model Architecture
SegFormer represents "a simple, efficient yet powerful semantic segmentation framework" that unifies transformers with lightweight multilayer perception decoders. It predicts class labels for each pixel, distinguishing between person and background classes.

## Input/Output Format

**Input:** Color images at 512x512x3 resolution

**Output:** "Category label (person or background) for every pixel in the input image"

## Training Data
The model trained on a proprietary dataset encompassing:
- 7.6+ million images
- 71+ million objects (person class)
- Mixed camera heights, crowd densities, and field-of-view angles
- ~50% indoor office environments (10-foot height, 45-degree angle, close FOV)
- ~500k low-density scenes with extended limbs
- ~200k low-contrast images

## Intended Users
Developers using NVIDIA hardware and software (GPUs, Jetson devices) who work with TAO Toolkit, DeepStream SDK, or TensorRT.

## License
"License to use this model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these licenses" (NVIDIA AI Enterprise EULA referenced).

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, TAO Toolkit, Transfer Learning

## Version/Date
**deployable_v1.0** - Updated November 27, 2024 UTC

## Getting Started
Download via NGC CLI. Deploy using TAO Toolkit, DeepStream SDK 6.1+, or TensorRT with provided configuration files.
