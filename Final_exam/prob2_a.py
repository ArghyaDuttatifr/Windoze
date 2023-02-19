import math as m
import numpy as np
def func(r,x):
    return m.sqrt(r**2-x**2)
def simpson (n,r):
    xi=-r
    xf=r
    h=(xf-xi)/n
    integration=func(r,xi)+func(r,xf)
    for i in range(1,n):
        k=xi+i*h
        if(i%2==0):
            integration+=func(r,k)*2
        else:
            integration+=func(r,k)*4
    integration=integration*h/3
    return integration

print("The area of the circle with radius 10 is given by: ",2*simpson(1000,10))
    
