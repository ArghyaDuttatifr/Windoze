from math import sin
import matplotlib.pyplot as plt
import numpy as np

from colors import *
from integration import *

m = 1
omega = 5
d = 3.5355
a = 0.2
omega_f = 5
x0 = 0
v0 = 1
t0 = 0
tf = 10

def func(x, v, t):
 return -m*omega*omega*x

# derivative kernel
def kernel (u, t):
    x_der = u[1]                   # dx/dt
    v_der = -m*omega*omega*u[0] + d*u[1]*u[1]   # dv/dt
    return np.array([x_der, v_der])

# Stoermer’s rule
# Numerical Recipies W. Press 17.4
def Stoermer(N, func):
    h = (tf-t0)/N
    xnn = x0
    xn = xnn + h*(v0 + (h/2)*func(xnn, v0, t0))
    x_arr = [x0]
    v_arr = [v0]
    for i in range(1, N):
        vn = (xn - xnn)/h + (h/2)*func(xn, vn, t0+i*h)
        x_arr.append(xn)
        v_arr.append(vn)
        temp = 2*xn - xnn + h*h*func(xn, vn, t0 + i*h)
        xnn = xn
        xn = temp

    # plt.plot([t0 + i*h for i in range(0,N)], x_arr, blue)
    # plt.plot([t0 + i*h for i in range(0,N)], v_arr, red)
    plt.plot(x_arr, v_arr, red)

# RK4
# https://en.smath.com/wiki/GetFile.aspx?File=Examples/RK4-2ndOrderODE.pdf
def rk4Int(N, kernel):
    h = (tf-t0)/N   # step size
    un = np.array([x0, v0])   # x, v

    # initialise x, v arrays
    x_arr = [un[0]]
    v_arr = [un[1]]
    vp_arr = [m*omega*omega*un[0] - d*un[1]*un[1]]

    # iteration loop
    for i in range(0, N):
        un = rk4(t0 + i*h, un, h, kernel)
        x_arr.append(un[0])
        v_arr.append(un[1])
        vp_arr.append(m*omega*omega*un[0] - d*un[1]*un[1])

    plt.plot([t0 + i*h for i in range(0,N+1)], x_arr, linewidth=1, color= blue)
    plt.plot([t0 + i*h for i in range(0,N+1)], v_arr, linewidth=1, color= red)
    plt.plot([t0 + i*h for i in range(0,N+1)], vp_arr, linewidth=1, color= cyan)
    # plt.plot(x_arr, v_arr, red)


    

# Stoermer(100, func)
rk4Int(800, kernel)
plt.legend(("x", "v"),loc='upper right')
# plt.hlines(0, 0, tf, 'k', 'dashed')
plt.margins(x=0)
# plt.legend("x", "v")
plt.title("SHO")
plt.xlabel("t")
plt.ylabel("x,v")
plt.show()