# PhysicsNeMo Checkpoints: AFNO_DX_SR-V1-ERA5
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/earth-2/models/afno_dx_sr-v1-era5

## Model Name
PhysicsNeMo Checkpoints: AFNO_DX_SR-V1-ERA5

## Description/Overview
A surface solar irradiance (SSI) diagnostic model checkpoint using the Adaptive Fourier Neural Operator framework. It predicts 6-hour accumulated surface solar irradiance given 24 atmospheric variables plus invariants, based on atmospheric conditions at time t.

## Use Case
Solar irradiance prediction for energy forecasting and climate modeling applications.

## Model Architecture
- **Type:** Adaptive Fourier Neural Operator (AFNO)
- **Network Architecture:** AFNO

## Input Format
- **Type:** PyTorch Tensor / NumPy array
- **Dimensions:** 4D (batch, variable, latitude, longitude)
- **Grid Resolution:** 0.25 degree regular latitude/longitude (720 x 1440 pixels)
- **Variables (24 total):** "t2m, sp, tcwv, z50, z300, z500, z700, z850, z925, z1000, t50, t300, t500, t700, t850, t925, t1000, q50, q300, q500, q700, q850, q925, q1000"
- **Additional Input:** DateTime (NumPy Array, 1D)

## Output Format
- **Type:** PyTorch Tensor
- **Variable:** Surface Solar Irradiance (ssi)
- **Dimensions:** 4D (batch, variable, latitude, longitude)
- **Grid Resolution:** 0.25 degree regular latitude/longitude (720 x 1440 pixels)

## Training Data
"ERA5 data for the period January 1980 - December 2016" covering hourly atmospheric, land, and oceanic climate variables on a 30km global grid with 137 atmospheric levels.

## Testing Data
"ERA5 data for the date range of January 2017 - December 2018" with identical specifications.

## Evaluation Data
"ERA5 data for the date range of January 2019 - December 2020" with identical specifications.

## Intended Users
Developers and researchers working on weather forecasting, solar energy prediction, and climate modeling applications.

## License
**License Name:** NVIDIA Community Model License

**License Link/Clause:** "Use of this model is governed by the NVIDIA Community Model License. By pulling and using this model, you accept the terms and conditions of this license."

License URL: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/

## Tags
Earth-2, Energy, Forecasting, PhysicsNeMo, PyTorch, Simulation and Modeling

## Version/Date
- **Version:** 1.0.0
- **Updated:** May 29, 2025 UTC
- **Compressed Size:** 152.33 MB
- **Status:** Signed (digitally verified)

## Getting Started
**Training recipes:** Available at NVIDIA PhysicsNeMo GitHub: https://github.com/NVIDIA/PhysicsNeMo/tree/main/examples/weather/diagnostic

**Inference:** See NVIDIA Earth2Studio: https://github.com/NVIDIA/earth2studio

## References
- "Advancing Solar Irradiance Prediction with NVIDIA Earth-2"
- "Data-driven Surface Solar Irradiance Estimation using Neural Operators at Global Scale" (arxiv.org/abs/2411.08843)
