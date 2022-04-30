
import numpy as np
def D2x(v, x, F, k, b):
    v, x 
    return F*np.cos(x) - k * x - b * v

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
k = 5.0


y0 = [np.pi - 0.1, 0.0]

t = np.linspace(0, 10, 101)

from scipy.integrate import odeint
sol = odeint(D2x, y0, t, args=(b, c))

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
