# PhysicsNeMo Checkpoints: AFNO_DX_TP-V1-ERA5
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/earth-2/models/afno_dx_tp-v1-era5

## Model Name
PhysicsNeMo Checkpoints: AFNO_DX_TP-V1-ERA5 (ERA5 AFNO Accumulated Total Precipitation Diagnostic Model)

## Description/Overview
"This is a 6-hour accumulated surface precipitation diagnostic model checkpoint. This deep learning model, based on the Adaptive Fourier Neural Operator framework (AFNO), predicts 6-hour accumulated surface precipitation given 20 atmospheric variables plus invariants."

## Use Case
Weather forecasting and precipitation prediction, specifically for 6-hour accumulated surface precipitation forecasting given atmospheric state variables.

## Model Architecture
- **Type:** Adaptive Fourier Neural Operator (AFNO)
- **Network Architecture:** AFNO

## Input Format
- **Type:** PyTorch Tensor / NumPy Array
- **Dimensions:** 4D (batch, variable, latitude, longitude)
- **Resolution:** 0.25 degree regular latitude/longitude grid (720 x 1440 pixels)
- **Variables:** 20 atmospheric variables including u10m, v10m, t2m, sp, msl, t850, u1000, v1000, z1000, u850, v850, z850, u500, v500, z500, t500, z50, q500, q850, tcwv plus DateTime (1D NumPy Array)

## Output Format
- **Type:** PyTorch Tensor
- **Dimensions:** 4D (batch, variable, latitude, longitude)
- **Variable:** tp06 (6-hour accumulated surface precipitation)
- **Resolution:** 0.25 degree grid (720 x 1440 pixels)

## Training Data
"ERA5 data for the period January 1980 - December 2016." Data collection and labeling were automatic/sensor-based. ERA5 provides hourly atmospheric, land, and oceanic climate variables on a 30km grid with 137 atmospheric levels.

## Testing Data
"ERA5 data for the date range of January 2017 - December 2018."

## Evaluation Data
"ERA5 data for the date range of January 2019 - December 2020."

## Intended Users
Commercial users; the model is ready for commercial use.

## License
**Name:** NVIDIA Community Model License

**Clause/Link:** "Use of this model is governed by the NVIDIA Community Model License. By pulling and using this model, you accept the terms and conditions of this license."

License URL: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/

## Tags
- Earth-2
- Energy
- English
- Forecasting
- PhysicsNeMo
- PyTorch
- Simulation and Modeling

## Version & Date
**Version:** v0.1.0 (Latest)
**Updated:** April 4, 2025 UTC
**Model Version:** v1

## Download Instructions
Use the NGC CLI to download the model. Compressed size: 494.6 MB

## Getting Started
For training recipes, see NVIDIA PhysicsNeMo: https://github.com/NVIDIA/PhysicsNeMo/tree/main/examples/weather/diagnostic. For inference, see NVIDIA Earth2Studio: https://github.com/NVIDIA/earth2studio.

## Supported Hardware & Software
- **Runtime:** PyTorch
- **Hardware:** NVIDIA Ampere, Hopper, Turing microarchitectures
- **Operating System:** Linux
- **Test Hardware:** A100, H100, L40S
