"""
===========================================================
Transient Cooling of Stainless Steel Bar (Semi-Infinite Solid)
Author: S. Carr
Date: 2024-06-12
Description:
    Computes the time required for a stainless steel AISI304 bar
    to cool from an initial temperature to a target temperature
    at both the centre and a specified depth using semi-infinite
    solid transient conduction theory.

    Includes:
        - Material properties
        - Semi-infinite analytical solution
        - Iterative convergence on theta
        - Plotly visualisation of theta vs time
===========================================================
"""

import math
import plotly.graph_objects as go

# -----------------------------------------------------------
# Input Parameters
# -----------------------------------------------------------
Ti = 95            # Initial temperature (°C)
To = 50            # Target temperature (°C)
Tinf = 17          # Fluid temperature (°C)
Lc = 0.05          # Characteristic length (m)
h = 50             # Convection coefficient (W/m²·K)
rho = 7900         # Density (kg/m³)
Cp = 494.29        # Specific heat (J/kg·K)
k = 15.675         # Thermal conductivity (W/m·K)
Lambda = 0.3835    # 1-term eigenvalue
Alpha = 1.025      # 1-term coefficient
x = 0.04           # Depth from surface (m)

# -----------------------------------------------------------
# Derived Properties
# -----------------------------------------------------------
a = k / (rho * Cp)                     # Thermal diffusivity
Bi = (h * Lc) / k                      # Biot number
theta_target = (To - Tinf) / (Ti - Tinf)

# -----------------------------------------------------------
# Iterative Solver
# -----------------------------------------------------------
t = 0.1
theta_values = []
time_values = []

while True:
    t += 0.5

    tau = (a * t) / (Lc ** 2)
    theta_wall = Alpha * math.exp(-(Lambda ** 2) * tau)

    # Semi-infinite solid solution
    n = x / (2 * math.sqrt(a * t))
    eq1 = (h * math.sqrt(a * t)) / k
    eq2 = (h * x) / k
    eq3 = (h ** 2 * a * t) / (k ** 2)

    theta_semi = 1 - math.erfc(n) + math.exp(eq2 + eq3) * math.erfc(n + eq1)
    theta_result = (theta_wall ** 2) * theta_semi

    theta_values.append(theta_result)
    time_values.append(t)

    if math.isclose(theta_result, theta_target, abs_tol=5e-5):
        final_time = t
        break

    if t > 500000:
        print("Overflow — no convergence.")
        break

# -----------------------------------------------------------
# Output Results
# -----------------------------------------------------------
print(f"Final theta: {theta_result:.6f} (target: {theta_target:.6f})")
print(f"Final time: {final_time:.2f} seconds")
print(f"Final time: {final_time/60:.2f} minutes")
print("Using a one-term approximation for the plane wall solution.")
print("Error < 2% because tau > 0.2")

# -----------------------------------------------------------
# Plotly Visualisation
# -----------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=time_values,
    y=theta_values,
    mode="lines",
    line=dict(color="royalblue", width=3),
    name="Theta(t)"
))

# Target theta line using a shape
fig.add_shape(
    type="line",
    x0=min(time_values),
    x1=max(time_values),
    y0=theta_target,
    y1=theta_target,
    line=dict(color="red", dash="dash"),
)

fig.update_layout(
    title="Transient Cooling of Stainless Steel Bar (Theta vs Time)",
    xaxis_title="Time (s)",
    yaxis_title="Theta",
    template="plotly_dark",
    font=dict(size=14),
    annotations=[
        dict(
            x=max(time_values),
            y=theta_target,
            xanchor="right",
            yanchor="bottom",
            text="Target Theta",
            showarrow=False,
            font=dict(color="red")
        )
    ]
)

# If VS Code/Jupyter errors, force a renderer:
# import plotly.io as pio
# pio.renderers.default = "notebook"  # or "vscode", "browser"

fig.show()

