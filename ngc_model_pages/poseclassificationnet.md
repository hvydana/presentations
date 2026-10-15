# Pose Classification Model (PoseClassificationNet)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/poseclassificationnet

## Description/Overview
"Pose classification network to classify poses of people from their skeletons." The model recognizes six distinct human actions: getting up, jumping, sitting, sitting down, standing, and walking. It is ready for commercial use.

## Use Case
The primary intended application is recognizing actions from sequences of skeletal data, with a maximum sequence length of 300 frames.

## Model Architecture
- **Type:** Graph Convolutional Network (GCN)
- **Specific Architecture:** Spatial-Temporal Graph Convolutional Network (ST-GCN)
- **Reference:** Based on "Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition" (Yan, Xiong, Lin, AAAI 2018)

## Input Format
- **Type:** Video (MP4)
- **Dimensions:** 5D NumPy array `(N, C, T, V, M)`
  - N: number of sequences
  - C: input channels (3)
  - T: maximum sequence length (300 frames / 10 seconds at 30 FPS)
  - V: joint points (34 for NVIDIA format)
  - M: number of persons (supports single or multiple)

## Output Format
- **Type:** Label(s)
- **Format:** Text string category labels
- **Classes:** sitting_down, getting_up, sitting, standing, walking, jumping

## Training Data
Proprietary internal datasets with 6 annotated action classes using 34-keypoint NVIDIA skeleton format from deepstream-bodypose-3d. Dataset includes:
- sitting_down: 1,923 training / 53 validation / 94 test sequences
- getting_up: 1,884 training / 56 validation / 109 test sequences
- sitting: 909 training / 55 validation / 101 test sequences
- standing: 1,391 training / 54 validation / 99 test sequences
- walking: 1,894 training / 45 validation / 99 test sequences
- jumping: 1,440 training / 55 validation / 90 test sequences

## Performance Metrics
Total accuracy: 90.88% | Average class accuracy: 90.74%

Class-specific accuracies range from 80.81% (standing) to 99.08% (getting_up)

## Intended Users
Developers using NVIDIA hardware and software ecosystems, specifically those working with TAO Toolkit, DeepStream SDK, or TensorRT for video analytics applications.

## Supported Deployment Platforms
- **Frameworks:** TAO 5.2, DeepStream 6.1+
- **Hardware:** Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta architectures
- **OS:** Linux, Linux 4 Tegra
- **Inference Engine:** TensorRT

## License
No explicit license name or clause is provided in the fetched content. The model is available through NVIDIA NGC Catalog and is "ready for commercial use" under NVIDIA's terms of service.

## Version Information
- **Latest Version:** deployable_onnx_v1.0 (Signed)
- **Updated:** November 27, 2024 UTC
- **Compressed Size:** 12.14 MB
- **Available Versions:**
  - trainable_v1.0
  - deployable_v1.0
  - deployable_onnx_v1.0

## Getting Started Instructions

### Model Load Key
Encrypted model decryption key: `nvidia_tao`

### Using with TAO Toolkit
Add to experiment spec file:
```
model:
  model_type: ST-GCN
  pretrained_model_path: "/path/to/st-gcn_3dbp_nvidia.tlt"
  input_channels: 3
  dropout: 0.5
  graph_layout: "nvidia"
  graph_strategy: "spatial"
  edge_importance_weighting: True
```

### Deployment Options
- Train with TAO Toolkit using provided Jupyter notebooks
- Deploy via DeepStream SDK for video analytics pipelines
- Deploy with Triton Inference Server using TAO Triton apps

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning
