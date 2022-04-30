#%%
import matplotlib.pyplot as plt

e=1.0
l=1.0
c=0.6
r=0.5


t=0.0
i=0.0
q=0.0
tf=30.0 # final value of t
dt=0.01 # step length
tt=[]
ii=[]
qq=[]

def f1(q,i,t):
    return i # dq/dt=i ..> f1(q,i,t)
def f2(q,i,t):
    return (e-i*r-q/c)/l # di/dt=(e-ri-q/c)/l ..> f2(q,i,t)

while t<=tf: 
    
    tt.append(t)
    qq.append(q)
    ii.append(i)
    p1=dt*f1(q,i,t) # dq at initial point
    p2=dt*f2(q,i,t) # di at initial point
    q1=dt*f1(q+0.5*p1,i+0.5*p2,t+0.5*dt)
    q2=dt*f2(q+0.5*p1,i+0.5*p2,t+0.5*dt)
    r1=dt*f1(q+0.5*q1,i+0.5*q2,t+0.5*dt)
    r2=dt*f2(q+0.5*q1,i+0.5*q2,t+0.5*dt)
    s1=dt*f1(q+r1,i+r2,t+dt)
    s2=dt*f2(q+r1,i+r2,t+dt)
    q+=(p1+2*q1+2*r1+s1)/6.0
    i+=(p2+2*q2+2*r2+s2)/6.0
    t+=dt
    
plt.subplot(2,1,1)
plt.plot(tt,ii,label="Current")
plt.xlabel("time")
plt.ylabel("Current")
plt.grid()
plt.axhline (y=0, color = 'r')
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.plot(tt,qq,label="Charge")
plt.xlabel("time")
plt.ylabel("Charge")
plt.legend(loc='best')

plt.grid()
plt.suptitle("Solution of LCR circuit by RK4 method")


#%%

import matplotlib.pyplot as plt
import numpy as np
e=1.0
l=1.0
c=0.6
r=0.5


t=0.0
i=0.0
q=0.0
tf=30.0 # final value of t
dt=0.01 # step length
tt=[]
ii=[]
qq=[]
def f(Q,t): 
    q,i=Q
    f1=i
    f2=(e-i*r-q/c)/l
    return np.array([f1,f2])

def update(Q,t):
    k1=dt*f(Q,t) # dQ at initial point
    k2=dt*f(Q+0.5*k1,t+0.5*dt)
    k3=dt*f(Q+0.5*k2,t+0.5*dt)
    k4=dt*f(Q+k3,t+dt)
    return Q+1/6.0*(k1+2*k2+2*k3+k4),t+dt
Q=np.array([q,i])
while t<=tf:
    tt.append(t)
    qq.append(Q[0])
    ii.append(Q[1])
    Q,t=update(Q,t)
plt.subplot(2,1,1)
plt.plot(tt,ii,label="Current")
plt.xlabel("time")
plt.ylabel("Current")
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.plot(tt,qq,label="Charge")
plt.xlabel("time")
plt.ylabel("Charge")
plt.legend(loc='best')
plt.suptitle("Solution of LCR circuit by RK4")

