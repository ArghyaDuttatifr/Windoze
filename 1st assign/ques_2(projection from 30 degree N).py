#question 2 for 30 deg. N

import numpy as np
import math as m
from scipy.integrate import solve_ivp
#all constants in SI unit
from scipy.constants import pi , G 
R = 6.378e6
M = 5.92e24
V= 80000.0/36.0
omega = 2.272e-5

def func(t, var):
    x, y, z, vx, vy ,vz = var
    r= np.sqrt((x**2+y**2+z**2))
    dvdt=[]
    dvdt.append( vx)
    dvdt.append( vy) 
    dvdt.append( vz)
    dvdt.append( -G*M*x/r**3 +2*omega*vy+ x*omega**2 )
    dvdt.append( -G*M*y/r**3 -2*omega*vx+ y*omega**2 )
    dvdt.append( -G*M*z/r**3)
    return dvdt

psi=(pi/180.0)*45         #the initial angle for launch with the horizontal (in rad)
theta=(pi/180.0)*60        # Polar angle is equal to (90-latitude) (in rad)
phi=(pi/180.0)*77             # Azimuthal angle / the longitude (in rad)

y0=[] 
     # Now store the initial values of x, y, z, vx, vy, vz           
     #change polar coordinates to cartesian coordinates(X, Y, Z)
y0.append( R*np.sin(theta)*np.cos(phi))
y0.append( R*np.sin(theta)*np.sin(phi))
y0.append( R*np.cos(theta))
     #velocity in spherical polar , vx, vy, vz
y0.append( V*(np.sin(psi)*np.sin(theta)*np.cos(phi)+ np.cos(psi)*np.sin(phi)))
y0.append( V*(np.sin(psi)*np.sin(theta)*np.sin(phi)-np.cos(psi)*np.cos(phi)))
y0.append( V*np.cos(theta)*np.sin(psi))

def final_val(t, var):                #the evevt to track
    return ((( var[1]**2+var[0]**2+var[2]**2 )**0.5) - R)
final_val.terminal = True
final_val.direction = -1

sol = solve_ivp(func,[0,500], y0 , events = final_val, dense_output=True)    #take help from scipy ivp package 
print('The missle hit the ground after\n', sol.t_events[0][0] ,'seconds')
print('final coordinates and velocities\n', sol.y_events[0][0])
x_f =sol.y_events[0][0][0]
y_f =sol.y_events[0][0][1]
z_f =sol.y_events[0][0][2]
r_f = m.sqrt(x_f**2+y_f**2+z_f**2)
Theta_final = m.acos(z_f/r_f)
phi_final =  m.atan(y_f/x_f)

latitude_final= 90-Theta_final*180/pi
longitude_final=phi_final*180/pi
print ('Final value of radius is',r_f ,'km; as expected')
print("The missile will hit the ground at", latitude_final,"degree N", longitude_final,"degree E, after", sol.t_events[0][0], 'seconds')
