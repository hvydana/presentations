# Earth-2 FourCastNet 3
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/earth-2/models/fourcastnet3

## Model Name
Earth-2 FourCastNet 3

## Description/Overview
"FourCastNet 3 advances global weather modeling by implementing a scalable, geometric machine learning (ML) approach to probabilistic ensemble forecasting." The model respects spherical geometry and accurately models spatially correlated probabilistic dynamics. It delivers forecasting accuracy surpassing conventional ensemble models while producing forecasts "8 to 60 times faster than these approaches." It demonstrates excellent probabilistic calibration and retains realistic spectra even at extended lead times of up to 60 days.

## Use Case
"Industry, academic, and government research teams interested in medium-range and subseasonal-to-seasonal weather forecasting, and climate modeling."

## Model Architecture
"Spherical Neural Operator. A fully convolutional architecture based on group convolutions defined on the sphere." It leverages both local and global convolutions. The architecture contains 710,867,670 parameters and runs in AMP with bf16, though inputs and outputs are typically float32.

## Input Format
- **Type:** PyTorch Tensor with 72 surface and pressure-level variables
- **Dimensions:** Six Dimensional (6D): (batch, time, lead time, variable, latitude, longitude)
- **Grid:** 0.25 degree equi-rectangular, 721 x 1440 resolution
- **Variables:** Include u10m, v10m, u100m, v100m, t2m, msl, tcwv, and pressure-level variables at multiple heights

## Output Format
- **Type:** PyTorch Tensor with 72 surface and pressure-level variables
- **Dimensions:** Six Dimensional (6D): (batch, time, lead time, variable, latitude, longitude)
- **Grid:** 0.25 degree, 721 x 1440 resolution (same as input)

## Training Data
ERA5 data from 1980-2015 containing "hourly estimates of various atmospheric, land, and oceanic climate variables." Dataset partition: training 95%, testing 2.5%, validation 2.5%.

## Intended Users
Industry, academic, and government research teams focused on weather forecasting and climate modeling.

## License
Apache 2.0 license: https://www.apache.org/licenses/LICENSE-2.0

## Tags
PyTorch, CUDA, Forecasting, HPC/Supercomputing, Simulation and Modeling, PhysicsNeMo

## Version and Date
Version 0.1.0, Released July 18, 2025 (Updated July 29, 2025 UTC)

## Getting Started
Access via NGC CLI download tool available on the model page. Code repositories: Makani, PhysicsNeMo, Earth2Studio, and torch-harmonics on GitHub.
