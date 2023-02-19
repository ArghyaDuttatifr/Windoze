# Importing packages:
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Making the data file more readable:
with open(r"C:\Users\Priyanka\Downloads\OUTCAR.txt",'r') as inp, open(r"C:\Users\Priyanka\Downloads\energies.txt",'w+') as out :
    copy=False
    for line in inp :
        if "k-point   131" in line : # upto 10 points after gamma point
            break
        if "k-point   110" in line : # from 10 points before gamma point
            copy=True
        if copy and "k-point" in line :
            out.write(line.strip().split()[1]+'\t'+line.strip().split()[3]+'\t'+line.strip().split()[4]+'\t'+line.strip().split()[5]+'\t')
        if line.strip().split()!=[] :
            if copy and line.strip().split()[0]=='28' :
                out.write(str(line.strip().split()[1])+'\t')
            if copy and line.strip().split()[0]=='29' :
                out.write(str(line.strip().split()[1])+'\n')

# Importing the required new data file which is just created:
x=np.loadtxt(r"C:\Users\Priyanka\Downloads\energies.txt")

# Defining the function for fitting:
def func(gamma,my,mz,a):
    kx=gamma[:,0]
    ky=gamma[:,1]
    kz=gamma[:,2]
    return a+ my*(ky**2+kx**2)+mz*kz**2

c = int(input("Enter 1 for effective mass of holes and 2 for effective mass of the electrons: "))+3
E = x[:, c]
k = x[:, 1:4]

# Fitting the graph:
param, cov= opt.curve_fit(func, k, E,(24, 10, -5))
con=15.2436 # unit convertion factor
print("In plane Effective mass: ", con/abs(param[0]))
print("Out of plane Effective mass: ", con/abs(param[1]))

#plt.plot(k,E)
#plt.show()

#'''Output:
#================ RESTART: C:\Users\Priyanka\Downloads\eff_mass.py ===============
#Enter 1 for effective mass of holes and 2 for effective mass of the electrons: 1
#In plane Effective mass:  0.48307561432797347
#Out of plane Effective mass:  1.0013499749878139
#>>> 
#================ RESTART: C:\Users\Priyanka\Downloads\eff_mass.py ===============
#Enter 1 for effective mass of holes and 2 for effective mass of the electrons: 2
#In plane Effective mass:  0.26961083677742614
#Out of plane Effective mass:  0.8993997746845827
#>>> 
#'''


