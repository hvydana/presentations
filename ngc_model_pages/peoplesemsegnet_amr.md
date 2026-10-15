# PeopleSemSegNet AMR
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplesemsegnet_amr

## Model Name
**PeopleSemSegNet AMR**

## Description/Overview
"The PeopleSemSegNet Autonomous Mobile Robot (AMR) model detects one or more 'person' object within an image and returns a semantic segmentation mask for all people within an image. This model is ready for commercial use."

## Use Case
The primary intended application is segmenting people in color (RGB) images. It can process photos and videos through appropriate decoding and preprocessing. The model performs semantic segmentation rather than instance-based segmentation.

## Model Architecture
**Type:** Convolutional Neural Network (CNN)
**Network Architecture:** UNet

"UNet is a fully convolutional network with an encoder that is comprised of convolutional layers and a decoder that is comprised of transposed convolutions or upsampling layers."

## Input Format
- **Type:** Images (RGB)
- **Resolution:** 960 x 544 x 3 (Width x Height x Channels)
- **Channel Ordering:** NCHW
- **Input Scale:** 1/255.0
- **Properties:** No mean subtraction, no minimum bit depth requirements

## Output Format
- **Types:** Label(s), Segmentation Mask, Confidence Scores
- **Format:** Text strings for labels; floating point for masks and scores
- **Categories:** Bag, Face, Person

## Training Data
Internal proprietary dataset containing over 5 million person objects across 920,026 images with 8,785,876 total person annotations. Data collection method was automatic/sensors with human labeling.

**Dataset composition:**
- 5ft Indoor: 108,692 images
- 5ft Outdoor: 206,912 images
- 10ft Indoor (Office): 413,270 images
- 10ft Outdoor: 18,321 images
- 20ft Indoor: 104,972 images
- 20ft Outdoor: 24,783 images
- Robotics Subset: 43,076 images

"Approximately half of the training data consisted of images captured in an indoor office environment."

## Intended Users
Developers and organizations using NVIDIA hardware and software who need person segmentation capabilities for robotics, autonomous vehicles, smart cities, or industrial applications.

## License
No specific license name or clause is displayed on this model card. The page indicates terms of use exist but no license agreement text is reproduced.

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, TLT, Transfer Learning, Transfer Learning Toolkit

## Version and Date
**Latest Version:** deployable_v1.1
**Updated:** August 19, 2024 UTC
**Compressed Size:** 3.71 MB

## Getting Started Instructions
Models require NVIDIA hardware and software. Usage requires:
- TAO 5.1 runtime engine
- Compatible with Ampere, Jetson, Hopper, Lovelace, Pascal, Turing architectures
- Linux or Linux 4 Tegra operating systems
- Model load key: `tlt_encode`

"These models can only be used with Train Adapt Optimize (TAO) Toolkit, DeepStream SDK or TensorRT."

Access the TAO Container and refer to TAO documentation for detailed implementation and transfer learning instructions.

## Performance Metrics
**Mean Intersection-Over-Union (MIOU):** 87 on robot's point of view evaluation dataset (5,000 proprietary images)

**Real-time Inference Performance (INT8, unpruned models):**
- Xavier NX: 199 FPS (BS 16)
- AGX Xavier: 356 FPS (BS 16)
- T4 GPU: 1,027.85 FPS (BS 64)
- A100 GPU: 5,745.79 FPS (BS 64)
