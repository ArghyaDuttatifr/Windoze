import matplotlib.pyplot as plt
import numpy as np

from func import func, exact
from init_val import y0, x0
from integration import *
from colors import *

plt.figure()

# Integrator func
def Integrator1(x0, y0, func, integrator, xf, N, exact):
    h = (xf - x0)/N
    yn = y0
    for i in range(0, N):
        yn = integrator(x0 + i*h, yn, h, func)

    error = abs(exact(yn, x0 + N*h) - yn)
    return error

def Integrator2(x0, y0, func, integrator, xf, N, exact):
    h = (xf - x0)/N
    y1 = rk4(x0, y0, h, func)
    y2 = rk4(x0+h, y1, h, func)
    y3 = rk4(x0+2*h, y2, h, func)
    f = [
        func(y3, x0 + 3*h),
        func(y2, x0 + 2*h),
        func(y1, x0 + h),
        func(y0, x0),
    ]
    yn = y3
    for i in range(3, N):
        yn = integrator(yn, h, f)
        f.pop(3)
        f.insert(0, func(yn, x0 + (i+1)*h))

    error = abs(exact(yn, x0 + N*h) - yn)
    return error

def Adaptive(x0, y0, func, integrator, xf, N, exact):
    eps0 = 1e-9
    eps = eps0/N
    s = 0.9
    h = (xf - x0)/N
    yn = y0
    xn = x0
    while(xn < xf):
        y1 = integrator(xn, yn, h, func)
        y2i = integrator(xn, yn, h/2, func)
        y2 = integrator(xn + h/2, y2i, h/2, func)

        delta = abs(y2 - y1)
        if (delta <= eps):
            yn = (16*y2 - y1)/15
            xn = xn + h
            h = s*h*pow((eps/delta),1/4)
        else:
            h = s*h*pow((eps/delta),1/5)
            y1 = integrator(xn, yn, h, func)
            y2i = integrator(xn, yn, h/2, func)
            y2 = integrator(xn + h/2, y2i, h/2, func)
            yn = (16*y2 - y1)/15
            xn = xn + h


    error = abs(exact(yn, xn) - yn)
    return error


def looper(x0, y0, func, integrator, Integrator, xf, exact, Ni, Nf, Nsteps, color):
    err_array = []
    for N in range(Ni, Nf, Nsteps):
        err_array.append(Integrator(x0, y0, func, integrator, xf, N, exact))
    
    plt.plot(range(Ni, Nf, Nsteps), err_array, color + "o")

looper(x0, y0, func, euler, Integrator1, 1., exact, 100, 1000, 100, red)
looper(x0, y0, func, trapezoidal_pc, Integrator1, 1., exact, 100, 1000, 100, blue)
looper(x0, y0, func, rk4, Integrator1, 1., exact, 100, 1000, 100, green)
looper(x0, y0, func, ab4, Integrator2, 1., exact, 100, 1000, 100, magenta)
looper(x0, y0, func, rk4, Adaptive, 1., exact, 100, 1000, 100, yellow)

plt.legend(("euler", "trapezoidal", "rk4", "ab4", "adaptive"),loc='upper right')
plt.yscale('log')
plt.xscale('log')
plt.title(r'$\Delta y$' + ' vs N')
plt.xlabel("N")
plt.ylabel(r'$\Delta y$')
plt.show()