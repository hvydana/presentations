# TAO Pretrained Classification-TF2 (efficientnet_tf2_savedmodel_nohead_b0_amp_cosine)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_classification_tf2

Note: The exact slug `efficientnet_tf2_savedmodel_nohead_b0_amp_cosine` could not be resolved as its own standalone catalog page. It appears to correspond to a specific downloadable version/checkpoint within this parent model resource (TAO Pretrained Classification-TF2), whose latest listed version at fetch time was `efficientnet_b0` (EfficientNet-B0 backbone, TF2 "nohead"/no-classification-head SavedModel format, trained with AMP + cosine LR schedule — consistent with the slug's naming). Content below is from the parent model card.

## Model Name
TAO Pretrained Classification-TF2

## Description/Overview
"Pretrained backbones for TAO Toolkit TF2 image classification"

The model provides pre-trained weights for feature extractors based on the EfficientNet architecture, designed to serve as starting points for transfer learning within the TAO Toolkit ecosystem.

## Use Case
These models support image classification tasks and can be adapted for computer vision applications including smart cities, retail, healthcare, and industrial inspection.

## Model Architecture
"The models in this instance are feature extractors based on the EfficientNet architecture."

Specifically, EfficientNet-based backbones optimized for TensorFlow 2.

## Training Data
"These models are trained on a subset of the Google OpenImages dataset."

## Input/Output Format
Not explicitly specified in the provided content.

## Intended Users
Developers using NVIDIA's Train Adapt Optimize (TAO) Toolkit who need pre-trained backbones for custom model development and transfer learning.

## License
Creative Commons Attribution 4.0 International License

**License Clause:** "This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, please visit this link: http://creativecommons.org/licenses/by/4.0/"

## Tags
- EfficientNet
- Classification
- TensorFlow 2
- Pre-trained
- Transfer Learning

## Version Information
- **Latest Version:** efficientnet_b0
- **Updated:** December 8, 2022 UTC
- **Compressed Size:** 45.6 MB

## Supported Backbone Versions
- efficientnet-b0

## Getting Started Instructions

1. Install NGC CLI from ngc.nvidia.com
2. Configure NGC CLI: `ngc config set`
3. Download the model: `ngc registry model download-version nvidia/tao/pretrained_efficientde_tf2t:<template> --dest <path>`
4. Obtain NGC API key from the SETUP tab
5. Download sample notebooks: `ngc registry resource download-version "nvidia/tao/getting_started:4.0.0"`
6. Run Jupyter: `jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root`

## Limitations
"These are unpruned models with just the feature extractor weights and, may not be used without re-training in an EfficientDet object detection application."

## Publisher
NVIDIA

## URLs tried before finding the parent page
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/efficientnet_tf2_savedmodel_nohead_b0_amp_cosine (404)
- https://catalog.ngc.nvidia.com/orgs/nvidia/models/efficientnet_tf2_savedmodel_nohead_b0_amp_cosine (404)
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/resources/efficientnet_tf2_savedmodel_nohead_b0_amp_cosine (404)
- https://catalog.ngc.nvidia.com/orgs/nvidia/resources/efficientnet_tf2_savedmodel_nohead_b0_amp_cosine (404)
- https://catalog.ngc.nvidia.com/orgs/nvstaging/teams/tao/models/efficientnet_tf2_savedmodel_nohead_b0_amp_cosine (404)
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_classification_tf2 (SUCCESS — used above)
