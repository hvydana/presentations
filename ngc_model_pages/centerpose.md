# CenterPose
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/centerpose

## Model Name
**CenterPose**

## Description/Overview
"CenterPose is a single-stage, keypoint-based method for category-level object pose estimation." It processes unknown object instances within a recognized category using a single RGB image. The pretrained model detects the projections of 3D keypoints, estimates a 6-DoF pose, and regresses the relative 3D bounding cuboid dimensions.

## Use Case
The primary application involves estimating an object's pose from a single RGB image. It identifies objects in photos and is designed for deployment to edge devices using TensorRT.

## Model Architecture
Two backbone network types are supported:
- **DLA34**: A standard Convolutional Neural Network (CNN) backbone
- **FAN-Small-Hybrid**: A transformer-based classification backbone

"The network architecture processes a re-scaled and padded RGB image. Using the DLA34/FAN-Small-Hybrid feature extractor combined with an upsampling module, the network outputs distinct heads that predict the projections of 3D bounding box keypoints and relative cuboid dimensions."

## Input Format
"RGB Image of dimensions: 512 X 512 X 3 (W x H x C). Channel Ordering of the Input: NCHW, where N = Batch Size, C = number of channels (3), H = Height of images (512), W = Width of the images (512)"

## Output Format
"The model outputs three distinct results that predict the projections of 3D bounding box keypoints, the cuboid relative dimensions, and the 6-DoF (Degrees of Freedom)."

## Training Data
Trained on the Objectron dataset, comprising:
- 15,000 annotated video clips
- Over 4 million annotated frames
- Eight object categories: bikes, books, bottles, cameras, cereal boxes, chairs, laptops, and shoes
- Training frames extracted at 15 fps temporally downsampled from original videos
- For symmetric objects, multiple ground truth labels generated through rotation

Training data distribution by category:

| Category | Training Videos | Training Images |
|----------|-----------------|-----------------|
| Bike | 375 | 8,396 |
| Book | 1,618 | 31,609 |
| Bottle | 1,542 | 26,090 |
| Camera | 652 | 12,758 |
| Cereal Box | 1,288 | 22,024 |
| Chair | 1,555 | 27,608 |
| Laptop | 1,179 | 26,462 |
| Shoe | 1,693 | 30,515 |

## Intended Users
Developers building AI applications for computer vision and object pose estimation on NVIDIA hardware and software platforms.

## License
"License to use these models is covered by the NVIDIA Open Model License. By downloading the model, you accept the terms and conditions of these licenses."

**License Link**: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, TLT, Transfer Learning, Transfer Learning Toolkit

## Version/Date
**Latest Version**: trainable_fan_small
**Updated**: November 12, 2024 UTC
**Compressed Size**: 327.96 MB

## Download/Getting Started Instructions
Use the NGC CLI to download. Models are designed for use with the Train Adapt Optimize (TAO) Toolkit or TensorRT.

For deployment with TAO-Deploy:
- Convert pretrained ONNX models into TRT engine using TensorRT
- Set up engine file path and configure intrinsic matrix in experiment spec file
- Run TAO-Deploy inference pipeline

For Triton Inference Server deployment, refer to TAO Triton apps for end-to-end inference.
