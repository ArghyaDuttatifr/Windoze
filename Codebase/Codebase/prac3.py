from cmath import cos, exp, pi, sin, sqrt
import matplotlib.pyplot as plt
import numpy as np

from colors import *
from integration import *

D = 1e-3
m = 160e-3

# define the equation
def kernel (u, t):
    x_der = u[1]
    vx_der = -(D/m)*u[1]*sqrt(u[1]*u[1] + u[3]*u[3])
    y_der = u[3]
    vy_der = -9.8 -(D/m)*u[3]*sqrt(u[1]*u[1] + u[3]*u[3])        
    return np.array([x_der, vx_der, y_der, vy_der])

# Integration routine
def Integrator(u0, t0, h, kernel, routine):
    # initialise vars
    un = u0
    tn = t0

    # initialise x, v arrays
    x_arr = [un[0]]
    y_arr = [un[2]]

    i = 0
    # iterator
    while(un[2] > 0):
        un = routine(tn, un, h, kernel)
        x_arr.append(un[0])
        y_arr.append(un[2])
        tn += h

    return un

def angDist(x0, y0, v, h):
    dist_arr = []
    for theta in np.linspace(0, pi/2, 100):
        u0 = [x0, v*cos(theta), y0, v*sin(theta)]
        un = Integrator(u0, 0, h, kernel, rk4)
        dist_arr.append(un[0])

    plt.plot(np.linspace(0, pi/2, 100), dist_arr, linewidth=1, color= blue)

angDist(0, 1.8, 100/3, 0.1)
plt.margins(x=0, y=0)
plt.title("Max Dist")
plt.xlabel("theta")
plt.ylabel("dist")
plt.show()