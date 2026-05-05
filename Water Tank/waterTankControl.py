import control as ctrl
import matplotlib.pyplot as plt

s = ctrl.tf('s')

rho = 1000 # Density of water in kg/m^3

G = 1/(rho*s) # Transfer function of the system (Tank)

Kp = 50 # Proportional gain

# Closed-loop transfer function with proportional control
T = ctrl.feedback(Kp*G, 1)

t, y = ctrl.step_response(T)

plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Volume')
plt.title('Closed Loop Step Response')
plt.grid()
plt.show()