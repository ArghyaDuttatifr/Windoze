#%%question 1 (a)

'''Take the rigid pendulum,
d2θ/dt2 = − sin θ − α dθ/dt + A cos ωt .
a) Explore the phase diagram for the non-driven system, A=0.
 Take α = 0.5 and ω = 23
. Start from the initial position
θ(0), v(0) = dθ
dt(0) ≡ (1.1, −0.1).'''
from scipy.fftpack import fft, ifft
from scipy import fftpack

import math  as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 0.3 #given , the damping term
#A= [0.5, 0.9, 1.07, 1.5] .... here A = 0
w = 1/3 # frequency of ext. force 
def func(u,t ):
    return ( u[1], - m.sin(u[0]) - a*u[1] ) # + A[1]* m.cos(w*t)
# 
u0 = [1.1, -0.1]
t = np.linspace(0, 35, 2000)
oscillation = odeint(func, u0, t)


r = oscillation[:,0]
v_r = oscillation[:,1]

X = fft(r)
X_mag = np.abs(X)/2000
f_p = t[0: 1001]
X_mag_p = 2 * X_mag[0:1001]

'''

freq = fftpack.fftfreq(2000)
mask = freq>0
fft_t = 2.0 * np.abs(fft(r)/2000)
''' 

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)
ax = axs[0]
ax.plot(t, r , 'g' , label = ' time vs r' , lw = 2)
ax.set_title('t vs r')
ax.grid()
ax.axhline(alpha =0.2)
ax.legend()



ax = axs[1]
ax.plot(f_p, X_mag_p , '.-')
#ax.plot(freq[mask], fft_t[mask])

plt.show()






