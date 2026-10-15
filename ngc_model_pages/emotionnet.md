# EmotionNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/emotionnet

## Model Name
**EmotionNet**

## Description/Overview
A classification network designed to categorize human emotions into six categories: Neutral, Happy, Surprise, Squint, Disgust, and Scream.

## Use Case
The primary application is detecting human emotion from photos and videos. It processes facial landmarks to classify emotional states and can be deployed in video analytics applications.

## Model Architecture
"This is a classification model with five fully connected layers."

## Input/Output Format

**Input:** "68 points (X, Y) of Human facial landmarks (1 x 136 x 1)"

**Output:** "Category labels (emotion) of each subject in the input image."

## Training Data
Trained on the MultiPie dataset containing over 750,000 images. The dataset includes "337 subjects, imaged under 15 view points and 19 illumination conditions in up to four recording sessions." Ground-truth emotion labels were obtained from subjects performing posed emotions during data collection.

## Intended Users
Developers using NVIDIA hardware and software frameworks, particularly those utilizing TAO Toolkit, DeepStream 6.0, or TensorRT for deployment on NVIDIA GPUs and Jetson devices.

## License
"License to use this model is covered by the Model EULA. By downloading the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)."

## Tags
Computer Vision, CV, DeepStream, Emotion Recognition, Healthcare, Metropolis, NVIDIA AI, Retail, TAO Toolkit

## Version/Date
**trainable_v1.0** | Updated November 27, 2024 UTC | Compressed Size: 4.38 MB

## Getting Started
"Get [TAO Container](https://ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit)" and refer to TAO documentation for training and deployment instructions.
