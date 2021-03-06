'''
This script provides the solution 
for Question 2 of Assignment 2
'''

import sys
import os

# Add the Utils Module
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path.replace("Assignment2/Question2", ""))

# Python imports
import numpy as np

# Utils module imports
from Utils.colors import blue, green, red
from Utils.plt_creator import plt_creator

# Local imorts
from solver import solver


# Initial Parameters for Code
N = 1000
Nvalues = 3
lmbda = 1

# Part A

# take length scale for solution
xi = -5
xf = 5

# evaluate solutions
k = 1
eigs = solver(xi, xf, N, True, Nvalues, k, lmbda)
print("Eigenvalues for k = 1 case are:", eigs)

k = -1
eigs = solver(xi, xf, N, True, Nvalues, k, lmbda)
print("Eigenvalues for k = -1 case are:", eigs)

# Part B

# initialise L = 2*X range
X = np.linspace(1, 5, 10)

k = 1
dE1, dE2, dE3 = [], [], []
for x in X:

    # evaluate energies for two boundary conditions
    eigs2 = solver(-x, x, N, False, Nvalues, k, lmbda)
    eigs1 = solver(-x, x, N, True, Nvalues, k, lmbda)
    dE = eigs2 - eigs1

    dE1.append(dE[2])
    dE2.append(dE[1])
    dE3.append(dE[0])

# plot the result
plt1 = plt1 = plt_creator(
    title= r'$\Delta E$ vs L', 
    xLabel="L", 
    yLabel=r'$\Delta E$', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(2*X, dE1, color=blue, label=r'$\Delta E_1$')
plt1.plot(2*X, dE2, color=red, label=r'$\Delta E_2$')
plt1.plot(2*X, dE3, color=green, label=r'$\Delta E_3$')

plt1.legend()
plt1.savefig("Results/del_k_1.png")


k = -1
dE1, dE2, dE3 = [], [], []
for x in X:

    # evaluate energies for two boundary conditions
    eigs2 = solver(-x, x, N, False, Nvalues, k, lmbda)
    eigs1 = solver(-x, x, N, True, Nvalues, k, lmbda)
    dE = eigs2 - eigs1

    dE1.append(dE[2])
    dE2.append(dE[1])
    dE3.append(dE[0])

# plot the result
plt1 = plt1 = plt_creator(
    title= r'$\Delta E$ vs L', 
    xLabel="L", 
    yLabel=r'$\Delta E$', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(2*X, dE1, color=blue, label=r'$\Delta E_1$')
plt1.plot(2*X, dE2, color=red, label=r'$\Delta E_2$')
plt1.plot(2*X, dE3, color=green, label=r'$\Delta E_3$')

plt1.legend()
plt1.savefig("Results/del_k_m1.png")




    