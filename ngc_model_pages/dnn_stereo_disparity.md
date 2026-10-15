# ESS DNN Stereo Disparity Model Card
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/models/dnn_stereo_disparity

## Model Name
**ESS DNN Stereo Disparity** (Efficient Supervised Stereo)

## Description/Overview
"ESS is a DNN that estimates disparity for a stereo image pair and returns a continuous disparity map for the given left image." The model also produces a confidence map indicating prediction certainty for each pixel.

## Use Cases
The model targets robotics applications including:
- Autonomous mobile robot navigation
- Robot manipulator depth perception
- Humanoid robot operations
- General robot perception to planning to action pipelines

## Model Architecture
The architecture comprises:
- Feature extractor with atrous spatial pyramid pooling (ASPP) for enhanced receptive field
- UNet stereo matching module
- Cost volume for computing left-right feature correlations
- Stereo mixture density module for disparity and confidence outputs
- Parallel confidence network branch

## Input Format
- **ESS**: RGB stereo image pairs, 576×960×3 (height×width×channels)
- **Light ESS**: RGB stereo image pairs, 288×480×3 (height×width×channels)
- Normalized by mean 0.5 and standard deviation 0.5

## Output Format
- **Disparity map**: FP32 values ranging 0 to infinity, shape 576×960 (ESS) or 288×480 (Light ESS)
- **Confidence map**: FP32 values ranging 0 to 1, same spatial dimensions as disparity

## Training Data
"Trained with 1,000,000 synthetically generated stereo images in rendered scenes from Omniverse using Replicator-Composer." Version 4.1.0 additionally includes:
- 100k real-world robot images from warehouses, urban areas, and indoor environments
- 1.1 million total stereo samples with randomized features
- 600k+ autonomous mobile robot scenario samples
- 250k+ robotic arm manipulation scene samples

## Intended Users
Developers building robotics applications on NVIDIA hardware requiring real-time stereo depth perception capabilities.

## License
"License to use this model is covered by the Model EULA. By downloading...you accept the terms and conditions of these [licenses](https://developer.download.nvidia.com/licenses/tao_toolkit_21-08_models_eula.pdf)."

## Tags
- Robotics
- Stereo disparity
- Computer vision
- Depth estimation

## Version & Date
- **Latest Version**: 4.1.0_onnx_trt10.16 (Signed)
- **Updated**: June 24, 2026 UTC
- **Compressed Size**: 122.59 MB

## Getting Started Instructions
Convert the encrypted model using TAO Toolkit with key **"ess"**:

```
LD_PRELOAD=plugins/x86_64/ess_plugins.so tao-converter -k ess -t fp16 -e ./ess.engine -o output_left,output_conf ess.etlt
```

Use NGC CLI to download the model from the catalog.
