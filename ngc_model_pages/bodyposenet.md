# BodyPoseNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/bodyposenet

## Model Name
BodyPoseNet

## Description/Overview
"BodyPoseNet predicts the skeleton for every person in a given input image. The model predicts 18 key points" including nose, neck, shoulders, elbows, wrists, hips, knees, ankles, eyes, and ears. The model is designed for multi-person human pose estimation using a single-shot bottom-up methodology.

## Use Case
Primary applications include activity/gesture recognition, fall detection, and posture analysis. The model is ready for commercial use.

## Model Architecture
- **Type:** Convolutional Neural Network (CNN)
- **Network Architecture:** Visual Geometry Group (VGG)
- Uses "confidence maps" and "part affinity fields" with post-processing via NMS and bipartite graph matching for final skeleton predictions.

## Input Format
- **Type:** RGB Image
- **Dimensions:** H × W × 3
- **Properties:** "No minimum bit depth, alpha, or gamma"
- Images preprocessed for normalization and aspect-ratio-preserving resizing

## Output Format
- **Type:** Tensors (N-Dimensional arrays)
- **Structure:** M × N × 3 where M = number of humans detected, N = number of keypoints
- Includes confidence maps (H1' × W1' × C) and part affinity fields (H2' × W2' × P)

## Training Data
Google OpenImages Version 3: approximately 400,000 images and 7,000 validation images across thousands of classes with human and crowdsourced verification.

## Evaluation Data
COCO validation sets containing "more than 200,000 images and 250,000 person instances labeled with keypoints."

## Performance Metrics (INT8, 288×384 input)
- AP 0.50:0.95 (all): 56.2
- AP 0.5 (all): 79.3
- Inference latency ranges from 200ms (Nano) to 1.80ms (T4 GPU)

## Intended Users
Developers using NVIDIA's Train Adapt Optimize (TAO) Toolkit for pose estimation applications.

## Supported Hardware
Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta architectures; Linux and Linux 4 Tegra operating systems.

## Model Versions
- **trainable_v1.0:** For finetuning on custom datasets
- **deployable_v1.0:** Inference pipeline with INT8 calibration (TensorRT 7)
- **deployable_v1.0.1:** Inference pipeline with INT8 calibration (TensorRT 8)
- **deployable_onnx_v1.0.1:** Latest signed version

## License
No specific license name or clause is displayed on this NGC catalog page.

## Tags
Body pose estimation, CV, DeepStream, Healthcare, Metropolis, NVIDIA AI, Retail, Robotics, TAO Toolkit

## Version/Date
Latest Version: deployable_onnx_v1.0.1 (Updated November 12, 2024 UTC)
Compressed Size: 64.09 MB

## Getting Started Instructions
1. Install NGC CLI from ngc.nvidia.com
2. Configure NGC CLI: `ngc config set`
3. View supported models: `ngc registry model list nvidia/tao/bodyposenet:*`
4. Download model: `ngc registry model download-version nvidia/tao/bodyposenet:<template> --dest <path>`

Requires TAO Toolkit 5.2 runtime engine.
