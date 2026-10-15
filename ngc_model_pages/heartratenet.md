# HeartRateNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/heartratenet

## Model Name
**HeartRateNet**

## Description/Overview
"Estimate heart-rate non-invasively from RGB facial videos." This is a non-invasive heart rate estimation network designed to predict heart rates from RGB face video recordings.

## Use Case
Primary use case intended for estimating heart rates from RGB face videos. The model can be deployed for healthcare and video analytics applications.

## Model Architecture
This is a two-branch architecture incorporating an attention mechanism that processes:
- **Motion map**: Difference between consecutive frames (current and previous) within a face region of interest
- **Appearance map**: Current frame within the same ROI, serving as the attention mechanism to focus on important features

The model is based on the DeepPhys architecture as referenced in the paper "Video-Based Physiological Measurement Using Convolutional Attention Networks."

## Input/Output Format

**Input**: "Image of face crop with dimension 3x72x72, input crop size and data format (channels first or last) is configurable"

**Output**: Estimated heart rate in beats per minute

## Training Data
HeartRateNet was trained on a proprietary dataset containing over 30,000 raw images with:
- Various skin tones, heart rates, and exercise conditions
- Data primarily from low-cost webcams (laptops or USB)
- Average 3-foot distance from camera
- Ground truth collected using CMS50d pulse oximeters

The model optimizes to minimize mean squared error between ground truth and predicted photoplethysmogram signals.

## Intended Users
Developers and organizations using NVIDIA hardware and software ecosystems, specifically those working with TAO Toolkit, DeepStream, or TensorRT for video analytics applications.

## License
"License to use these models is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these licenses (https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)."

## Tags
Computer Vision, CV, DeepStream, Healthcare, Heart Rate estimation, Metropolis, NVIDIA AI, TAO Toolkit, NVIDIA AI Enterprise Supported

## Version/Date
- **Latest Version**: deployable_v2.0
- **Updated**: November 27, 2024 UTC
- **Available Versions**: trainable_v2.0, deployable_v2.0, trainable_v1.0, deployable_v1.0

## Getting Started/Download Instructions
Download using NGC CLI. Model requires load key: `nvidia_tlt`. Access through NVIDIA NGC catalog at https://ngc.nvidia.com/catalog/models/nvidia:tao:heartratenet. Requires NVIDIA GPU hardware and TAO Toolkit, DeepStream 6.0, or TensorRT for deployment.
