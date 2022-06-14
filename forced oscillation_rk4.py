
#forced oscillation
import math  as m
from numpy import arange
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy import fftpack

alpha = 0.2
# y' = u
# u' = -y

def F(y, u, x):
    return -y +  alpha *u**2 - 0.5*u



xi = 0
xf = 50.0                 #initial and final points
N =10000
h = (xf-xi)/N


xpoints = arange(xi,xf,h)   # it is time here
ypoints = []                # it is x here
upoints = []                # it is dx/dt = v  here
         
       #initial conditions
y = 1.1
u = -0.1

for x in xpoints:
    
    ypoints.append(y)
    upoints.append(u)
    
    m1 = h*u
    k1 = h*F(y, u, x)                #(x, v, t)

    m2 = h*(u + 0.5*k1)
    k2 = h*F(y+0.5*m1, u+0.5*k1, x+0.5*h)

    m3 = h*(u + 0.5*k2)
    k3 = h*F(y+0.5*m2, u+0.5*k2, x+0.5*h)

    m4 = h*(u + k3)
    k4 = h*F(y+m3, u+k3, x+h)

    y += (m1 + 2*m2 + 2*m3 + m4)/6
    u += (k1 + 2*k2 + 2*k3 + k4)/6

plt.grid(True)
plt.title(' Damped hermonic oscillator')
plt.xlabel('Time (t)', size='15')
plt.axhline (y=0, color = 'r')
plt.plot(xpoints, ypoints, 'g', label = 'oscillation curve', lw=1)
#plt.plot(ypoints, upoints, 'b', label = 'oscillation curve', lw=1)
X = fft(ypoints)
X_mag = np.abs(X)/2000
f_p = xpoints[0: 5001]
X_mag_p = 2 * X_mag[0:5001] 
plt.plot(f_p, X_mag_p , '.-')
plt.legend()
plt.show()








'''
#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
lam=0.5
k=4.0
F=1.0
tf=100.0

def f(z,t):
    x, v = z
    f1=v
    f2= F*np.cos(w*t)-k*x-lam*v
    return np.array([f1,f2])
freq=np.linspace(0.5,4,500)
A,V=[],[]
for w in freq:
    t=0.0
    v=1.0
    x=0.0
    t=np.linspace(t,tf,500)
    z=np.array([x,v]) # packing initial values
    sol=odeint(f,z,t)
    x,v=sol[:,0],sol[0:,1] # unpacking solutions x and v
    
    
    amplitude = np.max(x[-100:])
    velocity = np.max(v[-100:])
    A.append(amplitude)
    V.append(velocity)
plt.plot(freq,A,label="Amplitude",lw=3)

plt.plot(freq[::5],V[::5], 'o',label="Velocity",lw=3)

plt.xlabel("Frequency")
plt.ylabel("Velocity")
plt.legend(loc='best')
plt.title("Amplitude & Velocity Resonance")










'''


