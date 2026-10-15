# GestureNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/gesturenet

## Model Name
GestureNet

## Description/Overview
"Classify gestures from hand crop images." The model is described as "a classification network, which aims to classify hand crop images into 5 gesture types: thumbs up, fist, stop, ok, two, random."

## Use Cases
GestureNet operates in cascade with hand detection or body pose networks. "BodyPoseNet detects human body joints which are used to create hand crops and GestureNet acts as a classifier determining the gesture of the hand." Applied across healthcare, retail, and robotics industries.

## Model Architecture
"This is a classification model with a Resnet-18 backbone."

## Training Algorithm
"The training algorithm optimizes the network to minimize the categorical cross entropy loss for the classes."

## Training Data
"GestureNet was trained on a proprietary dataset with more than 150K images. The training dataset contains hand crops from user facing camera at various heights with variations in user, backgrounds and illumination."

## Input/Output Format
**Input:** "RGB Images of 160 X 160 X 3"
**Output:** "Gesture category labels."

## Performance Metrics
Evaluation on 10,000 proprietary images shows 85% precision, recall, and F1-score. Real-time inference performance varies by device (FP16 precision): Jetson Nano (79 FPS), NX (111 FPS), Xavier (481 FPS), T4 GPU (1227 FPS).

## Intended Users
"This model needs to be used with NVIDIA Hardware and Software" and can only be deployed with TAO Toolkit, DeepStream 6.0, or TensorRT.

## Model Versions Available
- trainable_v1.0
- deployable_v1.0
- deployable_v2.0
- deployable_v2.0.1
- deployable_v2.0.2 (latest)

## License
"License to use this model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these licenses (https://developer.nvidia.com/deep-learning-models-license-agreement)."

## Download Instructions
Use NGC CLI to download. Model load key required: `nvidia_tlt`

## Version & Date
Latest: deployable_v2.0.2 | Updated November 27, 2024 UTC | Compressed Size: 43.99 MB

## Tags
Computer Vision, CV, DeepStream, Gesture recognition, Healthcare, Metropolis, NVIDIA AI, Retail, Robotics, TAO Toolkit

## Key Limitations
- Designed for frontal views only
- Requires mostly monochromatic backgrounds
- Trained on RGB images in good lighting; poor performance in dark/monochrome/infrared conditions
