# Cosmos-Reason1-7B (closest available release to "Cosmos Reason 2 / Cosmos 3")
Source: https://huggingface.co/nvidia/Cosmos-Reason1-7B (NGC catalog page not found — see note below)

## Note on source and naming
NGC catalog URLs tried and 404'd:
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-reason2
- https://catalog.ngc.nvidia.com/orgs/nvidia/models/cosmos-reason2

The requested "Cosmos Reason 2 / Cosmos 3" does not appear to exist as a published model yet under that exact name. The Hugging Face page for nvidia/Cosmos-Reason1-7B explicitly references "Cosmos Predict 2.5" and "Cosmos 3" in linked blog articles, and a collection at https://huggingface.co/collections/nvidia/cosmos-reason1, but no separate "Cosmos-Reason2" or "Cosmos-3" reasoning model page was located. Reproducing the Cosmos-Reason1-7B card below as the closest verified/available reference; treat the "Reason 2 / Cosmos 3" naming as unconfirmed/forthcoming.

## Model Name
**nvidia/Cosmos-Reason1-7B**

## Description/Overview
"NVIDIA Cosmos Reason – an open, customizable, 7B-parameter reasoning vision language model (VLM) for physical AI and robotics" that "enables robots and vision AI agents to reason like humans, using prior knowledge, physics understanding and common sense to understand and act in the real world."

The model "understands space, time, and fundamental physics, and can serve as a planning model to reason what steps an embodied agent might take next." It was "post-trained with physical common sense and embodied reasoning data with supervised fine-tuning and reinforcement learning."

## Use Cases
"Physical AI: Space, time, fundamental physics understanding and embodied reasoning, encompassing robotics, and autonomous vehicles (AV)."

Specific applications include:
- Data curation and annotation
- Robot planning and reasoning
- Video analytics AI agents

## Model Architecture
"A Multi-modal LLM consists of a Vision Transformer (ViT) for vision encoder and a Dense Transformer model for LLM. Network Architecture: Qwen2.5-VL-7B-Instruct."

**Parameter breakdown:**
- Vision Transformer (ViT): 675.76M
- Language Model (LLM): 7.07B
- Other components: 545.00M

## Input/Output Format

**Input:**
- Type: Text + Video/Image
- Formats: Text (string), Video (mp4), Image (jpg)
- Note: "Use `FPS=4` for input video to match the training setup."

**Output:**
- Type: Text (string)
- Recommendation: "4096 or more output max tokens to avoid truncation of long chain-of-thought response."

## Training Data Used

**Datasets (as of 05/17/2025):**
- RoboVQA
- BridgeDataV2
- AgiBot
- RoboFail
- HoloAssist
- AV (Autonomous Vehicle)

**Updated datasets (08/01/2025):**
- PLM-Video-Human
- Nexar
- Describe Anything
- ITS/Warehouse applications
- Visual Critics

**Data collection methods:** Hybrid automatic/sensor-based and human-annotated approaches

## Intended Users
"Physical AI developers"

## License
**Name:** NVIDIA Open Model License

**Full license clause/link:**
"This model is released under the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license). Additional Information: [Apache License 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md)."

**Key provisions:**
- "Models are commercially usable."
- "You are free to create and distribute Derivative Models."
- "NVIDIA does not claim ownership to any outputs generated using the Models or Derivative Models."

## Tags
- Image-Text-to-Text
- Transformers
- Safetensors
- Cosmos
- English
- qwen2_5_vl
- nvidia
- conversational
- text-generation-inference

## Version/Release Date
- **GitHub:** 05/17/2025
- **Hugging Face:**
  - 08/01/2025 (latest improvements)
  - 06/10/2025 (enhanced critic capability)
  - 05/17/2025 (initial release)

## Getting Started Instructions

**Using Transformers:**
```python
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="nvidia/Cosmos-Reason1-7B")
```

**Using vLLM:**
```bash
pip install vllm
vllm serve "nvidia/Cosmos-Reason1-7B"
```

**Using SGLang:**
```bash
pip install sglang
python3 -m sglang.launch_server --model-path "nvidia/Cosmos-Reason1-7B" --host 0.0.0.0 --port 30000
```

## Related Models Referenced
The page references that this model is "Finetuned" from [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct), and links to a collection at https://huggingface.co/collections/nvidia/cosmos-reason1, plus mentions of "Cosmos Predict 2.5" and "Cosmos 3" in linked blog articles.

**Downloads:** 92,963 last month | **Model Size:** 8B params | **Tensor Type:** BF16
