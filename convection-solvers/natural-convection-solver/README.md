
Natural Convection Heat‑Transfer Calculator (Python / NumPy / Engineering Analysis)
This project implements a natural convection heat‑transfer calculation for a vertical plate using the Churchill–Chu correlation. It demonstrates how engineering physics can be automated using Python, NumPy, and reproducible scientific‑computing practices.

The script computes:
- Grashof number (Gr)
- Rayleigh number (Ra)
- Nusselt number (Nu)
- Convective heat‑transfer coefficient (h)
Finally -> Total heat loss (Q)

This type of calculation is commonly used in thermal design, electronics cooling, HVAC, and general heat‑transfer engineering.

1. Problem Overview
Natural convection occurs when fluid motion is driven by buoyancy forces caused by temperature differences.
For a vertical plate, the heat transfer can be estimated using the Churchill–Chu correlation.
Fluid properties (k, ν, Pr) are linearly interpolated for intermediate temperatures.

The Churchill–Chu correlation is valid for a wide range of Rayleigh numbers.
The model assumes a vertical plate with uniform surface temperature.
This script can be extended for parametric sweeps or sensitivity analysis.

