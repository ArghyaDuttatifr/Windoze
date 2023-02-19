import math as m
import numpy as np 
def func(x):
    return m.exp(x)
def trapezoidal (xi,xf,n):
    h=(xf-xi)/n
    integration=func(xi)+func(xf)
    for i in range (1,n):
        k=xi+i*h
        integration=integration+2*func(k)
    integration=integration*h/2
    return integration
def simpson (xi,xf,n):
    h=(xf-xi)/n
    integration=func(xi)+func(xf)
    for i in range(1,n):
        k=xi+i*h
        if i%2==0:
            integration+=2*func(k)
        else:
            integration+=4*func(k)
    integration=integration*h/3
    return integration
print("The trapezoidal rule gives using 100 points : ",trapezoidal(0,1,100))
print("The simpson rule gives using 100 points : ",simpson(0,1,99))
print("The exact answer would be : ",m.exp(1)-1)
