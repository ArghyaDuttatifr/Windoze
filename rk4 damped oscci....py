# -*-
#forced oscillation
import math  as m
from numpy import arange
import matplotlib.pyplot as plt

# y' = u
# u' = -y

def F(y, u, x):
    return -2*y-0.2*u+0.1*m.sin(x)

a = 1
b = 120.0                 #initial and final points
N =500
h = (b-a)/N

xpoints = arange(a,b,h)
ypoints = []
upoints = []
                        #initial conditions
y = 1
u = 1

for x in xpoints:
    
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
plt.plot(xpoints, ypoints, 'g', label = 'oscillation curve', lw=2)
plt.legend()
plt.show()