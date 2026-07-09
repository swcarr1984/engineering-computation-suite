"""
===========================================================
Cross‑Flow Heat Exchanger Analysis (Mixed–Unmixed)
Author: S. Carr
Date: 2024‑12‑08
Description:
    Compares LMTD and NTU methods for a cross‑flow heat exchanger
    with one fluid mixed and the other unmixed. Includes a Plotly
    bar chart showing outlet temperatures for baseline and doubled
    flow rates.
===========================================================
"""

import math
import plotly.graph_objects as go

# -----------------------------------------------------------
# Input Parameters
# -----------------------------------------------------------
U = 150            # Overall heat transfer coefficient (W/m²·K)
cin = 25           # Cold inlet temperature (°C)
cout = 210         # Cold outlet temperature (°C)
hin = 425          # Hot inlet temperature (°C)
cCp = 1007         # Cold fluid specific heat (J/kg·K)
hCp = 1101.25      # Hot fluid specific heat (J/kg·K)

mh1 = 10           # Hot flow rate (kg/s)
mh2 = 20           # Hot flow rate doubled (kg/s)
mc1 = 10           # Cold flow rate (kg/s)
mc2 = 20           # Cold flow rate doubled (kg/s)

# -----------------------------------------------------------
# Capacity Rates
# -----------------------------------------------------------
Cc = mc1 * cCp
Ch = mh1 * hCp
Cmin = Cc
Cmax = Ch

Q = Cc * (cout - cin)
hout = hin - (Q / Ch)

# -----------------------------------------------------------
# LMTD Method
# -----------------------------------------------------------
dt1 = hin - cout
dt2 = hout - cin
tlm = (dt1 - dt2) / math.log(dt1 / dt2)

F = 0.88  # Correction factor (Cengel Fig. 11.19)
LMTD_area = Q / (U * F * tlm)

# -----------------------------------------------------------
# NTU Method
# -----------------------------------------------------------
c = Cmin / Cmax
Qmax = Cmin * (hin - cin)
effectiveness = Q / Qmax

NTU = -math.log(c * math.log(1 - effectiveness) + 1) / c
NTU_area = (NTU * Cmin) / U

# -----------------------------------------------------------
# Flow‑Doubling Case
# -----------------------------------------------------------
Ch2 = mh2 * hCp
Cc2 = mc2 * cCp

hout2 = hin - (Q / Ch2)
cout2 = cin + (Q / Cc2)

# -----------------------------------------------------------
# Output Summary
# -----------------------------------------------------------
print(f"Cc = {Cc:.2f}, Ch = {Ch:.2f}")
print(f"Heat Transfer Q = {Q:.2f} W")
print(f"Hot Outlet Temperature = {hout:.2f} °C")
print(f"LMTD Area = {LMTD_area:.3f} m²")
print(f"NTU Area = {NTU_area:.3f} m²")
print(f"Effectiveness = {effectiveness:.4f}")
print(f"NTU = {NTU:.4f}")
print(f"Flow‑doubling outlets: Cout2 = {cout2:.2f}, Hout2 = {hout2:.2f}")

# -----------------------------------------------------------
# Plotly Visualisation
# -----------------------------------------------------------
outlet_labels = [
    "Cold Out @ 10 kg/s",
    "Cold Out @ 20 kg/s",
    "Hot Out @ 10 kg/s",
    "Hot Out @ 20 kg/s"
]

outlet_values = [cout, cout2, hout, hout2]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=outlet_labels,
    y=outlet_values,
    marker_color=["royalblue", "lightblue", "firebrick", "indianred"]
))

fig.update_layout(
    title="Outlet Temperatures for Baseline and Doubled Flow Rates",
    xaxis_title="Outlet Stream",
    yaxis_title="Temperature (°C)",
    template="plotly_dark",
    font=dict(size=14)
)

fig.show()

print("Doubling the flow rate reduces the temperature change across each stream.")
