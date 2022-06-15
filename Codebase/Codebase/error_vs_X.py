import matplotlib.pyplot as plt
import numpy as np

from func import func, exact
from init_val import y0, x0
from integration import *
from colors import *

plt.figure()

# Integrator func
def Integrator(x0, y0, func, integrator, xf, N, exact, color):
    err_array = []
    h = (xf - x0)/N
    yn = y0
    for i in range(0, N):
        yn = integrator(x0 + i*h, yn, h, func)
        error = abs(exact(yn, x0 + (i+1)*h) - yn)
        err_array.append(error)

    
    x = np.array([x0 + i*h for i in range(1, N+1)])
    plt.plot(x, err_array, color)
    

Integrator(x0, y0, func, euler, 1., 1000, exact, red)
Integrator(x0, y0, func, trapezoidal_pc, 1., 1000, exact, blue)
Integrator(x0, y0, func, rk4, 1., 1000, exact, green)

plt.legend(("euler", "trapezoidal", "rk4"),loc='upper right')
plt.yscale('log')
plt.title(r'$\Delta y$' + ' vs x')
plt.xlabel("x")
plt.ylabel(r'$\Delta y$')
plt.show()