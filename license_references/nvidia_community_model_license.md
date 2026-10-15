# NVIDIA Community Model License

Source: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/

Used by 5 models in the NGC physical-AI list (Earth-2/PhysicsNeMo weather models: AFNO_DX_FI/SR/TP/WG-V1-ERA5, DLESyM-v1-ERA5).

## Commercial Use — CONDITIONAL
> "to exercise these grants in production you must use an NVIDIA Inference Microservice runtime (NVIDIA NIM) available through an NVIDIA AI Enterprise subscription"

Exceptions that avoid the NIM/AI-Enterprise requirement:
- Models designated for RTX/GeForce RTX GPUs: usable if "not used in a commercial kiosk, server or similar system used to service multiple users" — i.e. single-user, and still tied to NVIDIA RTX/GeForce hardware.
- Models on NVIDIA's approved list: "used locally on an end user device."

## Redistribution
Permitted: "distribute NVIDIA Models and Derivative Models with a copy of this Agreement." Modified files must carry notices stating they were changed.

**Prohibited use:** cannot use the model to "develop or improve any other AI models (excluding NVIDIA Models or Derivative Models), unless approved by NVIDIA in writing." This blocks using the weights to train/improve a competing (e.g. AMD-affiliated) model.

## Hardware/Software Tie
Real and explicit: production commercial deployment requires either NVIDIA's own inference runtime (NIM, gated behind an AI Enterprise subscription) or an NVIDIA RTX/GeForce GPU specifically. There is no path to commercial production use that avoids NVIDIA's software or hardware stack.
