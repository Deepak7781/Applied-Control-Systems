import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
x_init = 0
x_ref = 10

# PID gains
Kp = 100
Ki = 75
Kd = 75

# Simulation settings
dt = 0.02
t_final = 10
t = np.arange(0, t_final + dt, dt)

# Train parameter
m = 10.0   # mass of train, kg

# Arrays
x = np.zeros(len(t))        # position
v = np.zeros(len(t))        # velocity
a = np.zeros(len(t))        # acceleration
u = np.zeros(len(t))        # control force
error = np.zeros(len(t))    # position error

# Initial values
x[0] = x_init
v[0] = 0
a[0] = 0

# PID memory
integral_error = 0
previous_error = x_ref - x_init

# Simulation loop
for i in range(1, len(t)):

    # Current error
    error[i] = x_ref - x[i-1]

    # Integral of error
    integral_error += error[i] * dt

    # Derivative of error
    derivative_error = (error[i] - previous_error) / dt

    # PID controller output
    u[i] = (
        Kp * error[i]
        + Ki * integral_error
        + Kd * derivative_error
    )

    # Train dynamics: m*x_ddot = u
    a[i] = u[i] / m

    # Trapezoidal integration for velocity
    v[i] = v[i-1] + 0.5 * (a[i-1] + a[i]) * dt

    # Trapezoidal integration for position
    x[i] = x[i-1] + 0.5 * (v[i-1] + v[i]) * dt

    # Update previous error
    previous_error = error[i]

# Plot position response
plt.figure()
plt.plot(t, x, linewidth=2, label="Train Position")
plt.axhline(x_ref, linestyle="--", label="Reference Position")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Magnetic Train Position Control using PID")
plt.grid(True)
plt.legend()

# Plot velocity
plt.figure()
plt.plot(t, v, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Train Velocity")
plt.grid(True)

# Plot acceleration
plt.figure()
plt.plot(t, a, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Train Acceleration")
plt.grid(True)

