
import math  as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 0.5
A= [0.5, 0.9, 1.07, 1.5]
w = 2/3
fig , axs = plt.subplots(2, 2, constrained_layout=True)
#define function for each A
def func_1(u,t ):     #function for A = 0.5
    return ( u[1] ,- m.sin(u[0]) - a*u[1] + A[0]* m.cos(w*t))
u0 = [1.1, -0.1]
t = np.linspace(0, 100, 1000)
oscillation_1 = odeint(func_1, u0, t)
#excecution
ax = axs[0]

x_1=oscillation_1[:,0]
v_1=oscillation_1[:,1]
ax.plot(x_1 , v_1  )
ax.set_title('phase space curve for A=0.5')

plt.show()
def func_2(u,t ):   #function for A = 0.9
    return ( u[1] , - m.sin(u[0]) - a*u[1] + A[1]* m.cos(w*t))
u0 = [1.1, -0.1]
t = np.linspace(0, 100, 2000)
oscillation_2 = odeint(func_2, u0, t)
#execution

ax = axs[1]


ax.plot ( oscillation_2[:,0], oscillation_2[:,1] )
ax.set_title('phase space curve for A=0.5')

def func_3(u,t ):  # function for A=1.07
    return ( u[1] , - m.sin(u[0]) - a*u[1] + A[2]* m.cos(w*t))
u0 = [1.1, -0.1]
t = np.linspace(0, 100, 2000)
oscillation_3 = odeint(func_3, u0, t)
#excecution
ax = axs[2]


ax.plot ( oscillation_3[:,0], oscillation_3[:,1] )
ax.set_title('phase space curve for A=0.5')

def func_4(u,t ):   ## function for A=1.5
    return ( u[1] , - m.sin(u[0]) - a*u[1] + A[3]* m.cos(w*t))
u0 = [1.1, -0.1]
t = np.linspace(0, 100, 2000)
oscillation_4 = odeint(func_4, u0, t)
#excecution
ax = axs[3]


ax.set_ylabel('Momentum (p)', size='8')
ax.plot ( oscillation_4[:,0], oscillation_4[:,1] )
ax.set_title('phase space curve for A=0.5')

plt.show()
