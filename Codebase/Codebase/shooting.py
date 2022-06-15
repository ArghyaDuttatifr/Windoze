from math import exp, sin
import matplotlib.pyplot as plt
import numpy as np

from colors import *
from integration import *

# define the equation
def kernel (u, t):
    x_der = u[1]
    vx_der = u[1] - sin(t)       
    return np.array([x_der, vx_der])

# Integration routine
def Integrator(u0, t0, tf, N, kernel, routine):
    # initialise vars
    h = (tf-t0)/N
    un = u0
    
    # initialise x, v arrays
    x_arr = [un[0]]
    vx_arr = [un[1]]

    # iterator
    for i in range (0, N):
        un = routine(t0 + i*h, un, h, kernel)
        x_arr.append(un[0])
        vx_arr.append(un[1])

    return un

def secant(v1, v2, x1, x2, xf):
    return v1 + (xf - x1)*(v1 - v2)/(x1 - x2)

# bvp routine
def bvp(vx1, vx2, xf, t0, tf, N, kernel, routine, tol):
    u1 = Integrator([0, vx1], t0, tf, N, kernel, routine)
    u2 = Integrator([0, vx2], t0, tf, N, kernel, routine)

    # luck check
    if (abs(u1[0] - xf) < tol):
        # plt.plot(np.linspace(t0, tf, N+1), x1_arr, linewidth=1, color= blue)
        # plt.plot(x1_arr, y1_arr, linewidth=1, color= red)
        print(vx1)
        print(u1)

    i = 0   # iterator
    
    # iteration loop
    while (i < 100):
        # exit condition
        if (abs(u2[0] - xf) < tol):
            # plt.plot(np.linspace(t0, tf, N+1), x2_arr, linewidth=1, color= blue)
            # plt.plot(np.linspace(t0, tf, N+1), y2_arr, linewidth=1, color= red)
            print(vx2)
            break
        else:
            vxm = secant(vx1, vx2, u1[0], u2[0], xf)
            vx1 = vx2
            vx2 = vxm
            u1[0] = u2[0]
            u2 = Integrator([0, vx2,], t0, tf, N, kernel, routine)
            print(vx2)
            input()
            i += 1

vx1 = -1
vx2 = -10

tol = 1e-5
N = 10000

bvp (vx1, vx2, 0, 0, 1, N, kernel, rk4, tol)