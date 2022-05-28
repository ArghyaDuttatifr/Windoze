#Question 3
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

#given values
D = 3
M = 450 #mass
g = 9.8
h = 1e-3 #smallest scale
t0 = 0
#define RK4 Method
def rk4(xn, yn, h, func):
    k1= func(yn, xn)
    k2 = func( yn+(h/2)*k1 , xn+ h/2 )
    k3 = func( yn+(h/2)*k2 , xn+ h/2 )
    k4 = func( yn+ h*k3 , xn+h )
    return yn +(h/6)*(k1+ 2*(k2+k3) +k4)
    
def vprime(u, t):    # u = [x, vx, y, vy]  , vprime is basically du/dt
    xnew = u[1]
    vx = -(D/M)*u[1]* np.sqrt(u[1]*u[1] + u[3]*u[3])
    ynew = u[3]
    vy = -g -(D/M)*u[3]* np.sqrt(u[1]*u[1] + u[3]*u[3])        
    return np.array([xnew, vx, ynew , vy ])


# Integration routine
def function(theta ,yf, v, t0, xf, h):
    u = [0, v*np.cos(theta) , 0, v* np.sin(theta)]
    # let's start the iteration loop
    i = 0  
    while True:
        u = rk4(t0 + i*h, u, h, vprime)

        if (u[0] > xf): break
        i += 1
    return u[2]-yf

theta = np.pi/180 * 34
v = 71*1000/3600    #in meter / sec
xf = np.sqrt (22**2 + 3.36**2)
yf = 2.14
theta_f = newton (function, theta , args= (yf, v, t0, xf, h))  #Finding the roots

print ('The value of angle  = ', theta_f * 180/np.pi, 'degrees')
'''Part B '''
velocity=np.linspace(70*1000/3600,80*1000/3600, 20)
thetas=np.zeros(len(velocity))
for i in range(len(velocity)) :
    thetas[i]=newton (function, theta , args= (yf, velocity[i], t0, xf, h))
#print(thetas*180/np.pi)
#plot
plt.plot(velocity,thetas,  linewidth=1, color='r')
plt.grid()
plt.ylabel('\u03B8(in Radian )')
plt.title('Variation oh angle with velocity')
plt.xlabel('Velocity(m/s)')
plt.show()



