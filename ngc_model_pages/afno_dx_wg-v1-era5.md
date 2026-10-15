# PhysicsNeMo Checkpoints: AFNO_DX_WG-V1-ERA5
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/earth-2/models/afno_dx_wg-v1-era5

## Model Name
PhysicsNeMo Checkpoints: AFNO_DX_WG-V1-ERA5 (AFNO ERA5 Wind Gust Diagnostic)

## Description/Overview
A deep learning checkpoint that "predicts 6-hour maximum 3-second wind gusts given 20 atmospheric variables plus invariants," defined as the maximum wind speed value over a 6-hour period of 3-second running average wind speed.

## Use Case
Weather forecasting and wind gust prediction for meteorological applications.

## Model Architecture
- **Type:** Adaptive Fourier Neural Operator (AFNO)
- **Framework:** Based on AFNO architecture as described in the FourCastNet paper

## Input Format
- **Type:** PyTorch Tensor / NumPy Array
- **Dimensions:** 4D (batch, variable, latitude, longitude)
- **Resolution:** 0.25 degree regular grid (720 x 1440 pixels)
- **Variables:** 20 surface and atmospheric variables including u100m, v100m, msl, u/v wind components at multiple levels, temperature, geopotential, and specific humidity
- **Additional Input:** DateTime (1D NumPy Array)

## Output Format
- **Type:** PyTorch Tensor
- **Variable:** fg10 (maximum 3-second wind speed gusts)
- **Dimensions:** 4D (batch, variable, latitude, longitude)
- **Resolution:** 0.25 degree regular grid (720 x 1440 pixels)

## Training Data
ERA5 reanalysis data spanning "January 1980 - December 2016" with hourly atmospheric estimates on 30km grid with 137 vertical levels.

## Testing & Evaluation Data
- **Testing:** ERA5 data "January 2017 - December 2018"
- **Evaluation:** ERA5 data "January 2019 - December 2020"

## Intended Users
Commercial users and researchers in weather forecasting and climate modeling.

## License
**Name:** NVIDIA Community Model License

**Exact Clause/Link:** "Use of this model is governed by the NVIDIA Community Model License. By pulling and using this model, you accept the terms and conditions of this license."

License URL: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/

## Tags
- Earth-2
- Energy
- Forecasting
- PhysicsNeMo
- PyTorch
- Simulation and Modeling

## Version & Date
- **Version:** v0.1.0 (Latest)
- **Updated:** April 4, 2025 UTC
- **Compressed Size:** 621.37 MB

## Getting Started/Download
Use NGC CLI to download; for training recipes see NVIDIA PhysicsNeMo repository; for inference see NVIDIA Earth2Studio repository.

## Hardware Compatibility
- NVIDIA Ampere, Hopper, Turing architectures
- Tested on: A100, H100, L40S
- Operating System: Linux
