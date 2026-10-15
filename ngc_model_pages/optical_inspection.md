# NVIDIA Optical Inspection Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/optical_inspection

## Model Name
Optical Inspection

## Description/Overview
"A Siamese Network is a class of neural network architectures that contain two or more identical subnetworks." The model applies this architecture to detect defects in soldered components on printed circuit boards by comparing golden reference images with sample component images.

## Use Case
The primary application is optical inspection using RGB component-level images. The model generates similarity scores between paired images to determine if a component is defective or acceptable.

## Model Architecture
Siamese Network with custom backbone. The model computes Euclidean distance between feature vectors extracted from paired inputs to assess similarity.

## Input/Output Format

**Input:**
- Two RGB images: 512 × 128 × 3 (Width × Height × Channels)
- Channel ordering: NCHW (Batch Size, Channels, Height, Width)

**Output:**
- Embedding vectors: 1 × 5 (Batch Size × Dimensions) for each input image
- Channel ordering: NC (Batch Size, Number of Dimensions)

## Training Data
Proprietary NVIDIA internal dataset containing:
- 168,828 total images
- 42,207 individual components
- 105 PCB boards across 4 different designs
- Components: Resistors, Capacitors, Inductors, etc.
- Defect rate: 0.15% (65 defects out of 42,207 components)
- Four LED illumination types per component: Solder, Uniform, LowAngle, White

## Training Algorithm
Contrastive loss optimization using the `optical_inspection` entrypoint in TAO (Train Adapt Optimize Toolkit).

## Performance Metrics

**Validation Results (21,148 test components):**
- At score cutoff 0.3: 0.97% False Positive Rate, 100% Defect Capture
- At score cutoff 0.5: 0.11% False Positive Rate, 97% Defect Capture

## Intended Users
Developers using NVIDIA hardware and software platforms, particularly those implementing manufacturing quality control and PCB inspection systems.

## Supported Hardware
- Jetson devices: Xavier NX, AGX Xavier, Orin NX, AGX Orin
- NVIDIA GPUs: T4, A100, A30, A10, A2

## License
"License to use this model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)"

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, TLT, Transfer Learning, Transfer Learning Toolkit

## Version & Date
**Latest Version:** deployable_v1.0
**Updated:** October 16, 2023 UTC
**Compressed Size:** 1 GB

## Getting Started Instructions
1. Access via NVIDIA NGC Catalog
2. Use NGC CLI to download the model
3. Deploy with TensorRT for inference or TAO Toolkit for training/fine-tuning
4. Refer to TAO User Guide for experiment configuration
5. Jupyter notebooks available in TAO container for retraining on custom datasets
