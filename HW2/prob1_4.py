from scipy import optimize
import math as m
def func(x):
    return m.sin(m.cos(m.exp(x)))
def diff(x):
    return m.cos(m.cos(m.exp(x)))*(-m.sin(m.exp(x)))*m.exp(x)
root1=optimize.newton(func,-1,diff)
print("The root found using scipy.optimize.newton library : ",root1)
root2=optimize.bisect(func,-1,1)
print("The root found using scipy.optimize.bisect library : ",root2)
