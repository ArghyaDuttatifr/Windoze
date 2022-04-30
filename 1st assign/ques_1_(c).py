#question 1 (c)
#all packages
import math  as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#given values

a = 0.5
A= [0.5, 0.9, 1.07, 1.1]
w = 0.2/0.3
#function

def func_1(u,t ):
    return ( u[1], - m.sin(u[0]) - a*u[1] + A[l]* m.cos(w*t))
u0 = [1.09, -0.1]
t = np.linspace(0, 100, 2000)
 
#excecution 
fig, axs = plt.subplots(2, 2, constrained_layout=True)

#for the 1 st value of A

ax = axs[0,0]
l=0
oscillation = odeint(func_1, u0, t)
ax.plot( oscillation[:,0], oscillation[:,1] , lw = 1)
ax.xaxis.set_label_position('top')
ax.set_xlabel(r'$\theta$')
ax.set_ylabel('velocity (v)')
ax.grid()
ax.set_title('phase space diagram for A='+str(A[l]))

#for the 2 nd value of A

ax = axs[0,1]
l=1
oscillation = odeint(func_1, u0, t)
ax.plot( oscillation[:,0], oscillation[:,1] , 'b', lw = 1)
ax.xaxis.set_label_position('top')
ax.set_xlabel(r'$\theta$')
ax.grid()
ax.set_ylabel( 'velocity')
ax.set_title('phase space diagram for A='+str(A[l]))

#for the 3 rd value of A

ax = axs[1,0]
l=2
oscillation = odeint(func_1, u0, t)
ax.plot( oscillation[:,0], oscillation[:,1], 'r' , lw = 1)
ax.xaxis.set_label_position('top')
ax.set_xlabel(r'$\theta$')
ax.grid()
ax.set_ylabel('velocity (v)')
ax.set_title('phase space diagram for A='+str(A[l]))

##for the 4-th value of A

ax = axs[1,1]
l=3
oscillation = odeint(func_1, u0, t)
ax.plot( oscillation[:,0], oscillation[:,1], 'g' , lw = 1)
ax.xaxis.set_label_position('top')
ax.set_xlabel(r'$\theta$')
plt.grid()
ax.set_ylabel( 'velocity')
ax.set_title('for A='+str(A[l]))
plt.title(' phase space diagram for A='+str(A[l]))

plt.show()
