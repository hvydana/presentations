# Facial Landmark Estimator (FPENet)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/fpenet

## Model Name
**Facial Landmark Estimator (FPENet) Model** - also referenced as "Facial Landmarks Estimation"

## Description/Overview
The FPENet is a facial keypoints estimator network designed to "predict the (x,y) location of keypoints for a given input face image." It serves applications including face alignment, head pose estimation, emotion detection, eye blink detection, and gaze estimation. The model predicts 68, 80, or 104 keypoints and can handle visibility/occlusion flags for each point.

## Use Case
General-purpose facial landmark detection used in conjunction with face detectors for downstream computer vision tasks including facial alignment, head pose analysis, emotion recognition, and gaze tracking.

## Model Architecture
The architecture employs a "classification model with a Recombinator network backbone." This CNN family is suited for "fine grained pixel level predictions" where "convolutional layers in the finer branches get inputs from both coarse and fine layers."

## Input/Output Format
**Input:** "Images of 80 X 80 X 1"

**Output:** "N X 2 keypoint locations. N X 1 keypoint confidence." (N = number of keypoints)

## Training Data
Pre-trained models were developed using "a combination of NVIDIA internal dataset and Multi-PIE dataset." Specifics include approximately 500k NVIDIA internal images and 750k Multi-PIE images. Ground truth was established through "labeling ground-truth facial keypoints by human labellers."

## Intended Users
Developers using NVIDIA hardware and compatible software frameworks (TAO Toolkit, DeepStream 6.0, or TensorRT).

## License
Model EULA governs usage. Users must accept terms at: https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/

## Tags
Computer Vision, CV, DeepStream, Facial landmark estimation, Metropolis, NVIDIA AI, Retail, Robotics, TAO Toolkit

## Version & Date
**Latest Version:** deployable_v3.0 | **Updated:** November 27, 2024 UTC | **Compressed Size:** 2.24 MB

## Getting Started
Access via NGC CLI or download from NVIDIA NGC Catalog. Use with TAO Toolkit for retraining or DeepStream/TensorRT for deployment. Model load key: `nvidia_tlt`
