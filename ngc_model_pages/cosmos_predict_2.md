# Cosmos-Predict2.5-2B
Source: https://huggingface.co/nvidia/Cosmos-Predict2.5-2B (NGC catalog page not found — see note below)

## Note on source
NGC catalog URLs tried and 404'd:
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-predict2
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-predict2.5
- https://catalog.ngc.nvidia.com/orgs/nvidia/models/cosmos-predict2.5

Falling back to the Hugging Face model card per task instructions.

## Model Name
**Cosmos-Predict2.5-2B**

## Description/Overview
A diffusion-based world foundation model designed for generating physics-aware images and videos. The model is described as: "A family of highly performant pre-trained world foundation models purpose-built for generating physics-aware images, videos and world states for physical AI development." It functions as a diffusion transformer model that conditions on text inputs throughout the denoising process.

## Use Case
Physical AI applications, encompassing robotics, autonomous vehicles (AV), and related systems.

## Model Architecture
A diffusion transformer composed of interleaved self-attention, cross-attention, and feedforward layers. The architecture employs adaptive layer normalization to embed time information for denoising. Cross-attention layers enable conditioning on text throughout the denoising process. When image or video inputs are provided, their latent frames concatenate with generated frames along the temporal dimension. The model contains **2,059,174,912 parameters**.

## Input/Output Format

**Input:**
- Types: Text+Image or Text+Video
- Text: String (maximum 300 words)
- Image formats: jpg, png, jpeg, webp (1280x704 for 720P model)
- Video formats: mp4 (5 frames at 1280x704 for 720P model)

**Output:**
- Format: mp4 video
- Resolution: 1280x704 (720P variant)
- Frame rate: 16 FPS
- Duration: 5-second clips

## Training Data
- **Modalities**: Image, Text, Video
- **Collection Method**: Automated
- **Labeling Method**: Hybrid (Human and Automated)

Data sourced from large-scale publicly available datasets with automated filtering and human-in-the-loop validation to remove personal data.

## Intended Users
Physical AI developers

## License
**NVIDIA Open Model License** (Released September 23, 2025)

**Key License Clauses:**
- "Models are commercially usable."
- "You are free to create and distribute Derivative Models."
- "NVIDIA does not claim ownership to any outputs generated using the Models or Model Derivatives."

**Critical Restriction:** "If You bypass or disable any technical limitation, safety guardrail, encryption, DRM, or authentication mechanism contained in the Model without a substantially similar Guardrail, your rights will terminate."

Full license: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license

## Tags
Cosmos, Diffusers, Text2Video, Image2Video, Video2Video

## Version/Release Date
- GitHub: October 6, 2025
- Hugging Face: October 6, 2025
- ArXiv Paper: 2511.00062 (October 28, 2025)

## Getting Started Instructions

**Installation:**
```bash
pip install -U diffusers transformers accelerate
```

**Basic Usage:**
```python
import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "nvidia/Cosmos-Predict2.5-2B",
    dtype=torch.bfloat16,
    device_map="cuda"
)

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]
```

**Resources:**
- Code Repository: https://github.com/nvidia-cosmos/cosmos-predict2.5
- Full Documentation: See Cosmos-Predict2.5 repository
- White Paper: https://arxiv.org/abs/2511.00062
