import math as m
def func(x):
    return m.sin(m.cos(m.exp(x)))
def diff(x):
    return m.cos(m.cos(m.exp(x)))*(-m.sin(m.exp(x)))*m.exp(x)
r=-1
eps=1e-7
i=0
while(abs(func(r))>eps):
    r+=-func(r)/diff(r)
    i=i+1
    print(r,"   ",func(r),"     ",diff(r))
print("The root is found to be ",r,"after ",i," interations with precision of ",eps)

