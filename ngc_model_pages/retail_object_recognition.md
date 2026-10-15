# Retail Object Recognition
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/retail_object_recognition

## Description/Overview
"This model encodes retail objects to embedding vectors and predicts their labels based on the embedding vectors in the reference space." Version 2.0 additionally provides classification output to categorize objects into seen classes. Both versions support few-shot learning through metric learning techniques.

## Use Case
Recognition and classification of retail objects on checkout counters for inventory management and smart retail applications.

## Model Architecture

**Version 1.0:**
- Backbone: ResNet101 with removed fully connected layers
- Embedder: Single-layer perceptron (input: 2048, output: 2048)
- Embedding dimension: 2048

**Version 2.0:**
- Backbone: FAN-Base-Hybrid (Fully Attentional Network)
- Three components: trunk, classification head, embedding head
- Embedding head: Four adaptors with output size 448
- Input resolution: 224x224

## Input/Output Format
- Input: RGB images (224x224 pixels)
- Output: Embedding vectors (2048-dimensional for v1.0; variable for v2.0) and/or classification predictions

## Training Data

**Version 1.0:**
- 600,000 synthetic images (100 retail subjects)
- 50,000 real images (100 subjects, cropped from 6 scenes)
- Training algorithm: Triplet Loss

**Version 2.0:**
- 80,872 synthetic images (315 categories)
- 48,140 training images + 58,699 test images from real data (315 subjects, 7 scenes)
- Training algorithms: Triplet Loss (embedder) and Cross-entropy (classifier)

## Intended Users
Computer vision developers, retail analytics teams, and organizations deploying intelligent video analytics using NVIDIA TAO Toolkit and DeepStream SDK.

## License
"License to use these models is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)."

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest: trainable_head_fan_base_v2.0 | Updated March 13, 2024 UTC | Compressed Size: 4.39 MB

## Getting Started
1. Download TAO Toolkit and install
2. Configure experiment spec file with pretrained model path
3. Use command: `tao model ml_recog train -e=<train config file>`
4. Refer to TAO Toolkit Jupyter notebooks for Retail Object Recognition examples in NGC Catalog
