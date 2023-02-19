import math as m
import numpy as np
def integrand(x):
    return m.exp(x)
def I_right(a,b,n):
    h=(b-a)/(n-1)
    x=np.linspace(a,b,n)
    f=np.exp(x)
    Integration=h*sum(f[1::])
    return Integration
def I_left(a,b,n):
    h=(b-a)/(n-1)
    x=np.linspace(a,b,n)
    f=np.exp(x)
    Integration=h*sum(f[:n-1])
    return Integration
def I_mid(a,b,n):
    h=(b-a)/(n-1)
    x=np.linspace(a,b,n)
    Integration=h*sum(np.exp((x[:n-1]+x[1:])/2))
    return Integration
print("The exact answer is : ", m.exp(1)-1)
print("The right-point rule gives after 100 interations : ",I_right(0,1,100), " and the error is ",I_right(0,1,100)-m.exp(1)+1)
print("The left-point rule gives after 100 iterations : ", I_left(0,1,100), " and the error is ",I_left(0,1,100)-m.exp(1)+1)
print("The mid_point rule gives after 100 iterations : ",I_mid(0,1,100), " and the error is ",I_mid(0,1,100)-m.exp(1)+1)
       

