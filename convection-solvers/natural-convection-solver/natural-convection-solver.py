"""
===========================================================
Heat Balance Equation - Natural Convection Calculator
Author: S. Carr
Date: 2024-07-27
Description:
    This script calculates heat transfer by natural convection
    using standard thermophysical correlations. It includes
    interpolation of fluid properties, computation of Grashof,
    Rayleigh, and Nusselt numbers, and visualizes the resulting
    heat transfer rate using Plotly.
===========================================================
"""

import math
import numpy as np
import plotly.graph_objects as go

# -----------------------------------------------------------
# Interpolated fluid properties (example: air at mid-range)
# -----------------------------------------------------------
k = 0.02439 + ((2.5 * (0.02476 - 0.02439)) / 5)
v = 1.426e-5 + ((2.5 * ((1.47e-5) - (1.426e-5))) / 5)
Pr = 0.7336 + ((2.5 * (0.7336 - 0.7323)) / 5)

# -----------------------------------------------------------
# Constants and geometry
# -----------------------------------------------------------
g = 9.81          # gravitational acceleration (m/s^2)
B = 1 / 285.5     # thermal expansion coefficient (1/K)
Ts = 25           # surface temperature (°C)
Tinf = 0          # ambient temperature (°C)
H = 2             # height (m)
W = 0.6           # width (m)

# -----------------------------------------------------------
# Natural convection function
# -----------------------------------------------------------
def natural_convection(Ts, Tinf, H, W, k, v, Pr):
    Gr = (g * B * (Ts - Tinf) * (H ** 3)) / (v ** 2)
    Ra = Gr * Pr
    Nu = (0.825 + (0.387 * (Ra ** (1 / 6)) /
          (1 + (0.492 / Pr) ** (9 / 16)) ** (8 / 27))) ** 2
    h = (Nu * k) / H
    Q = h * (H * W) * (Ts - Tinf)
    return Gr, Ra, Nu, h, Q

# -----------------------------------------------------------
# Compute results
# -----------------------------------------------------------
Gr, Ra, Nu, h, Q = natural_convection(Ts, Tinf, H, W, k, v, Pr)

print(f"Grashof Number: {Gr:.3e}")
print(f"Rayleigh Number: {Ra:.3e}")
print(f"Nusselt Number: {Nu:.3f}")
print(f"Heat Transfer Coefficient (h): {h:.3f} W/m²·K")
print(f"Heat Transfer Rate (Q): {Q:.4f} W")

# -----------------------------------------------------------
# Visualization using Plotly
# -----------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Indicator(
    mode="number + gauge + delta",
    value=Q,
    delta={'reference': 100, 'increasing': {'color': "blue"}},
    gauge={'axis': {'range': [None, Q * 1.5]},
           'bar': {'color': "royalblue"},
           'steps': [{'range': [0, Q], 'color': "lightblue"}]},
    title={'text': "Heat Transfer Rate (W)"}
))

fig.update_layout(
    title="Natural Convection Heat Transfer Visualization",
    template="plotly_dark",
    font=dict(size=14)
)

fig.show()
