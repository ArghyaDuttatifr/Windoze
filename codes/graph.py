import numpy as np
import matplotlib.pyplot as plt

data_fcc_loc = np.loadtxt("fcc_local_Si.txt", skiprows = 0,delimiter= " ")
import numpy as np
import matplotlib.pyplot as plt

data_fcc_loc = np.loadtxt("fcc_local_Si.txt", skiprows = 0,delimiter= " ")
data_fcc = np.loadtxt("fcc_global_Si.txt", skiprows = 0,delimiter= " ")
data_simple =  np.loadtxt("simple_global_Si.txt", skiprows = 0,delimiter= " ")
data_simple_local = np.loadtxt("simple_local_Si.txt", skiprows = 0,delimiter= " ")
data_diamond =  np.loadtxt("diamond_global_Si.txt", skiprows = 0,delimiter= " ")

ener_fcc = data_fcc[:,1]
a_fcc = data_fcc[:,0]**3
ener_simple = data_simple[:,1]
a_simple = data_simple[:,0]**3
ener_dia = data_diamond[:,1]/2
a_dia = data_diamond[:,0]**3

#Plotting
plt.grid()
plt.title("Energy versus Volume")
plt.xlabel("V")
plt.ylabel("E")
plt.scatter(a_fcc, ener_fcc, color='r', label = "fcc")
plt.scatter(a_simple, ener_simple, color='g', label = "simple")
plt.scatter(3.9**3, -4.8386015, color = "black")#fcc
plt.scatter(5.47**3, -10.820939/2, color = "black")#diamond
plt.scatter(2.54**3, -5.0665763, color = "black")#simple
plt.scatter(a_dia, ener_dia, color='b', label = "diamond")
plt.legend()
plt.show() 
