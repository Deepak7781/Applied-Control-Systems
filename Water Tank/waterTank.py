import numpy as np
import matplotlib.pyplot as plt 

# Parameters
Vol_T = 100 # Total volume of the tank in m^3
Kp = 0.5 # Proportional gain
Ref_Vol = 50 # Desired Output (Volume) in m^3

rho = 1000 # Density of water in kg/m^3
dt = 0.02 # Time step in seconds
t = np.arange(0, 50+dt, dt)
mdot_in = np.zeros(len(t)) # Inflow rate in m^3/s
Vol_I = np.zeros(len(t)) # Initial volume of water in the tank in m^3

for i in range(1, len(t)):
    error_C = Ref_Vol - Vol_I[i]
    mdot_in[i] = Kp * error_C # Inflow rate in m^3/s
    Vol_I[i] = Vol_I[i-1] + (((mdot_in[i] + mdot_in[i-1])/2) * dt) # Update the volume of water in the tank

plt.plot(t, Vol_I, label='Volume of Water in Tank (m^3)')