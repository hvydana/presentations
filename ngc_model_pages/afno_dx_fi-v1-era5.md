# PhysicsNeMo Checkpoints: AFNO_DX_FI-V1-ERA5
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/earth-2/models/afno_dx_fi-v1-era5

## Model Name
PhysicsNeMo Checkpoints: AFNO_DX_FI-V1-ERA5

## Version
v0.1.0 (Updated April 4, 2025 UTC)

## Description
A forecast interpolation diagnostic model that "interpolates a prognostic forecast model to a shorter time-step size (by default from 6 h to 1 h)" operating on a 0.25-degree latitude-longitude grid with 73 atmospheric variables.

## Use Case
Weather forecasting and temporal interpolation of atmospheric predictions.

## Model Architecture
Adaptive Fourier Neural Operator (AFNO) framework.

## Input Format
- 5D PyTorch tensors or NumPy arrays (batch, time, variable, latitude, longitude)
- 73 atmospheric variables at 0.25-degree resolution (720 x 1440 pixels)
- DateTime as 1D NumPy array
- Variables include surface measurements (u10m, v10m, t2m, sp, msl, tcwv) and pressure-level data

## Output Format
5D PyTorch tensors with 1-hourly interpolated forecasts at identical grid resolution and variable set as inputs.

## Training Data
ERA5 reanalysis (January 1980-December 2016) from the Copernicus Climate Change Service.

## Testing Data
ERA5 (January 2017-December 2018)

## Evaluation Data
ERA5 (January 2019-December 2020)

## License
"Use of this model is governed by the NVIDIA Community Model License. By pulling and using this model, you accept the terms and conditions of this license."
License link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/

## Intended Users
Commercial users; model is cleared for commercial use.

## Tags
Earth-2, Energy, Forecasting, PhysicsNeMo, Simulation and Modeling

## Getting Started
Use NGC CLI for download. For training recipes, see NVIDIA PhysicsNeMo repository. For inference, see NVIDIA Earth2Studio.
