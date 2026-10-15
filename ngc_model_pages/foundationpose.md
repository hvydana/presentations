# FoundationPose
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/models/foundationpose

## Model Name
**FoundationPose**

## Description/Overview
"FoundationPose is a unified foundation model for 6D object pose estimation and tracking of objects." The model estimates the 6D pose of specific objects using input containing the object's image, depth map, and 3D model. When a 3D model is unavailable, it can use a few images with corresponding depth maps instead. The model is fully trained and requires no additional training for commercial applications.

## Use Cases
- Robotic arm manipulation tasks
- Autonomous robot navigation
- Target tracking in delivery robots
- Robot manipulation of grocery products
- Mobile robot charging dock pose estimation

## Model Architecture
The architecture comprises three aggregated modules: a pose refinement network, a pose selection network, and an optional object modeling neural field. The object modeling neural field uses a signed distance function (SDF) to approximate a neural object field for model-free objects without CAD models. "The SDF is an implicit MLP network that maps any 3D point location to a signed distance value."

## Input/Output Format
**Inputs:**
- RGB image
- Depth map
- 3D object model (or few reference images with depth)
- Coarse global poses (sampled during processing)

**Outputs:**
- Estimated pose vector containing orientation and position
- Object tracking information

## Training Data
The model was trained on 678,000 synthetically generated images with ground truth annotations (augmented to 5.4 million total during training). "The dataset was synthetically generated with Isaac Sim, using 41K object models from Objaverse and 1K object models from GSO." Images include textures from real photographs rendered into synthetic scenes.

## Intended Users
Organizations requiring 6D pose estimation and tracking capabilities, particularly in robotics, autonomous systems, and computer vision applications. The model targets users with access to NVIDIA hardware and Ubuntu 22.04 with CUDA 11.6 or Jetpack 6.0 DP and later.

## License
**License Name:** Model EULA

**License Link/Clause:** "License to use this model is covered by the Model EULA. By downloading the public and release version of the model, you accept the terms and conditions of these [licenses](https://developer.download.nvidia.com/licenses/tao_toolkit_21-08_models_eula.pdf)."

## Tags
- AI
- Computer Vision
- CUDA
- Isaac
- Robotics
- Video Analytics
- Vision AI

## Version and Date
**Latest Version:** 1.0.1_onnx
**Last Updated:** October 13, 2025 UTC

## Download and Getting Started Instructions

**Download:**
Use the NGC CLI to download the model from the NVIDIA NGC catalog.

**Format Options:**
- Version 1.0.0 contains encrypted ETLT files
- Version 1.0.0_onnx contains unencrypted ONNX format

**Converting to TensorRT Engine Plan (ONNX):**
```
trtexec --onnx=./refine_model.onnx --saveEngine=./refine_trt_engine.plan --minShapes=input1:1x160x160x6,input2:1x160x160x6 --optShapes=input1:1x160x160x6,input2:1x160x160x6 --maxShapes=input1:252x160x160x6,input2:252x160x160x6

trtexec --onnx=./score_model.onnx --saveEngine=./score_trt_engine.plan --minShapes=input1:1x160x160x6,input2:1x160x160x6 --optShapes=input1:1x160x160x6,input2:1x160x160x6 --maxShapes=input1:252x160x160x6,input2:252x160x160x6
```

**Converting to TensorRT Engine Plan (ETLT):**
"In order to use the model in this encrypted format, convert the two etlt files to TensorRT engine plans using TAO. The model is encrypted and will only operate with the key foundationpose."
```
tao-converter -k foundationpose -t fp16 -e ./refine_trt_engine.plan -p input1,1x160x160x6,1x160x160x6,252x160x160x6 -p input2,1x160x160x6,1x160x160x6,252x160x160x6 -o output1,output2 refine_model.etlt

tao-converter -k foundationpose -t fp16 -e ./score_trt_engine.plan -p input1,1x160x160x6,1x160x160x6,252x160x160x6 -p input2,1x160x160x6,1x160x160x6,252x160x160x6 -o output1 score_model.etlt
```

**Integration:**
"FoundationPose is accessible in Isaac-ROS under isaac_ros_foundationpose. It seamlessly integrates both the refinement and score model inference, along with all required preprocessing and postprocessing to deliver the accurate pose estimation." Refer to the [quickstart documentation](https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_pose_estimation/isaac_ros_foundationpose/index.html#quickstart) in isaac_ros_docs.
