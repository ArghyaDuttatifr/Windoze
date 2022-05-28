
#%%

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import math as mt

R=mt.sqrt(22**2+3.36**2+2.14**2) #Distance covered by the shot
D=3
g=9.8
m=450
h=k=10**-8  #Allowed range of Error


def Eq_M(t,H):  # Defining D equation of motion
    x=H[0]
    y=H[1]
    z=H[2]
    vx=H[3]
    vy=H[4]
    vz=H[5]
    dHdt=[]
    dHdt.append(vx)
    dHdt.append(vy)
    dHdt.append(vz)
    dHdt.append(-(D/m)*np.sqrt(vx**2+vy**2+vz**2)*vx)
    dHdt.append(-(D/m)*np.sqrt(vx**2+vy**2+vz**2)*vy)
    dHdt.append(-((D/m)*np.sqrt(vx**2+vy**2+vz**2)*vz)-g)
    return dHdt


def goal_line(t, H):    # Defining Goal-lines
    return H[0]-22
goal_line.terminal=True
goal_line.direction=1



def Solve(vx,vy,vz):    #Solving Function
    H_initial=[0,0,0,vx,vy,vz]
    sol=solve_ivp(Eq_M,[0,50],H_initial, method='RK45', events=goal_line, dense_output=True)
    return np.array([sol.y_events[0][0][1],sol.y_events[0][0][2]])

def Variation(vx,vy,vz):  #Varying velocity to optimise
    V=[0,0,0]
    a=Solve(vx,vy,vz)
    V[0]=(Solve(vx+h,vy,vz)-a)/h
    V[1]=(Solve(vx,vy+h,vz)-a)/h
    V[2]=(Solve(vx,vy,vz+h)-a)/h
    return V

def v_mag(vx,vy,vz,v0):
    return np.sqrt(vx**2+vy**2+vz**2)-v0

def x_vel(vx,vy,vz):
    return vx/(np.sqrt(vx**2+vy**2+vz**2))

def y_vel(vx,vy,vz):
    return vy/(np.sqrt(vx**2+vy**2+vz**2))

def z_vel(vx,vy,vz):
    return vz/(np.sqrt(vx**2+vy**2+vz**2))


v0_vals=(5./18.)*np.linspace(70,85,75)  #Initial Velocity variation 

theta=[]
phi=[]


for alpha in v0_vals:
   Vel_vec=(alpha/R)*np.array([22,3.36,2.14])
   vx_step,vy_step,vz_step=Vel_vec
   b=[v_mag(vx_step,vy_step,vz_step,alpha),Solve(vx_step,vy_step,vz_step)[0]-3.36,Solve(vx_step,vy_step,vz_step)[1]-2.14]
   while((abs(b[0])>k) or (abs(b[1])>k) or (abs(b[2])>k)):  # Optimising the values upto our error range
      Z=Variation(vx_step,vy_step,vz_step)
      A=np.array([[x_vel(vx_step,vy_step,vz_step),z_vel(vx_step,vy_step,vz_step),z_vel(vx_step,vy_step,vz_step)],[Z[0][0],Z[1][0],Z[2][0]],[Z[0][1],Z[1][1],Z[2][1]]])
      inv_A=np.linalg.inv(A)
      delta_V=-np.matmul(inv_A,b)
      Vel_vec=Vel_vec+delta_V
      vx_step,vy_step,vz_step=Vel_vec
      b=[v_mag(vx_step,vy_step,vz_step,alpha),Solve(vx_step,vy_step,vz_step)[0]-3.36,Solve(vx_step,vy_step,vz_step)[1]-2.14]
   theta.append(mt.asin(vz_step/alpha)*(180/mt.pi))     #Determination of the angles
   phi.append(mt.atan(vy_step/vx_step)*(180/mt.pi))

#Plotting

plt.plot((18./5.)*v0_vals,theta)
plt.xlabel("Initial Velocity")
plt.ylabel("Angle with Horizontal") 
plt.xticks([70,75,80,85])
plt.show()

plt.plot((18./5)*v0_vals,phi)
plt.xlabel("Initial Velocity")
plt.ylabel("Azimuthal Angle") 
plt.xticks([70,75,80,85])
plt.show()

print("When Initial velocity is 70 km/hr, the horizontal angle would be ",theta[0],"Azimuthal Angle would be",phi[0])
print("When Initial velocity is 85 km/hr, the horizontal angle would be ",theta[-1],"Azimuthal Angle would be",phi[-1])




#%%



