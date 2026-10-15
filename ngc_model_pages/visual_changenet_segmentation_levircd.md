# Visual ChangeNet-Segmentation (Research-only) - LEVIR-CD
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/visual_changenet_segmentation_levircd

## Description/Overview
This model detects building change maps from paired co-registered remote sensing images. It accepts "a pair of co-registered pre-change golden image and a post-change test image" and outputs "a binary segmentation change map denoting the change between the two images."

## Use Case
The primary application involves "Visual ChangeNet-Segmentation using RGB component level images" for comparing imagery. It's "intended for training and fine-tune using TAO Toolkit and user datasets for image comparison."

## Model Architecture
The system employs "a state of the art transformer-based Change Detection model" structured as "a Siamese Network, which is a class of neural network architectures containing two or more identical subnetworks." It uses "the FAN backbone network" and was "trained on NVImageNet dataset, and then fine-tunes on the LEVIR-CD dataset."

## Input/Output Format

**Input:** Two RGB images at 256 x 256 x 3 resolution with "Channel Ordering of the Input: NCHW"

**Output:** "Segmentation change map with the same spatial resolution as the input images: 256 X 256 X 2"

## Training Data
The model was trained on the LEVIR-CD dataset containing "10,192 pair-wise co-registered images" of "resolution 1024 x 1024" with "non-overlapping patches of size 256 x 256."

## Intended Users
These models require "NVIDIA hardware and software" and "can only be used with Train Adapt Optimize (TAO) Toolkit, or TensorRT."

## License
"CC-BY-NC-SA-4.0" with full terms at: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ml

## Tags
Computer Vision, CV, Deep Learning, Industrial Inspection, Optical Inspection, TAO, TAO Toolkit

## Version/Date
**Latest Version:** visual_changenet_levircd_trainable_v1.0
**Updated:** November 12, 2024 UTC
**Compressed Size:** 134.17 MB

## Download Instructions
Use the NGC CLI to download the model from the NGC Catalog at the provided NGC resource link.
