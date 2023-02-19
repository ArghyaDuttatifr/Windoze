import math as m
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return m.exp(x)
def I_right(a,b,n):
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    f=np.exp(x)
    Integration=h*sum(f[1::])
    return Integration
def I_left(a,b,n):
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    f=np.exp(x)
    Integration=h*sum(f[:n])
    return Integration
def I_mid(a,b,n):
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    Integration=h*sum(np.exp((x[:n]+x[1:])/2))
    return Integration
def trapezoidal(a,b,n):
    h=(b-a)/n
    Integration=func(a)+func(b)
    for i in range (1,n):
        k=a+i*h
        Integration+=2*func(k)
    Integration=Integration*h/2
    return Integration
def simpson(a,b,n):
    h=(b-a)/n
    Integration=func(a)+func(b)
    for i in range (1,n):
        k=a+i*h
        if i%2==0:
            Integration+=2*func(k)
        else:
            Integration+=4*func(k)
    Integration=Integration*h/3
    return Integration    
N=int(input("Enter the number of iterations : "))
x=[]
xsimpson=[]
rightpoint=[]
leftpoint=[]
midpoint=[]
trapezoidal1=[]
simpson1=[]
for i in range (1,(N+1)):
    x.append(i)
    rightpoint.append(abs(I_right(0,1,i+1)-I_right(0,1,i)))
    leftpoint.append(abs(I_left(0,1,i+1)-I_left(0,1,i)))
    midpoint.append(abs(I_mid(0,1,i+1)-I_mid(0,1,i)))
    trapezoidal1.append(abs(trapezoidal(0,1,i+1)-trapezoidal(0,1,i)))
    if i%2==0:
        simpson1.append(abs(simpson(0,1,i+2)-simpson(0,1,i)))
        xsimpson.append(i)
plt.plot(x,rightpoint,label="Right_point Rule")
plt.plot(x,leftpoint,label="Left_point Rule")
plt.plot(x,midpoint,label="Mid_point Rule")
plt.plot(x,trapezoidal1,label="Trapezoidal Rule")
plt.plot(xsimpson,simpson1,label="Simpson Rule")
plt.yscale("log")
plt.xlabel("Number of points")
plt.ylabel("Absolute Error")
plt.title("Comparison of Error in Different Integration Algorithms")
plt.legend()
plt.show()

