# Designing a PID controller for a magnetic train which tries to catch an object

![Magnetic Train System](magTrain.png)

- The train can only move in horizontal direction (left or right) by the applied force F_a produced by the magnets on the railway track. We assume that the train is magnetic train so that the effect of friction can be neglected.

- The object can be anywhere on the x-y plane, it falls freely by the influence of gravity (F_g).

- The objective of the train is to catch the object before it touches the ground.

- x_r is the position of the object i.e., where the train needs to be (desired position)

- x is the position where the train initially is.

- Error e_x is calculated and accordingly the coontroller adjusts the control input.

## Building the mathematical model for the magnetic train