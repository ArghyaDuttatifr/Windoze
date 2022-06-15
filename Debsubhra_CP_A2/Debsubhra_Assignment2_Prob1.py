#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import math as mt
get_ipython().run_line_magic('matplotlib', 'notebook')

def vel_mag(vx,vy,vz,v0):
    return np.sqrt(vx**2+vy**2+vz**2)-v0

def dx_vel_mag(vx,vy,vz):
    return vx/(np.sqrt(vx**2+vy**2+vz**2))

def dy_vel_mag(vx,vy,vz):
    return vy/(np.sqrt(vx**2+vy**2+vz**2))

def dz_vel_mag(vx,vy,vz):
    return vz/(np.sqrt(vx**2+vy**2+vz**2))

def func(t,beta):
    x,y,z,vx,vy,vz=beta
    v=np.sqrt(vx**2+vy**2+vz**2)
    dbetadt=[]
    dbetadt.append(vx)
    dbetadt.append(vy)
    dbetadt.append(vz)
    dbetadt.append(-D*v*vx/m)
    dbetadt.append(-D*v*vy/m)
    dbetadt.append(-(D*v*vz/m)-g)
    return dbetadt
def hit_net(t,beta):
    return beta[0]-22
hit_net.terminal=True
hit_net.direction=1

def yz_net(vx,vy,vz):
    beta_initial=[0,0,0,vx,vy,vz]
    sol=solve_ivp(func,[0,60],beta_initial, method='RK45', events=hit_net, dense_output=True)
    return np.array([sol.y_events[0][0][1],sol.y_events[0][0][2]])
def der_yz_net(vx,vy,vz):
    der=[0,0,0]
    a=yz_net(vx+h,vy,vz)
    der[0]=(yz_net(vx+h,vy,vz)-a)/h
    der[1]=(yz_net(vx,vy+h,vz)-a)/h
    der[2]=(yz_net(vx,vy,vz+h)-a)/h
    return der

v0_vals=(5./18.)*np.linspace(70,85,100)
dist=np.sqrt(22**2+3.36**2+2.14**2)
D=3.
g=9.8
m=450.
ep=1e-9
h=1e-9
theta=[]
phi=[]
for alpha in v0_vals:
   Vel_vec=(alpha/dist)*np.array([22,3.36,2.14])
   vx_step,vy_step,vz_step=Vel_vec
   b=[vel_mag(vx_step,vy_step,vz_step,alpha),yz_net(vx_step,vy_step,vz_step)[0]-3.36,yz_net(vx_step,vy_step,vz_step)[1]-2.14]
   while((abs(b[0])>ep) or (abs(b[1])>ep) or (abs(b[2])>ep)):
      Z=der_yz_net(vx_step,vy_step,vz_step)
      A=np.array([[dx_vel_mag(vx_step,vy_step,vz_step),dz_vel_mag(vx_step,vy_step,vz_step),dz_vel_mag(vx_step,vy_step,vz_step)],[Z[0][0],Z[1][0],Z[2][0]],[Z[0][1],Z[1][1],Z[2][1]]])
      inv_A=np.linalg.inv(A)
      delta_V=-np.matmul(inv_A,b)
      Vel_vec=Vel_vec+delta_V
      vx_step,vy_step,vz_step=Vel_vec
      b=[vel_mag(vx_step,vy_step,vz_step,alpha),yz_net(vx_step,vy_step,vz_step)[0]-3.36,yz_net(vx_step,vy_step,vz_step)[1]-2.14]
   theta.append(mt.asin(vz_step/alpha)*(180/mt.pi))
   phi.append(mt.atan(vy_step/vx_step)*(180/mt.pi))
font = {'family': 'cursive',
        'color':  'k',
        'weight': 'bold',
        'size': 13,
        }   
plt.plot((18./5.)*(v0_vals),theta)
plt.xlabel("V in (km/hr)",fontdict=font)
plt.ylabel("Angle with Horizontal (in degrees)",fontdict=font)
plt.xticks([70,75,80,85],size=15)
plt.yticks([20,22,24,26],size=15)
plt.tight_layout()
plt.show()
print("When the magnitude of starting velocity is 70 km/hr, the angle with the horizontal (in degrees) would be: ",theta[0])
print("\n When the magnitude of starting velocity is 85 km/hr, the angle with the horizontal (in degrees) would be: ",theta[-1])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




