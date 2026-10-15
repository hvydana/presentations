# Action Recognition Net
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/actionrecognitionnet

## Model Name
Action Recognition Net

## Description/Overview
"ActionRecognitionNet recognizes actions of people in a sequence of video frames: walk, bike riding, running, Falling on the floor, and push"

## Use Case
Primary purpose involves recognizing human actions from sequential RGB frames and optical flow grayscale images, with a sequence length of 32 frames.

## Model Architecture
- **Type:** Convolutional Neural Network (CNN)
- **Network:** ResNet18
- **Input Variants:** 2D and 3D models available for both RGB and optical flow inputs

## Input/Output Format

**Input:**
- RGB model 3D: 3 x 32 x 224 x 224 (C x D x H x W)
- RGB model 2D: 96 x 224 x 224 (C x D x H x W)
- Optical flow 3D: 2 x 32 x 224 x 224 (C x D x H x W)
- Optical flow 2D: 64 x 224 x 224 (C x D x H x W)

**Output:**
Category labels including walk, ride_bike, run, fall_floor, and push

## Training Data
"Trained on 1024 Videos of people walking, bike-riding, running, falling on the floor, and pushing." Dataset characteristics include varied visible body parts, camera motion types, viewpoints, number of people, and video quality levels.

## Intended Users
Developers utilizing NVIDIA Hardware (GPUs/Jetson devices) with TAO Toolkit, DeepStream SDK, or TensorRT for video analytics applications.

## License
Not explicitly stated on provided webpage.

## Tags
Computer Vision, CV, Deep Learning, TAO, TAO Toolkit

## Version/Date
Latest Version: trainable_rgb_3d | Updated: April 9, 2025 UTC | Compressed Size: 316.64 MB

## Getting Started
Models require decryption key "nvidia_tao" and are deployable via TAO Toolkit for retraining or DeepStream SDK for production deployment. Six pre-trained model variants available for different input types and hardware targets.
