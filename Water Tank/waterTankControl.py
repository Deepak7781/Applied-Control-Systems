import control as ctrl
import numpy as np

s = ctrl.tf('s')

rho = 1000 # Density of water in kg/m^3

G = 1/(rho*s) # Transfer function of the system (Tank)

Kp = 0.5 # Proportional gain

# Closed-loop transfer function with proportional control
T = ctrl.feedback(Kp*G, 1)

ctrl.step_response(T)