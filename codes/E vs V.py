# Importing packages:
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Importing the data file:
data = np.loadtxt("EV.txt", skiprows = 0,delimiter= " ")
print("shape of data:",data.shape)

# Figuring out the axis values:
ener = data[:,1]
vol = data[:,0]**3

# The fitting equation:
def E(v, eo, ko, ko_prime, vo):
    return eo + vo*ko*((1/(ko_prime*(ko_prime - 1)))*(v/vo)**(1- ko_prime) + v/(ko_prime*vo)-1/(ko_prime-1))

# Fitting the curve:
fit = curve_fit(E, vol, ener, bounds= ([-100,0,1,0],[100,100,100,100]))

# Extracting out the parameters:
parameter = fit[0]

# Printing the parameter for the best fit curve:
print(parameter)

# Designing the graph for fitting:
vol_list = []
ener_list = []
vol_list = np.linspace(vol, 45,100,100)
ener_list = E(vol_list, parameter[0], parameter[1],parameter[2], parameter[3])
plt.title("E versus V")
plt.xlabel("Volume"r'$\longrightarrow$')
plt.ylabel("Energy"r'$\longrightarrow$')
plt.grid()
plt.scatter(vol, ener, color = 'r', label = "Points") 
plt.plot(vol_list, ener_list, color = "cyan")
plt.legend()
plt.show()

# The P vs V equation:
def P(v, ko, ko_prime, vo): 
    return (ko/ko_prime)*((v/vo)**(-ko_prime)-1)

# Designing the final graph (P vs V):
vollist = []
vollist = np.linspace(vol, 5,50,100)
pressure_list = P(vollist, parameter[1], parameter[2], parameter[3])
plt.title("P versus V")
plt.xlabel("Volume"r'$\longrightarrow$')
plt.ylabel("Pressure"r'$\longrightarrow$')
plt.grid()
plt.plot(vollist, pressure_list, color = "r")
plt.show()