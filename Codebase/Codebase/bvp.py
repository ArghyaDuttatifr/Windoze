from cmath import exp, sin
import matplotlib.pyplot as plt
import numpy as np

from colors import *
from integration import *

# define the equation
def kernel (u, t):
    x_der = u[1]
    vx_der = 0.
    y_der = u[3]
    vy_der = -9.8         
    return np.array([x_der, vx_der, y_der, vy_der])

# Integration routine
def Integrator(u0, t0, tf, N, kernel, routine):
    # initialise vars
    h = (tf-t0)/N
    un = u0
    
    # initialise x, v arrays
    x_arr = [un[0]]
    y_arr = [un[2]]

    # iterator
    for i in range (0, N):
        un = routine(t0 + i*h, un, h, kernel)
        x_arr.append(un[0])
        y_arr.append(un[2])

    return un, x_arr, y_arr

def secant(v1, v2, x1, x2, xf):
    return v1 + (xf - x1)*(v1 - v2)/(x1 - x2)

# bvp routine
def bvp(x0, xf, y0, yf, t0, tf, N, kernel, routine, vx1, vx2, vy1, vy2, tol):
    u1, x1_arr, y1_arr = Integrator([x0, vx1, y0, vy1], t0, tf, N, kernel, routine)
    u2, x2_arr, y2_arr = Integrator([x0, vx2, y0, vy2], t0, tf, N, kernel, routine)

    # luck check
    if (abs(u1[0] - xf) < tol and abs(u1[2] - yf) < tol):
        # plt.plot(np.linspace(t0, tf, N+1), x1_arr, linewidth=1, color= blue)
        plt.plot(x1_arr, y1_arr, linewidth=1, color= red)

    i = 0   # iterator
    
    # iteration loop
    while (i < 100):
        # exit condition
        if (abs(u2[0] - xf) < tol and abs(u2[2] - yf) < tol):
            # plt.plot(np.linspace(t0, tf, N+1), x2_arr, linewidth=1, color= blue)
            # plt.plot(np.linspace(t0, tf, N+1), y2_arr, linewidth=1, color= red)
            plt.plot(x2_arr, y2_arr, linewidth=1, color= red)
            print(i)
            print(vx2)
            break
        else:
            vxm = secant(vx1, vx2, u1[0], u2[0], xf)
            vym = secant(vy1, vy2, u1[2], u2[2], yf)
            vx1 = vx2
            vx2 = vxm
            vy1 = vy2
            vy2 = vym
            u1[0] = u2[0]
            u2, x2_arr, y2_arr = Integrator([x0, vx2, y0, vy2], t0, tf, N, kernel, routine)
            i += 1



t0 = 0.
tf = 2.
x0 = 0.
xf = 50.
y0 = 0.
yf = 0.
vx1 = 20.
vx2 = 26.
vy1 = 8.
vy2 = 11.
tol = 1e-9

bvp(x0, xf, y0, yf, t0, tf, 200, kernel, rk4, vx1, vx2, vy1, vy2, tol)

# plt.legend(("x", "v"),loc='upper right')
# plt.hlines(0, t0, tf, 'k', 'dashed')
plt.margins(x=0, y=0)
plt.title("BVP")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
