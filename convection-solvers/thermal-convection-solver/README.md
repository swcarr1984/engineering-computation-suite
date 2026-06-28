
Transient Cooling of a Stainless‑Steel Bar (Semi‑Infinite Solid Model)
This script implements a transient heat‑conduction model for a stainless‑steel (AISI 304) rectangular bar submerged in water. The goal is to determine the time required for:

The centre temperature, and a point 40 mm from the bottom surface
to cool from 95 °C to 50 °C, assuming:
- convection coefficient: 50 W/m²·K
- water temperature: 17 °C
- bar dimensions: 100 × 100 mm
- semi‑infinite solid approximation

The script solves the problem using analytical transient conduction equations combined with Newton cooling at the boundary.

This is a realistic thermal‑engineering calculation used in metallurgy, quenching, materials processing, and cooling‑rate estimation.

1. Engineering Background
A stainless‑steel bar initially at high temperature is submerged in cooler water. Heat is removed through:
- Convection at the surface
- Transient conduction inside the solid

Because the bar is large relative to the penetration depth of the thermal wave, it can be treated as a semi‑infinite solid, allowing use of the analytical solution.

Features of This Implementation
Uses material properties for AISI 304 stainless steel

Computes:
- Biot number
- Fourier number
- Dimensionless temperature
- Semi‑infinite conduction solution
- Iteratively solves for the cooling time
- Includes error tolerance and overflow protection

Reports:
- Final time in seconds and minutes
- dimensionless parameters
- numerical error
