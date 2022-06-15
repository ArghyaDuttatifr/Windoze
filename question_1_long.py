from scipy.optimize import leastsq
import numpy as np

vols = np.array([27, 29.791, 32.768, 35.937, 39.304])

energies = np.array([-0.7022, -1.9711, -2.917,-3.6087, 4.1008 ])

def Murnaghan(parameters, vol):
    E0, B0, BP, V0 = parameters

    E = E0 + B0 * vol / BP * (((V0 / vol)**BP) / (BP - 1) + 1) - V0 * B0 / (BP - 1.0)

    return E

def objective(pars, y, x):
    #we will minimize this function
    err =  y - Murnaghan(pars, x)
    return err

x0 = [ -1.0, 3.5, 4,4] #initial guess of parameters

plsq = leastsq(objective, x0, args=(energies, vols))

print ('Fitted parameters = {0}'.format(plsq[0]))

import matplotlib.pyplot as plt
plt.plot(vols,energies, 'ro')

#plot the fitted curve on top
x = np.linspace(min(vols), max(vols), 50)
y = Murnaghan(plsq[0], x)
plt.plot(x, y, 'k-')
plt.xlabel('Volume')
plt.ylabel('Energy')
plt.show()