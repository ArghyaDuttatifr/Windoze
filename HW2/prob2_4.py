import numpy as np
import math as m
from scipy import integrate
def func(x):
    return m.exp(x)
a=0
b=1
n=100
x=np.linspace(a,b,n)
f=np.exp(x)
trapezoidal=np.trapz(f,x)
print("The result of the integration using np.trapz function gives : ",trapezoidal)
simpson=integrate.simpson(f,x)
print("The result of the integration using scipy.integrate.simpson function is : ", simpson)
romberg=integrate.romberg(func,0,1)
print("The result of the integration using scipy.integrate.romberg function is : ", romberg)
guass=integrate.fixed_quad(np.exp,0,1)
print("The result of the integration using scipy.integrate.fixed.quad function is : ",guass)
