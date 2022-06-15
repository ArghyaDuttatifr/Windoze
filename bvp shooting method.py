import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#y"+3y+3x = 0

x = np.linspace(0, 2 * np.pi, 200)

def equations(x, y):
    yprime = np.zeros(2)
    
    yprime[0] =  y[1]
    yprime[1] = -3 * y[0] -3*x
    
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
plt.show()
'''
#%% shoot the y vlaue according to the solution

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#y"+3y+3x = 0  , with y(0)= 7  , y(2 np.pi)=0

x = np.linspace(0, 2.0*np.pi, 200)

def equations(x, y):
    yprime = np.zeros(2)
    
    yprime[0] =  y[1]
    yprime[1] = -3 * y[0] -3*x
    
    return yprime


xspan = (x[0], x[-1])
    
    #  Use the midpoint between high and low as our guess

    
    #  Set the initial condition vector to be passed into the solver
y0 = [7, -12]

    # Solve the system using our guess
sol = solve_ivp(equations, xspan, y0, t_eval = x)

    #  For ease of use, extract the function values from the solution object.
y_num = sol.y[0, :]


    #print(count, y_num[-1])
    
#  Plot the solution and compare it to the analytical form defined above

plt.plot(x, y_num, label='Numeric')   #'.b'
plt.plot([0, 2*np.pi], [7,0], 'bo')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

'''

