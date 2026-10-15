# BodyPose3DNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/bodypose3dnet

## Model Name
BodyPose3DNet

## Description/Overview
"3D human pose estimation network to predict 34 keypoints in 3D of a person in an image." The model tracks both 2D and 3D poses with 34 body joints including pelvis, hips, knees, ankles, shoulders, elbows, wrists, and facial landmarks. Applications span action understanding, surveillance, motion capture, AR/VR, sports analysis, and workplace monitoring.

## Use Cases
Primary applications include human pose detection in RGB images for:
- Activity and gesture recognition
- Fall detection
- Posture analysis
- Motion capture and CGI
- Augmented and virtual reality
- Sport analysis and AI-powered coaching
- Workplace activity monitoring

## Model Architecture
**Type:** Deep Convolutional Neural Network

**Architecture:** HRNet (High-Resolution Network)

## Input Format
- **input0:** float32, shape -1 x 3 x 256 x 192 (RGB image)
- **k_inv:** float32, shape -1 x 3 x 3 (inverse camera intrinsics)
- **t_form_inv:** float32, shape -1 x 3 x 3 (inverse transformation)
- **scale_normalized_mean_limb_lengths:** float32, shape -1 x 36
- **mean_limb_lengths:** float32, shape -1 x 36

## Output Format
Four output tensors:
- **pose2d:** float32, shape -1 x 34 x 3 [x, y, confidence]
- **pose2d_org_img:** float32, shape -1 x 34 x 3 [x, y, confidence]
- **pose25d:** float32, shape -1 x 34 x 4 [x, y, depth, confidence]
- **pose3d:** float32, shape -1 x 34 x 3 [x, y, z]

## Training Data
Not specified in documentation.

## Intended Users
Developers using NVIDIA's Train Adapt Optimize (TAO) Toolkit for computer vision applications.

## License
Licensed under "NVIDIA Open Model License." Additionally, work is "licensed under the Creative Commons Attribution 4.0 International License."

**License Link:** https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
CV, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version & Date
**Version:** deployable_performance_onnx_v1.0 (Latest)

**Updated:** September 20, 2024 UTC

**Compressed Size:** 38.49 MB

## Getting Started
1. Install NGC CLI from ngc.nvidia.com
2. Configure: `ngc config set`
3. Download: `ngc registry model download-version nvidia/tao/bodypose3dnet:<template> --dest <path>`

## Limitations
- "It only supports one person in the scene"
- "Full body of the person needs to be visible"
