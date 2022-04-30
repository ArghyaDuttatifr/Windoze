# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 01:42:00 2022

@author: arghy
"""


#forced oscillation
import math  as m
from numpy import arange
import matplotlib.pyplot as plt

# y' = u
# u' = -y

def F(y, u, x):
    return -2*y-0.2*u+0.2*m.sin(x)

xi = 0
xf = 100.0                 #initial and final points
N =500
h = (xf-xi)/N


xpoints = arange(xi,xf,h)   # it is time here
ypoints = []                # it is x here
upoints = []                # it is dx/dt = v  here
         
       #initial conditions
y = 1
u = 0

for i in range (0,N):
    x = x + i*h
    
    ypoints.append(y)
    upoints.append(u)
    
    m1 = h*u
    k1 = h*F(y, u, x)                #(x, v, t)

    m2 = h*(u + 0.5*k1)
    k2 = h*F(y+0.5*m1, u+0.5*k1, x+0.5*h)

    m3 = h*(u + 0.5*k2)
    k3 = h*F(y+0.5*m2, u+0.5*k2, x+0.5*h)

    m4 = h*(u + k3)
    k4 = h*F(y+m3, u+k3, x+h)

    y += (m1 + 2*m2 + 2*m3 + m4)/6
    u += (k1 + 2*k2 + 2*k3 + k4)/6

plt.grid(True)
plt.title(' Damped hermonic oscillator')
plt.xlabel('Time (t)', size='15')
plt.axhline (y=0, color = 'r')
plt.plot(xpoints, ypoints, 'g', label = 'oscillation curve', lw=1)
plt.plot(xpoints, upoints, 'b', label = 'oscillation curve', lw=1)

plt.legend()
plt.show()