import numpy as np
import matplotlib.pyplot as plt

dt = 0.02
tf = 50 # total time of simulation in seconds
t = np.arange(0, tf+dt, dt)
m = 10 # mass of the train in kg
x_r = 10
x_init = 0

error = np.zeros(len(t))
f = np.zeros(len(t))
a = np.zeros(len(t))
v = np.zeros(len(t))
x = np.zeros(len(t))

error[0] = x_r - x_init
f[0] = 0


# Control gains for PID controller
Kp = 75
Ki = 100
Kd = 75

integral_error = 0

for i in range(1, len(t)):

    error[i] = x_r - x[i-1] # proportional error
     
    derivative_error = (error[i] - error[i-1])/dt # derivative error

    integral_error += error[i]*dt # integral error

    f[i] = Kp*error[i] + Ki*integral_error + Kd*derivative_error

    v[i] = v[i-1] + (((1/m)*((f[i-1] + f[i])/2))*dt)

    x[i] = x[i-1] + (((v[i-1] + v[i])/2)*dt)

plt.plot(t,x)
plt.show()
