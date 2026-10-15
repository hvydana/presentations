# Isaac GR00T N1.7 (nvidia/GR00T-N1.7-3B)
Source: https://huggingface.co/nvidia/GR00T-N1.7-3B (NGC catalog page not found — see note below)

## Note on source
NGC catalog URLs tried and 404'd:
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/models/isaac-gr00t-n1.5
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/models/isaac-gr00t-n1-5

Falling back to the Hugging Face model card per task instructions, which resolved directly for the exact "N1.7" version requested.

## Model Name
**nvidia/GR00T-N1.7-3B**

## Description/Overview
"NVIDIA Isaac GR00T N1.7 is an open foundation model for generalized humanoid robot reasoning and skills." This cross-embodiment model accepts multimodal input including language and images to perform manipulation tasks in diverse environments. The N1.7 represents the medium-sized version utilizing pre-trained vision and language encoders along with a flow matching action transformer to model action sequences conditioned on vision, language, and proprioception.

## Use Case
According to the documentation, intended users include:
- "Researchers, Academics, Open-Source Community: AI-driven robotics research and algorithm development"
- "Developers: Integrate and customize AI for various robotic applications"
- "Startups & Companies: Accelerate robotics development and reduce training costs"

## Model Architecture
The architecture employs:
- Pre-trained vision transformer (SigLip2) processing RGB camera frames
- Pre-trained T5 transformer for text encoding
- Multi-layer perceptron (MLP) for robot proprioception indexed by embodiment ID
- Flow matching transformer implemented as a diffusion transformer (DiT) with adaptive layernorm conditioning
- **3 billion parameters**

The "GR00T-N1.7 VLM backbone is now Cosmos-Reason2-2B"

## Input Format
- **Vision:** Variable uint8 image frames from robot cameras (2D RGB)
- **State:** Floating-point proprioception vectors (1D)
- **Language:** Text instruction strings (1D)
- **Embodiment ID:** Integer indicating training embodiment (1D)

## Output Format
"Continuous-value vectors" representing different motor controls depending on the robot's degrees of freedom (2D output parameters).

## Training Data
Total training dataset comprises 21.6 million data points across 13 datasets. Data collection method: "Hybrid: Human, Robot, Simulated" with labeling by "Hybrid: Human, Automated." The model is cross-embodiment, utilizing RGB camera and robot proprioception/actuator data.

Four post-trained model variants use:
1. Bridge Dataset (60,096 trajectories across 24 environments)
2. Fractal Dataset (same Bridge data in SimplerEnv)
3. DROID Dataset (~76,000 trajectories across 564 scenes)
4. LIBERO Dataset (130 language-conditioned manipulation tasks)

## Intended Users
Researchers, academics, open-source community, developers, and commercial entities focused on robotics development and AI algorithm advancement.

## License
**Name:** NVIDIA Open Model License Agreement

**Link:** https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

The model "is ready for commercial/non-commercial use" with global deployment geography.

## Tags/Categories
- Robotics
- Safetensors
- Gr00tN1d7
- Vision-Language-Action (VLA) model

## Version/Date
**GR00T N1.7 EA** (Early Access)

**Release:** GitHub and HuggingFace (https://github.com/NVIDIA/Isaac-GR00T and https://huggingface.co/collections/nvidia/gr00t-n17)

**Associated Paper:** arxiv 2503.14734 (Published March 18, 2025)

## Getting Started/Download Instructions
Access via:
- GitHub: https://github.com/NVIDIA/Isaac-GR00T
- HuggingFace: Direct model repository or collection link
- Official website: https://developer.nvidia.com/isaac/gr00t

**Runtime:** PyTorch on NVIDIA GPU-accelerated systems (Ampere, Blackwell, Jetson, Hopper, Lovelace architectures). Linux operating system preferred.

## Note on related model
For reference, an earlier version, nvidia/GR00T-N1.5-3B, was also fetched during this research. Its license was the more restrictive "Nvidia OneWay Noncommercial License," whereas N1.7 is documented as "ready for commercial/non-commercial use" under the NVIDIA Open Model License Agreement — this discrepancy should be independently verified before relying on it, since the two fetches came from different HF pages.
