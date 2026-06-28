# S.Carr - Heat Balance equation calculation
from matplotlib import pyplot as plt
import numpy as np
import math
%matplotlib inline

# Natural Convection
# Interpolation
k = 0.02439+(((2.5)*(0.02476-0.02439))/5)
v = 1.426e-5+(((2.5)*((1.47e-5)-(1.426e-5)))/5)
Pr = 0.7336+(((2.5)*(0.7336-0.7323))/5)

# Constants
g = 9.81
B = 1/285.5
Ts = 25
Tinf = 0
H = 2
W = 0.6

# Combined function (use as required)
def natural_convection(Ts, Tinf, H, W, k, v, Pr):
    Gr = (g*B*(Ts-Tinf)*(H**3))/(v**2)
    Ra = Gr * Pr
    Nu = (0.825 + (0.387*(Ra**(1/6)) /
         (1+(0.492/Pr)**(9/16))**(8/27)))**2
    h = (Nu*k)/H
    Q = h*(H*W)*(Ts-Tinf)
    return Q

# Pure Equations

Gr = (g*B*(Ts-Tinf)*(H**3))/(v**2)
print('Grashof=',Gr)
Ra = Gr * Pr
print('Rayleigh=',Ra)
Nu = (0.825 + (0.387*(Ra**(1/6))/(1+(0.492/Pr)**(9/16))**(8/27)))**2
print("Complex Nusselt = ",Nu)
h = (Nu*k)/H
print('h=',h)
Q = h*(H*W)*(25-0)
print('The final Q value is:',round(Q,4),'W')
