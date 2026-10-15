# Cosmos-Transfer2.5-2B
Source: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B (NGC catalog page not found — see note below)

## Note on source
NGC catalog URLs tried and 404'd:
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-transfer2
- https://catalog.ngc.nvidia.com/orgs/nvidia/models/cosmos-transfer2.5

Falling back to the Hugging Face model card per task instructions.

## Model Name
**Cosmos-Transfer2.5-2B**

## Description/Overview
A diffusion-based world foundation model that generates physics-aware images and videos from text and control video inputs. The model produces "720P video with 16FPS" and is "purpose-built for generating physics-aware images, videos and world states aligned with the input control conditions."

## Use Case
Physical AI applications encompassing robotics, autonomous vehicles, and related domains.

## Model Architecture
A diffusion transformer designed for video denoising in latent space. The system features "interleaved self-attention, cross-attention and feedforward layers" with adaptive layer normalization for time embedding. Control branches process input videos to extract modality-specific signals injected into the base model's transformer blocks. The model contains **2,358,047,744 parameters**.

## Input/Output Format

**Inputs:**
- Text: String (under 300 words describing scenes for 5-second generation)
- Control Videos: MP4 format at 1280x720 resolution, supporting Canny edge, blurred RGB, segmentation masks, and depth maps

**Outputs:**
- Video: MP4 format matching input temporal length and spatial resolution at 16 FPS

## Training Data
- **Modalities:** Image, Text, Video
- **Collection Method:** Automated
- **Labeling Method:** Hybrid (Human and Automated)

## Intended Users
Physical AI developers

## License
**NVIDIA Open Model License** (Version: September 23, 2025)

**Key clause:** "Models are commercially usable. - You are free to create and distribute Derivative Models. - NVIDIA does not claim ownership to any outputs generated using the Models or Model Derivatives."

Additional license: Apache License 2.0

**License link:** https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license

## Tags
- Cosmos
- Diffusers
- text2video
- image2video
- video2video
- nvidia

## Version/Date
- GitHub release: October 6, 2025
- Hugging Face release: October 6, 2025
- arXiv: 2511.00062

## Getting Started Instructions

**Installation (Diffusers):**
```
pip install -U diffusers transformers accelerate
```

**Basic usage:**
```python
import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "nvidia/Cosmos-Transfer2.5-2B",
    dtype=torch.bfloat16,
    device_map="cuda"
)
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]
```

**Additional resources:**
- Repository: https://github.com/nvidia-cosmos/cosmos-transfer2.5
- White Paper: https://arxiv.org/abs/2511.00062
- Google Colab and Kaggle notebooks available on model card
