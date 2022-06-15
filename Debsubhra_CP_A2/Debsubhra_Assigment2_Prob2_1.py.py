#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse as sparse
from scipy.sparse.linalg import eigs
from scipy import constants as const
from scipy.optimize import fsolve
get_ipython().run_line_magic('matplotlib', 'notebook')

def calculate_laplace_three_point(r):
    h=r[1]-r[0]
    main_diag=-2.0/h**2* np.ones(N)
    off_diag=+1.0/h**2 *np.ones(N-1)
    bv1_diag=np.array([1.0/h**2])
    bv2_diag=np.array([1.0/h**2])
    laplace_term=sparse.diags([main_diag, off_diag, off_diag,bv1_diag,bv2_diag],(0,-1,1,(N-1),-(N-1)))
    #laplace_term=sparse.diags([main_diag, off_diag, off_diag],(0,-1,1))
    return laplace_term

def calculate_potential_term(r):
    potential=0.5*k*r**2+(1/24)*lamda*r**4
    potential_term=sparse.diags(potential)
    return potential_term

def hamiltonian(r):
    laplace_term= calculate_laplace_three_point(r)
    potential_term= calculate_potential_term(r)
    hamiltonian = - 0.5*(laplace_term)+ potential_term
    return hamiltonian
def plot(r, densities,eigenvalues):
    plt.xlabel('X',fontdict=font)
    plt.ylabel('Probability density',fontdict=font)
    energies = ['E = {: >5.5f} '.format(eigenvalues[i].real) for i in range(6)]
    plt.plot(r , densities[0]/np.sqrt(r[1]-r[0]), color='blue',  label=energies[0])
    plt.plot(r , densities[1]/np.sqrt(r[1]-r[0]), color='green', label=energies[1])
    plt.plot(r , densities[2]/np.sqrt(r[1]-r[0]), color='cyan',  label=energies[2])
    plt.plot(r , densities[3]/np.sqrt(r[1]-r[0]), color='magenta',  label=energies[3])
    plt.plot(r , densities[4]/np.sqrt(r[1]-r[0]), color='red',  label=energies[4])
    plt.plot(r , densities[5]/np.sqrt(r[1]-r[0]), color='yellow',  label=energies[5])
    plt.legend()
    plt.xlim([-10,10])
    plt.tight_layout()
    plt.savefig("Prob2_5.png")
    plt.show()
    return
font = {'family': 'cursive',
        'color':  'k',
        'weight': 'bold',
        'size': 13,
        }
k=float(input("Enter the value of k: "))
lamda=1
N=4000
r=np.linspace(-10,10, N,endpoint=False)
hamiltonian_1=hamiltonian(r)
number_of_eigenvalues=30
eigenvalues, eigenvectors =eigs(hamiltonian_1, k=number_of_eigenvalues, which='SM')
print("The energy eigenvalues are: ", eigenvalues.real)
eigenvectors = np.array([x for _, x in sorted(zip(eigenvalues, eigenvectors.T), key=lambda pair: pair[0])])
densities = [eigenvectors.real[i, :] for i in range(len(eigenvalues))]
plot(r, densities, eigenvalues)


# In[ ]:




