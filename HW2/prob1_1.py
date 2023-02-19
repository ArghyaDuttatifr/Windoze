import math as m
def func(x):
    return m.sin(m.cos(m.exp(x)))
eps=1e-5
a=-1
b=1
r=(a+b)/2
while (abs(func(r))>eps):
    r=(a+b)/2
    if (func(r)*func(a)>0):
        a=r
    else:
        b=r
print(r)
