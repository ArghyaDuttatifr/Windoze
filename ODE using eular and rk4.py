# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:58:46 2022

@author: arghy
"""

import matplotlib.pyplot as plt
import numpy as np
# initial value of t, i
e=1.0
l=0.5
c=0.1
t=0.0
i=0.0
q=0.0
tt=[]
ii=[]
qq=[]
tf=20.0 # final value of t
dt=0.01 # step length
# defining function
def f1(t,i,q): 
    return i # dq/dt=i
def f2(t,i,q):
    return (e-q/c)/l # di/dt=(e-q/c)/l
while t<=tf:
    tt.append(t)
    ii.append(i)
    qq.append(q)
    p1=dt*f1(t,i,q) # dq at initial point (t)
    p2=dt*f2(t,i,q) # di at initial point (t)
    q1=dt*f1(t+dt,i+p2,q+p1) # dq at end point (t+dt)
    q2=dt*f2(t+dt,i+p2,q+p1) # di at end point (t+dt)
    q=q+0.5*(p1+q1)
    i=i+0.5*(p2+q2)
    t+=dt
plt.plot(tt,qq,label="Charge")
plt.plot(tt,ii,label="Current")
plt.xlabel("time")
plt.ylabel("Current & Charge")
plt.legend(loc='best')
plt.title("Solution of LC circuit by Modified Euler method")

#%%
e=1.0
l=1.0
c=0.5
r=0.5
############################################
#"""
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
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.plot(tt,qq,label="Charge")
plt.xlabel("time")
plt.ylabel("Charge")
plt.legend(loc='best')
plt.suptitle("Solution of LCR circuit by RK4 method:Underdamped")