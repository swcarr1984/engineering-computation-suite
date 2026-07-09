"""
===========================================================
Transient 2‑D Heat Transfer of Disk Brake (Explicit FDM)
Author: S. Carr
Date: 2024‑08‑27
Description:
    Numerical transient 2‑D conduction with convection and jet
    cooling. All node update equations reconstructed from PDF
    image blocks and converted into executable Python.
===========================================================
"""

import math
import numpy as np
import plotly.graph_objects as go

# -----------------------------------------------------------
# Time stepping
# -----------------------------------------------------------
dt = 20
t_init = 0
t_final = 5000
t_total = int(t_final / dt) + 1

# -----------------------------------------------------------
# Temperature matrix
# -----------------------------------------------------------
T = np.zeros((37, t_total))
T[:, 0] = 20   # Initial temperature everywhere

# -----------------------------------------------------------
# Constants
# -----------------------------------------------------------
cp = 200
p = 7000
k = 100
h = 25
hjet = 250
Tinf = 20

dx = 0.2
dy = 0.15

dx_dy = dx / dy
dy_dx = dy / dx

a = k / (p * cp)
tau = (a * dt) / (dx * dy)

# -----------------------------------------------------------
# Main transient loop
# -----------------------------------------------------------
qr = 200000 * (1 - (dt / t_final) ** 2)

