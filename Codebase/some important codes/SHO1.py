from math import sin
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

from colors import *
from integration import *

for x0 in np.arange(1, 1.1, 0.01):
    for v0 in np.arange(1.0, 0, 0.01):
        m = 1
        omega = 5
        d = 1
        t0 = 0
        tf = 20

        # derivative kernel
        def kernel (u, t):
            x_der = u[1]                   # dx/dt
            v_der = -m*omega*omega*u[0] - d*u[1]*u[1]   # dv/dt
            return np.array([x_der, v_der])

        def rk4Int(N, kernel):
            h = (tf-t0)/N   # step size
            un = np.array([x0, v0])   # x, v

            # iteration loop
            for i in range(0, N):
                un = rk4(t0 + i*h, un, h, kernel)
                
                if(i==0):
                    plt.plot(un[0], un[1], marker="o", markersize=2, color=green)

                if(i==100):
                    plt.plot(un[0], un[1], marker="o", markersize=2, color=red)

                if(i==200):
                    plt.plot(un[0], un[1], marker="o", markersize=2, color=blue)

                if(i==300):
                    plt.plot(un[0], un[1], marker="o", markersize=2, color=yellow)

                if(i==400):
                    plt.plot(un[0], un[1], marker="o", markersize=2, color=cyan)

                if(i==500):
                    plt.plot(un[0], un[1], marker="o", markersize=2, color=magenta)

                if(i==600):
                    plt.plot(un[0], un[1], marker="o", markersize=2, color=black)
                


            # plt.plot([t0 + i*h for i in range(0,N+1)], x_arr, linewidth=1, color= blue)
            # plt.plot([t0 + i*h for i in range(0,N+1)], v_arr, linewidth=1, color= red)
        
        rk4Int(800, kernel)
plt.margins(x=0)
plt.title("SHO")
plt.xlabel("x")
plt.ylabel("v")
plt.show()