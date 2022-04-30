# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 23:38:26 2022

@author: arghy
"""

#forced oscillation
import math  as m
from numpy import arange
import matplotlib.pyplot as plt

# y' = u
# u' = -y

def F(y, u, t):    # u = dy/dt
    return -2*y-0.5*u - m.sin(t)   #consider 2nd term in resistive force 

a = 1
b = 150.0                 #initial and final points
N =2000
h = (b-a)/N

tpoints = arange(a,b,h)   # it is time here
ypoints = []              
upoints = []              
                        #initial conditions
y = 1
u = 0

for t in tpoints:
    
    ypoints.append(y)
    upoints.append(u)
    
    m1 = h*u
    k1 = h*F(y, u, t)                #(x, v, t)

    m2 = h*(u + 0.5*k1)
    k2 = h*F(y+0.5*m1, u+0.5*k1, t+0.5*h)

    m3 = h*(u + 0.5*k2)
    k3 = h*F(y+0.5*m2, u+0.5*k2, t+0.5*h)

    m4 = h*(u + k3)
    k4 = h*F(y+m3, u+k3, t+h)

    y += (m1 + 2*m2 + 2*m3 + m4)/6
    u += (k1 + 2*k2 + 2*k3 + k4)/6

plt.grid(True)
plt.title(' phase space')
plt.xlabel('X', size='15')
plt.ylabel('P', size='15')
plt.plot(ypoints, upoints, 'r', label = 'oscillation curve', lw=0.5)
plt.legend()
plt.show()