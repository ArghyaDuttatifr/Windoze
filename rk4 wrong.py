import numpy as np
import matplotlib.pyplot as plt
import math as m

def fun(t,x):
    # This is the right-hand side of the first-order ordinary differential 
    # equation dx/dt = fun.
#    fun = 3*t**2 
    fun = m.exp(-0.25*x*(t-1)**2)
    return fun
    
# Set initial conditions.
t = 0
x = 0.2

# Set initial step size.
dt = 1e-2

# Set minimal step size.
dt_min = 1e-3

# Set relative change tolerances.
dx_max = 0.01  # Enables faster speed.
dx_min = 0.008 # Controls accuracy.
x_tol = 1e-3
nag= [0]*4000
for i in range (0,50):
    
    # Calculate partial steps.
    k1 = fun(t,      x)
    k2 = fun(t+dt/2, x+dt*k1/2)
    k3 = fun(t+dt/2, x+dt*k2/2)
    k4 = fun(t+dt,   x+dt*k3)
    # Combine partial steps.
    step_x = x + dt/6*(k1+2*k2+2*k3+k4)

    # Calculate partial steps.
    k5 = fun(t+dt/4, x+dt*k1/4)
    k6 = fun(t+dt/4, x+dt*k5/4)
    k7 = fun(t+dt/2, x+dt*k6/2)
    # Combine partial steps.
    half_step_x = x + dt/12*(k1+2*k5+2*k6+k7)

    # Calculate partial steps.
    k8 = fun(t+dt,   x+dt*k1)
    k9 = fun(t+dt,   x+dt*k8)
    k10= fun(t+2*dt, x+2*dt*k9)
    # Combine partial steps.
    dble_step_x = x + dt/3*(k1+2*k2+2*k3+k4)

    if (abs(step_x) < x_tol): # Use a fixed step size for small values of x.
        if (dt != dt_min):
            print("New step size",dt_min)
            dt = dt_min
        new_x = step_x
    else:
        if (abs(step_x) > x_tol and abs(step_x-half_step_x)/abs(step_x) > dx_max):
            dt = dt/2 # Error is too large; decrease step size.
            print("New step size",dt)
            new_x = half_step_x
        elif (abs(step_x) > x_tol and abs(step_x-dble_step_x)/abs(step_x) < dx_min):
            dt = dt*2 # Larger error is acceptable; increase step size.
            print("New step size",dt)
            new_x = dble_step_x
        else:
            new_x = step_x # This step size is just right.

    nag[i] = new_x
    t = t + dt
    
xx=np.linspace(0,1,4000)
plt.plot(xx,nag)
plt.show()

