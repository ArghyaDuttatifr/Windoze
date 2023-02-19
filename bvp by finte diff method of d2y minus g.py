# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:28:21 2022

@author: arghy
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi , 201)
n = 200
h = (2* np.pi-0) / n

# Get A
A = np.zeros((n+1, n+1))
A[0, 0] = 1
A[n, n] = 1
for i in range(1, n):
    A[i, i-1] = 1
    A[i, i] = -2 + 3* h**2
    A[i, i+1] = 1

print(A)

# Get b
b = np.zeros(n+1)
b[-1] = 0
b[0]= 7
print(b)

# solve the linear equations
y = np.linalg.solve(A, b)



plt.figure(figsize=(10,5))
plt.plot(t, y)
plt.plot([0, 2*np.pi], [7,0], 'bo')
#plt.plot(5, 50, 'ro')
plt.xlabel('time (s)')
plt.ylabel('altitude (m)')
plt.grid()
plt.show()


#%%


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#y"+3y+3x = 0

x = np.linspace(0, 2 * np.pi, 200)

def equations(x, y):
    yprime = np.zeros(2)
    
    yprime[0] =  y[1]
    yprime[1] = -3 * y[0] 
    
    return yprime

tol = 1e-7
max_iters = 200
low = -50
high = 20
count = 0
while count <= max_iters:
    count = count + 1
    xspan = (x[0], x[-1])
    
    #  Use the midpoint between high and low as our guess
    yprime0 = np.mean([low, high])
    
    #  Set the initial condition vector to be passed into the solver
    y0 = [7, yprime0 ]

    # Solve the system using our guess
    sol = solve_ivp(equations, xspan, y0, t_eval = x)

    #  For ease of use, extract the function values from the solution object.
    y_num = sol.y[0, :]

    #  Check to see if we within our desire tolerance
    if np.abs(y_num[-1]) <= tol:
        break
    
    #  Adjust our bounds if we are not within tolerance
    if y_num[-1] < 0:
        high = yprime0
    else:
        low = yprime0
        
    #print(count, y_num[-1])
    
#  Plot the solution and compare it to the analytical form defined above

plt.plot(x, y_num, label='Numeric')   #'.b'
plt.plot([0, 2*np.pi], [7,0], 'bo')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# %%
