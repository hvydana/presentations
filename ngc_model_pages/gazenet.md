# GazeNet (Gaze Estimation)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/gazenet

## Model Name
**GazeNet** (Gaze Estimation)

## Description/Overview
"The model described in this card detects a person's eye gaze point of regard (X, Y, Z) and gaze vector (theta and phi)."

## Primary Use Case
Detecting eye point of regard and gaze vector in video or image data for applications requiring eye tracking capability.

## Model Architecture
GazeNet employs a multi-input, multi-branch design. Three branches (face, left eye, right eye) use AlexNet-based feature extractors, while a fourth facegrid branch relies on fully connected layers. The architecture processes face crop, left eye crop, right eye crop, and facegrid inputs simultaneously.

## Input Format
- Face Image (grayscale): 224 x 224 x 1
- Left Eye Image (grayscale): 224 x 224 x 1
- Right Eye Image (grayscale): 224 x 224 x 1
- Facegrid Input (binary mask): 25 x 25 x 1

## Output Format
3D point of regards (X, Y, Z) and gaze vector (theta and phi angles in degrees)

## Training Data
"GazeNet `trainable` model was trained on a proprietary dataset with more than 220K Images." The dataset includes varied camera heights, angles, and illumination conditions.

## Intended Users
Developers using NVIDIA hardware with TAO Toolkit, DeepStream 6.0, or TensorRT frameworks.

## License
Model EULA covering the pre-trained model; full license terms available at https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/.

## Tags
Computer Vision, CV, DeepStream, Eye gaze estimation, Metropolis, NVIDIA AI, Retail, Robotics, TAO Toolkit

## Version & Date
**trainable_v1.0** | Updated March 17, 2025 UTC | Compressed Size: 17.44 MB

## Getting Started
Access the TAO Container (https://ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit), utilize the model load key `nvidia_tlt`, and deploy via DeepStream or TensorRT following official documentation.
