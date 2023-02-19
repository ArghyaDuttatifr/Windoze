import matplotlib.pyplot as plt
import math as m
def func(x):
    return m.sin(m.cos(m.exp(x)))
def diff(x):
    return m.cos(m.cos(m.exp(x)))*(-m.sin(m.exp(x)))*m.exp(x)
def bisection(a,b,i):
    r=(a+b)/2
    a1=a
    b1=b
    for k in range (i): 
        if (func(a1)*func(r)>0):
           a1=r
        else:
            b1=r
        r=(a1+b1)/2
    return r

def newton(i,x0):
    r=x0
    for j in range (i):
        r+=-func(j)/diff(j)
    return r
x1=[]
y1=[]
y2=[]
iterations=int(input("Enter the number of iterations: "))
for n in range (1,iterations):
    x1.append(n)
    y1.append(abs(bisection(-1,1,n)-bisection(-1,1,(n-1))))
    y2.append(abs(newton(n,-1)-newton((n-1),-1)))
plt.plot(x1,y1,label="Error in bisection method")
plt.plot(x1,y2,label="Error in Newton-Raphson")
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.legend()
plt.yscale("log")
plt.show()
