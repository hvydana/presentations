# Cosmos-Policy-ALOHA-Predict2-2B (representative of the "Cosmos Policy" family; "Cosmos-H-Dreams" not found)
Source: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B (NGC catalog page not found — see note below)

## Note on source and naming
NGC catalog was searched for "cosmos policy" / "cosmos-h-dreams" style models under the cosmos, isaac, and nvresearch team paths; no matching NGC catalog page was found. On Hugging Face, no model or dataset named "Cosmos-H-Dreams" exists. Instead, NVIDIA publishes a "Cosmos Policy" family of embodiment-specific bimanual/manipulation policy models (collection: https://huggingface.co/collections/nvidia/cosmos-policy), including:
- nvidia/Cosmos-Policy-ALOHA-Predict2-2B
- nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B
- nvidia/Cosmos-Policy-LIBERO-Predict2-2B
- nvidia/Cosmos-Policy-RoboCasa-Predict2-2B
- nvidia/Cosmos3-Nano-Policy-DROID (16B)

The ALOHA-Predict2-2B variant is reproduced below as the representative model card since it was successfully fetched.

## Model Name
**Cosmos-Policy-ALOHA-Predict2-2B**

## Description/Overview
A 2B-parameter bimanual robot manipulation policy model fine-tuned from NVIDIA's Cosmos-Predict2-2B-Video2World video foundation model. The model achieves "93.6% average completion rate across four challenging real-world bimanual manipulation tasks on the ALOHA 2 robot platform."

Key characteristics include single-stage fine-tuning without architectural modifications, multimodal outputs predicting actions and future states through unified video diffusion, and demonstrated real-world performance on complex tasks.

## Use Case
Physical AI applications: "Bimanual robotic manipulation and control in real-world environments, encompassing contact-rich manipulation and imitation learning from human demonstrations." Additional applications include vision-based robot learning with multiple camera viewpoints, long-horizon task planning, and high-precision manipulation tasks.

## Model Architecture
"A diffusion transformer with latent video diffusion, fine-tuned from Cosmos-Predict2-2B-Video2World." The architecture encodes actions, proprioceptive states, and values as latent frames injected into the video model's diffusion sequence. The model contains 2B parameters inherited from the base model.

## Input Format
**Text + Multi-view Images + Proprioceptive State**
- Text: Natural language task description (1D string)
- Images: RGB from three camera views at 224x224 pixels (top-down third-person, left wrist, right wrist)
- Proprioception: 14-dimensional state array (7 joint angles per arm)

## Output Format
**Action Sequence + Future State Predictions + Value Estimate**
- Actions: 50-timestep sequence of 14-dimensional actions
- Future states: Images from all three camera views (224x224 RGB) plus 14-dimensional proprioception at t+50
- Value: Scalar expected cumulative reward estimate

## Training Data
**Dataset:** ALOHA-Cosmos-Policy dataset containing "4 bimanual manipulation tasks" with "185 total real-world human teleoperation demonstrations":
- put X on plate: 80 demos
- fold shirt: 15 demos
- put candies in bowl: 45 demos
- put candy in ziploc bag: 45 demos

**Training Configuration:**
- Base model: Cosmos-Predict2-2B-Video2World
- 50,000 gradient steps on 8 H100 GPUs
- Full model fine-tuning with batch size 200
- Training time: approximately 48 hours
- Image resolution: 224x224 pixels

## Intended Users
Research and development practitioners working on physical AI, robotic manipulation, and robot learning systems. The model is explicitly stated as "for research and development only."

## License
**NVIDIA One-Way Noncommercial License (NSCLv1)**

The license confirms: "Models are not for commercial use" and "NVIDIA does not claim ownership to any outputs generated using the Models or Derivative Models."

Full license available at: https://github.com/NVlabs/HMAR/blob/main/LICENSE

For custom licensing, contact: cosmos-license@nvidia.com

## Tags/Classification
- cosmos-policy
- bimanual manipulation
- robot control
- diffusion transformer
- video foundation model
- imitation learning
- ALOHA 2 platform

## Version/Release Date
GitHub and Hugging Face release: **January 22, 2026**

## Getting Started
Access the model and code via:
- **GitHub:** https://github.com/NVlabs/cosmos-policy
- **Paper:** https://arxiv.org/abs/2601.16163
- **Base model:** Cosmos-Predict2-2B-Video2World
- **Training dataset:** ALOHA-Cosmos-Policy (available on Hugging Face)

Requirements include H100 or A100 GPU with 6.0 GB VRAM minimum, BF16 precision, Linux operating system, and 25 Hz control frequency (not original 50 Hz).
