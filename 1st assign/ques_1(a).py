#%%question 1 (a)


import math  as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 0.5 #given , the damping term
#A= [0.5, 0.9, 1.07, 1.5] .... here A = 0
w = 2/3 # frequency of ext. force 
def func(u,t ):
    return ( u[1], - m.sin(u[0]) - a*u[1] ) # + A[1]* m.cos(w*t)
# 
u0 = [1.1, -0.1]
t = np.linspace(0, 100, 2000)
oscillation = odeint(func, u0, t)

plt.xlabel('position' r'($\theta$) ', size='12')
plt.ylabel('velocity (v)', size='12')
r = oscillation[:,0]
v_r = oscillation[:,1]
plt.plot (r , v_r , 'g' , label = ' Phase space curve' , lw = 2)
plt.axhline()
plt.axvline()
plt.legend()
plt.grid()
plt.show()
