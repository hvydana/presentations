# PeopleNet - AMR Model Card
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplenet_amr

## Model Name
**PeopleNet - AMR** (Autonomous Mobile Robot)

## Description/Overview
"The Peoplenet Autonomous Mobile Robot (AMR) model detects persons, bags, and faces in an image. This model is ready for commercial use."

## Use Case
The primary intended application is detecting people in RGB color images from photos and videos. Secondary capabilities include detecting bags and faces, particularly useful for robotic systems operating at low heights.

## Model Architecture
- **Architecture Type:** Convolutional Neural Network (CNN)
- **Network:** DetectNet_v2 + ResNet34 (Feature Extractor)
- The system employs "bounding-box regression on a uniform grid on the input image" with GridBox object detection methodology

## Input Format
- **Type:** Images in Red, Green, Blue (RGB) format
- **Resolution:** 960 x 544 x 3 (W x H x C)
- **Channel Ordering:** NCHW (Batch Size, 3 channels, Height 544, Width 960)
- **Input Scale:** 1/255.0
- **Preprocessing:** No mean subtraction; no minimum bit depth, alpha, or gamma requirements

## Output Format
- **Type:** Labels, Bounding-Boxes, Confidence Scores
- **Labels:** Text strings (Bag, Face, Person)
- **Bounding Box:** (x-coordinate, y-coordinate, width, height)
- **Confidence Scores:** Floating point values

## Training Data
Internal proprietary dataset exceeding 3 million images containing over 8 million people:
- **Natural scenes:** 1,920,657 images
- **Robotics subset:** 43,076 images
- **Rotated perspectives:** 1,020,163 images
- **Total:** 3,028,550 images with 8,553,961 person instances, 2,143,825 bags, 4,020,310 faces

Data collected using Hawkeye cameras at various heights and angles, with approximately two-thirds from horizontal viewpoints (2-5 feet height) and supplementary low-density robotic perspective imagery.

**Labeling Method:** Human annotation following specific occlusion and truncation guidelines with minimum visibility thresholds (60% for non-person objects, 20% for occluded persons).

## Intended Users
Developers using NVIDIA hardware (GPUs or Jetson devices) with either TAO Toolkit or TensorRT software frameworks for deployment.

## License
Not explicitly stated in provided content.

## Version & Date
- **Current Version:** deployable_v1.0
- **Updated:** August 19, 2024 UTC
- **Compressed Size:** 78.77 MB
- **Available Versions:** deployable_v1.0 and trainable_v1.0

## Getting Started
Two model variants available:
1. **Trainable (unpruned):** For transfer learning with TAO Toolkit using custom datasets
2. **Deployable (quantized):** For inference with TensorRT

Use "TAO Container" and configure model_config with ResNet34 pretrained weights for fine-tuning.

## Tags
Computer Vision, CV, Deep Learning, Industrial Inspection, TAO, TAO Toolkit
