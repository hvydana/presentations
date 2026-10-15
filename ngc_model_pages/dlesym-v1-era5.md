# PhysicsNeMo Checkpoints: DLESyM-V1-ERA5
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/earth-2/models/dlesym-v1-era5

## Model Name
PhysicsNeMo Checkpoints: DLESyM-V1-ERA5

## Description/Overview
"DLESyM-V1-ERA5 is an ensemble forecast model for global earth system modeling" with atmosphere and ocean components. The model operates at 6-hour temporal resolution, forecasting 8 atmospheric variables and 1 oceanic variable on a HEALPix nside=64 (approximately 1 degree) resolution grid. The package includes multiple trained checkpoints for both components to improve ensemble variability. "This model is for research and development only."

## Use Case
"Industry, academic, and government research teams interested in subseasonal-to-seasonal weather forecasting, and climate modeling."

## Model Architecture
- **Type:** Two UNet architectures adapted to the HEALPix grid—one for atmosphere, one for ocean
- **Network:** UNet with modified padding operations for HEALPix grid support

## Input Format
- **Type:** PyTorch Tensor (9 surface and pressure-level variables)
- **Dimensions:** Six Dimensional (batch, lead time, variable, face, height, width)
- **Variables:** z500, tau300-700, z1000, t2m, tcwv, t850, z250, ws10m, sst
- **Grid:** 0.25 degree 721 x 1440 regridded to HEALPix nside=64 in "XY" format

## Output Format
- **Type:** PyTorch Tensor (9 surface and pressure-level variables)
- **Dimensions:** Six Dimensional (batch, lead time, variable, face, height, width)
- **Variables:** Same as input (z500, tau300-700, z1000, t2m, tcwv, t850, z250, ws10m, sst)
- **Grid:** 0.25 degree 721 x 1440 regridded to HEALPix nside=64

## Training Data
- **Dataset:** ERA5 from Copernicus Climate Data Store
- **Period:** 1980-2015
- **Collection Method:** Automatic/Sensors
- **Resolution:** Regridded from 30km grid to HEALPix-64 grid (~1 degree)
- **Partition:** Training 90%, testing 5%, validation 5%
- **Total Data Points:** 110,960

## Testing Dataset
- **Link:** ERA5
- **Period:** 2016-2017
- **Collection:** Automatic/Sensors
- **Properties:** Same regridding as training data

## Evaluation Dataset
- **Link:** ERA5
- **Period:** 2018-2019
- **Collection:** Automatic/Sensors
- **Properties:** Same regridding as training data

## Intended Users
Industry, academic, and government research teams focused on weather forecasting and climate modeling

## License
**Name:** NVIDIA Community Model License

**Link:** https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/

**Clause:** "Use of this model is governed by the NVIDIA Community Model License."

## Tags
AI, Earth-2, Forecasting, High Performance Computing, HPC/Supercomputing, PhysicsNeMo, PyTorch, Simulation and Modeling

## Version & Date
- **Version:** 1.0.1 (Latest, Signed)
- **Release Date:** NGC 05/12/2025
- **Updated:** May 13, 2025 UTC

## Download Instructions
"Use the NGC CLI to download:" (specific command provided via copy button on NGC website)

## Supported Hardware
- **Microarchitecture:** NVIDIA Ampere, Hopper, Turing
- **Operating System:** Linux
- **Test Hardware:** A100, H100, L40S
- **Runtime:** PyTorch

## References
- Advancing Parsimonious Deep Learning Weather Prediction using the HEALPix Mesh (arXiv:2311.06253)
- A Deep Learning Earth System Model for Efficient Simulation of the Observed Climate (arXiv:2409.16247)
