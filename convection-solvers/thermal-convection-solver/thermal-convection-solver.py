
# S.Carr - Python (Jupyter) Thermodynamics program
# A stainless steel (AISI304) long rectangular bar 100×100mm is initially at 95 ◦C. The bar
# is submerged in water at constant temperature of 17 ◦C. Determine the time it takes for the
# bar centre temperature and at a distance in Z axis of 40mm from the bottom edge to reach 50
# ◦C. Assume the convection coefficient of 50W/m2.K. Solve as a semi-infinite bar.

import math

# List variables

Ti = 95           # Initial temp
To = 50           # Final temp
Tinf = 17         # Fluid temp
Lc = 0.05         # Lc (m) = half of L and W = 0.5 x 100mm
h = 50            # convection coeff
p = 7900          # density
Cp = 494.29       # spec heat
k = 15.675        # therm cond
Lambda = 0.3835   # 1D equation lambda
Alpha = 1.025     # 1D equation alpha  
t = 0.1           # initial time
x = 0.04          # z distance

# Equations

a = k/(p*Cp)                          # material alpha
Bi = (h*Lc)/k                         # Biot number
thetaFinal = ((To-Tinf)/(Ti-Tinf)) 

flag = 1

while(flag == 1):
    
    t = t+0.5
    
    # time dependent equations
    tau = (a*t)/(Lc**2)
    thetaWall = (Alpha)*math.exp(-((Lambda)**2)*(tau)) 
    
    # Semi Inf solid analytical equations
    n = x/(2 *math.sqrt(a*t))
    eq1 = (h*math.sqrt(a*t))/k
    eq2 = (h*x)/k
    eq3 = (h**2*a*t)/(k**2)
    thetaSemiInf = 1 - math.erfc(n)+((math.exp(eq2+eq3))*(math.erfc(n+eq1)))
    thetaResult = ((thetaWall**2)*(thetaSemiInf))
    if math.isclose(thetaResult, thetaFinal, abs_tol = 0.00005) == True:
        time = t
        flag = 0
        print('Final calculated theta is:',round((thetaResult),6),'Target theta is:',round((thetaFinal),6))
        error = abs(abs(thetaResult)-abs(thetaFinal))
        print('Error term is:',error)

        
    if t > 500000:
        flag = 0
        print('overflow, error')
        
print('Tau is:',round(tau,5))
print('Final Theta is:',round(thetaFinal,8))    
print('Final time is',time,'seconds')
print('Using a one-term approximation for the two plane wall equations')
print('The answer is:',round(time/60,2),'minutes')
print('This means that the error is < 2% as tau is greater than 0.2')