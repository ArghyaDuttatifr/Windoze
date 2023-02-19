import math as m
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
def func(r,x):
    return m.sqrt(r**2-x**2)
def simpson(n,r):
    xi=-r
    xf=r
    h=(xf-xi)/n
    integration=func(r,xi)+func(r,xf)
    for i in range(1,n):
        k=xi+i*h
        if (i%2==0):
            integration+=func(r,k)*2
        else:
            integration+=func(r,k)*4
    integration=integration*h/3
    return 2*integration
x=np.linspace(5,50,10)
y=[]
yi=[]
for z in range(10):
    y.append(simpson(100,x[z]))
F=CubicSpline(x,y)
for l in range(10):
    yi.append(F(x[l]))
fig, ax=plt.subplots(1,2)
ax[0].plot(x,y,label="Curve joing the points")
ax[0].set_xlabel("Radius")
ax[0].set_ylabel("The area")
ax[1].plot(x,yi,label="Interpolated Function using CubicSpline")
ax[1].set_xlabel("Radius")
ax[1].set_ylabel("The area of the circle")

plt.legend()
plt.show()
print("The area of the circle with radius 13 is given by: ",F(13))

