# S.Carr - Heat exchanger analysis with bar plot
# This script compares both methods for a cross‑flow exchanger 
# with one fluid mixed and the other unmixed

from matplotlib import pyplot as plt
import numpy as np
import math
%matplotlib inline

print('******** Question 2 ******** ')
U = 150
cin = 25
cout = 210
hin = 425
cCp = 1007
hCp = 1101.25
mh1 = 10   # hot flow rate initially
mh2 = 20   # hot flow when doubled
mc1 = 10
mc2 = 20
Cc = mc1*cCp
Ch = mh1*hCp
print('Cc=',Cc,'Ch=',Ch)
Cmin = Cc
Cmax = Ch
Q = Cc*(cout-cin)
print('Q=',Q)
hout = hin-(Q/Ch)
print('Th out temp =',hout)
dt1 = hin-cout
dt2 = hout-cin
tlm = (dt1-dt2)/(math.log(dt1/dt2))
print('Delta Tlm is:',tlm)
F = 0.88 # correction factor from Cengel fig 11.19
LMTD_As = Q/(U*F*tlm)
print('The LMTD method area is:',LMTD_As)
c = Cmin/Cmax
Qmax = Cmin*(hin-cin)
e = Q/Qmax
print('c=',c,'e=',e)
NTU = (-math.log(c*math.log(1-e)+1))/c
print('NTU=',NTU)
NTU_As = (NTU*Cmin)/U
print('The NTU method area is:',NTU_As)

Ch2 = mh2*hCp
Cc2 = mc2*cCp
hout2 = hin-(Q/Ch2)
cout2 = cin+(Q/Cc2)

print(cout,hout,cout2,hout2)

heights = [cout,cout2,hout,hout2]
x_pos = [1,2,3,4]
plt.bar(x_pos,heights)
plt.title("Outlet temperatures of heat exhanger with flow doubling")
plt.xlabel('Outlets')
plt.ylabel('Outlet Temperature (deg C)')
outlets = ['Cout @ 10kg/s','Cout @ 20kg/s','Hout @ 10kg/s','Hout @ 20kg/s']
plt.xticks([1,2,3,4], outlets)
plt.grid(axis='y')
plt.show()
print('Doubling the flowrate of the fluid halves the inlet/outlet temperature delta of the given stream ')