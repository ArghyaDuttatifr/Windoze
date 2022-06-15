
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(y,t,b):
    y0, y1 = y
    dydt = [y1, y1 - b*np.sin(t)]
    return dydt

b=1
t = np.linspace(0,1,50)

def sec(f,x1,x0, iter):
    for i in range(iter):
        f1 = f(x1)
        f0 = f(x0)
        h = (x1-x0)/(f1-f0)
        x2 = x1 - f1*h
        x0, x1 = x1, x2
        print(x2)
    return x2

def funct(v):
    y00 = [0,v]
    sol = odeint(func, y00, t, args=(b,))
    # plt.plot(t,sol[:,1])
    f = sol[49:,0]
    return f


# def righ():
#     v0 = 1
#     y00 = [0,v0]
#     sol = odeint(func, y00, t, args=(b,))
#     fi = sol[49:,0]
#     vi = 5
#     sol = odeint(func, y00, t, args=(b,))
#     # fi1 = sol[49:,0]
#     # vi = sec(fi1,fi,vi,v0)
#     for i in range(0,10):
#         y00 = [0,vi]
#         sol = odeint(func, y00, t, args=(b,))
#         fi1 = sol[49:,0]
#         vf = sec(fi1,fi,vi,v0)
#         v0 = vi
#         vi = vf

root = sec(funct, -1, -10, 10)
root = 0.121375
y00 = [0,root]
sol = odeint(func, y00, t, args=(b,))

plt.plot(t,sol[:,1])
plt.show()