
Heat‑Exchanger Performance Analysis (Python / Thermofluids / LMTD & NTU Methods)
This project implements a cross‑flow heat‑exchanger analysis using both the Log Mean Temperature Difference (LMTD) and Number of Transfer Units (NTU) methods.
It calculates outlet temperatures, effectiveness, and required heat‑transfer area, then visualizes how doubling the flow rate affects thermal performance.

The script demonstrates how engineering thermodynamics can be automated using Python, NumPy, and Matplotlib.

Engineering Background
A heat exchanger transfers energy between two fluids at different temperatures.
Two common design approaches are:
- LMTD Method: based on measured inlet/outlet temperatures and overall heat‑transfer coefficient.
- NTU Method: based on effectiveness and capacity‑rate ratio, useful when outlet temperatures are unknown.

This script compares both methods for a cross‑flow exchanger with one fluid mixed and the other unmixed (per Cengel, Heat and Mass Transfer, Fig. 11.19).

Interpretation
- The LMTD and NTU methods yield nearly identical required areas (~61 m²).
- Doubling the flow rate halves the temperature change of each fluid, confirming energy‑balance consistency.
- The correction factor 𝐹 = 0.88 accounts for cross‑flow geometry.