for t in range(t_total - 1):

    # -------------------------------------------------------
    # Nodes 1–8 (outer convection boundary)
    # -------------------------------------------------------
    T[1, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[1, t] +
                 tau * (((2*h*dx)/k)*Tinf + 2*dy_dx*T[2, t] + 2*dx_dy*T[13, t]))

    T[2, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[2, t] +
                 tau * (((2*h*dx)/k)*Tinf + dy_dx*T[3, t] + 2*dx_dy*T[14, t] + dy_dx*T[1, t]))

    T[3, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[3, t] +
                 tau * (((2*h*dx)/k)*Tinf + dy_dx*T[4, t] + 2*dx_dy*T[15, t] + dy_dx*T[2, t]))

    T[4, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[4, t] +
                 tau * (((2*h*dx)/k)*Tinf + dy_dx*T[5, t] + 2*dx_dy*T[16, t] + dy_dx*T[3, t]))

    T[5, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[5, t] +
                 tau * (((2*h*dx)/k)*Tinf + dy_dx*T[6, t] + 2*dx_dy*T[17, t] + dy_dx*T[4, t]))

    T[6, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[6, t] +
                 tau * (((2*h*dx)/k)*Tinf + dy_dx*T[7, t] + 2*dx_dy*T[18, t] + dy_dx*T[5, t]))

    T[7, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[7, t] +
                 tau * (((2*h*dx)/k)*Tinf + dy_dx*T[8, t] + 2*dx_dy*T[19, t] + dy_dx*T[6, t]))

    T[8, t+1] = ((1 - ((2*h*dx)/k)*tau - 2*dy_dx*tau - 2*dx_dy*tau) * T[8, t] +
                 tau * (((2*h*dx)/k)*Tinf + dy_dx*T[9, t] + 2*dx_dy*T[20, t] + dy_dx*T[7, t]))

    # -------------------------------------------------------
    # Nodes 9–12 (heat generation region)
    # -------------------------------------------------------
    T[9, t+1] = ((1 - 2*dy_dx*tau - 2*dx_dy*tau) * T[9, t] +
                 tau * (((2*qr*dx)/k) + dy_dx*T[10, t] + 2*dx_dy*T[21, t] + dy_dx*T[8, t]))

    T[10, t+1] = ((1 - 2*dy_dx*tau - 2*dx_dy*tau) * T[10, t] +
                  tau * (((2*qr*dx)/k) + dy_dx*T[11, t] + 2*dx_dy*T[22, t] + dy_dx*T[9, t]))

    T[11, t+1] = ((1 - 2*dy_dx*tau - 2*dx_dy*tau) * T[11, t] +
                  tau * (((2*qr*dx)/k) + dy_dx*T[12, t] + 2*dx_dy*T[23, t] + dy_dx*T[10, t]))

    T[12, t+1] = ((1 - ((2*h*dy)/k)*tau - 2*dx_dy*tau - 2*dy_dx*tau) * T[12, t] +
                  tau * (((2*qr*dx)/k) + ((2*h*dy)/k)*Tinf + 2*dx_dy*T[24, t] + 2*dy_dx*T[11, t]))

    # -------------------------------------------------------
    # Nodes 13–24 (interior conduction)
    # -------------------------------------------------------
    T[13, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[13, t] +
                  tau * (dx_dy*T[1, t] + dy_dx*T[14, t] + dx_dy*T[25, t] + dy_dx*T[14, t]))

    T[14, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[14, t] +
                  tau * (dx_dy*T[2, t] + dy_dx*T[15, t] + dx_dy*T[26, t] + dy_dx*T[13, t]))

    T[15, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[15, t] +
                  tau * (dx_dy*T[3, t] + dy_dx*T[16, t] + dx_dy*T[27, t] + dy_dx*T[14, t]))

    T[16, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[16, t] +
                  tau * (dx_dy*T[4, t] + dy_dx*T[17, t] + dx_dy*T[28, t] + dy_dx*T[15, t]))

    T[17, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[17, t] +
                  tau * (dx_dy*T[5, t] + dy_dx*T[18, t] + dx_dy*T[29, t] + dy_dx*T[16, t]))

    T[18, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[18, t] +
                  tau * (dx_dy*T[6, t] + dy_dx*T[19, t] + dx_dy*T[30, t] + dy_dx*T[17, t]))

    T[19, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[19, t] +
                  tau * (dx_dy*T[7, t] + dy_dx*T[20, t] + dx_dy*T[31, t] + dy_dx*T[18, t]))

    T[20, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[20, t] +
                  tau * (dx_dy*T[8, t] + dy_dx*T[21, t] + dx_dy*T[32, t] + dy_dx*T[19, t]))

    T[21, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[21, t] +
                  tau * (dx_dy*T[9, t] + dy_dx*T[22, t] + dx_dy*T[33, t] + dy_dx*T[20, t]))

    T[22, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[22, t] +
                  tau * (dx_dy*T[10, t] + dy_dx*T[23, t] + dx_dy*T[34, t] + dy_dx*T[21, t]))

    T[23, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau) * T[23, t] +
                  tau * (dx_dy*T[11, t] + dy_dx*T[24, t] + dx_dy*T[35, t] + dy_dx*T[22, t]))

    T[24, t+1] = ((1 - dx_dy*tau - ((2*h*dy)/k)*tau - dx_dy*tau - dy_dx*tau) * T[24, t] +
                  tau * (dx_dy*T[12, t] + ((2*h*dy)/k)*Tinf + dy_dx*T[36, t] + dy_dx*T[23, t]))

    # -------------------------------------------------------
    # Nodes 25–36 (jet cooling region)
    # -------------------------------------------------------
    T[25, t+1] = ((1 - 2*dx_dy*tau - 2*dy_dx*tau - ((2*hjet*dx)/k)*tau) * T[25, t] +
                  tau * (2*dx_dy*T[13, t] + 2*dy_dx*T[26, t] + ((2*hjet*dx)/k)*Tinf))

    T[26, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[26, t] +
                  tau * (dx_dy*T[14, t] + dy_dx*T[27, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[25, t]))

    T[27, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[27, t] +
                  tau * (dx_dy*T[15, t] + dy_dx*T[28, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[26, t]))

    T[28, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[28, t] +
                  tau * (dx_dy*T[16, t] + dy_dx*T[29, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[27, t]))

    T[29, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[29, t] +
                  tau * (dx_dy*T[17, t] + dy_dx*T[30, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[28, t]))

    T[30, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[30, t] +
                  tau * (dx_dy*T[18, t] + dy_dx*T[31, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[29, t]))

    T[31, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[31, t] +
                  tau * (dx_dy*T[19, t] + dy_dx*T[32, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[30, t]))

    T[32, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[32, t] +
                  tau * (dx_dy*T[20, t] + dy_dx*T[33, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[31, t]))

    T[33, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[33, t] +
                  tau * (dx_dy*T[21, t] + dy_dx*T[34, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[32, t]))

    T[34, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[34, t] +
                  tau * (dx_dy*T[22, t] + dy_dx*T[35, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[33, t]))

    T[35, t+1] = ((1 - dx_dy*tau - dy_dx*tau - ((2*hjet*dx)/k)*tau - dy_dx*tau) * T[35, t] +
                  tau * (dx_dy*T[23, t] + dy_dx*T[36, t] + ((2*hjet*dx)/k)*Tinf + dy_dx*T[34, t]))

    T[36, t+1] = ((1 - 2*dx_dy*tau - ((2*h*dy)/k)*tau - ((2*hjet*dx)/k)*tau - 2*dy_dx*tau) * T[36, t] +
                  tau * (2*dx_dy*T[24, t] + ((2*h*dy)/k)*Tinf + ((2*hjet*dx)/k)*Tinf + 2*dy_dx*T[35, t]))

    # Update heat generation term
    qr = 200000 * (1 - ((t+1)*dt / t_final) ** 2)

# -----------------------------------------------------------
# Output sample nodes
# -----------------------------------------------------------
span = int((t_total - 1) / 5)

print("T1:", T[1, span*1], T[1, span*2], T[1, span*3], T[1, span*4], T[1, span*5])
print("T2:", T[2, span*1], T[2, span*2], T[2, span*3], T[2, span*4], T[2, span*5])
print("T3:", T[3, span*1], T[3, span*2], T[3, span*3], T[3, span*4], T[3, span*5])
import plotly.graph_objects as go

# -----------------------------------------------------------
# Choose snapshot time (same as your assignment: 1 second)
# -----------------------------------------------------------
time_index = span * 1   # or span*2, span*3, etc.

temps = T[1:37, time_index]

# -----------------------------------------------------------
# 3 rows × 12 columns layout
# -----------------------------------------------------------

x_positions = []
y_positions = []

# Row 3 (top): nodes 1–12
for i in range(12):
    x_positions.append(i+1)
    y_positions.append(3)

# Row 2: nodes 13–24
for i in range(12):
    x_positions.append(i+1)
    y_positions.append(2)

# Row 1 (bottom): nodes 25–36
for i in range(12):
    x_positions.append(i+1)
    y_positions.append(1)

# -----------------------------------------------------------
# Plotly scatter heat‑map (3×12 grid)
# -----------------------------------------------------------

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_positions,
    y=y_positions,
    mode="markers+text",
    text=[str(i) for i in range(1,37)],
    textposition="middle center",
    marker=dict(
        size=55,
        color=temps,
        colorscale="Turbo",
        colorbar=dict(title="Temperature (°C)")
    )
))

fig.update_layout(
    title=f"Temperature Distribution at t = {time_index*dt} seconds",
    xaxis=dict(title="Node Column", range=[0.5, 12.5], dtick=1),
    yaxis=dict(title="Node Row", range=[0.5, 3.5], dtick=1),
    template="plotly_dark",
    width=1200,
    height=400
)

fig.show()
