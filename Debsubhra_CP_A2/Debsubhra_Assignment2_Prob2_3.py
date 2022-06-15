#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
    laplace_term=sparse.diags([main_diag, off_diag, off_diag],(0,-1,1))
    return laplace_term

def calculate_potential_term(r):
    potential=0.5*k*r**2+(1/24)*lamda*r**4
    potential_term=sparse.diags(potential)
    return potential_term

def hamiltonian(r):
    laplace_term= calculate_laplace_three_point(r)
    potential_term= calculate_potential_term(r)
    hamiltonian = - (laplace_term)+ 2*potential_term
    return hamiltonian
k=1
lamda=1

def plot(r, densities,eigenvalues):
    plt.xlabel('X')
    plt.ylabel('Probability density')
    energies = ['E = {: >5.5f} '.format(eigenvalues[i].real) for i in range(2)]
    plt.plot(r , densities[0]/(r[0]-r[1]), color='blue',  label=energies[0])
    plt.plot(r , densities[1]/(r[0]-r[1]), color='green', label=energies[1])
    plt.plot(r , densities[2]/(r[0]-r[1]), color='cyan',  label=energies[0])
    plt.plot(r , densities[3]/(r[0]-r[1]), color='magenta',  label=energies[0])
    plt.plot(r , densities[4]/(r[0]-r[1]), color='red',  label=energies[0])
    plt.legend()
    plt.xlim([0,2])
    plt.show()
    return

N=4000
r=np.linspace(-10,10, N)
hamiltonian_1=hamiltonian(r)
number_of_eigenvalues=30
eigenvalues, eigenvectors =eigs(hamiltonian_1, k=number_of_eigenvalues, which='SM')
print(eigenvalues.real)
eigenvectors = np.array([x for _, x in sorted(zip(eigenvalues, eigenvectors.T), key=lambda pair: pair[0])])
densities = [np.absolute(eigenvectors[i, :])**2 for i in range(len(eigenvalues))]
#plot(r, densities, eigenvalues)
eigvals=[]
eigvals1=[]
Lsize=[]
for i in range(2,16,1):
    N=100*i
    a=2*i
    N1=2*N
    a1=2*a
    r=np.linspace(-a,a, N)
    r1=np.linspace(-a1,a1, N1)
    hamiltonian_1=hamiltonian(r)
    number_of_eigenvalues=30
    eigenvalues, eigenvectors =eigs(hamiltonian_1, k=number_of_eigenvalues, which='SM')
    eigvals.append(np.array(eigenvalues.real))
    N=N1
    hamiltonian_2=hamiltonian(r1)
    number_of_eigenvalues=30
    eigenvalues, eigenvectors =eigs(hamiltonian_2, k=number_of_eigenvalues, which='SM')
    eigvals1.append(np.array(eigenvalues.real))
    Lsize.append(a)
err_vals=[]
eigvals=np.array(eigvals)
eigvals1=np.array(eigvals1)
for j in range(len(Lsize)):
    err_vals.append(abs(eigvals1[j]-eigvals[j])/abs(eigvals[j]))
err_vals=np.array(err_vals)



ll=['E_0','E_1','E_2','E_3','E_4','E_5']
for i in range(6):
     plt.plot(Lsize,err_vals[:,i],label=ll[i])
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.xlabel("Box Size(L)",fontsize=15)
plt.ylabel(r"Relative Error $\frac{\vert E(2L)-E(L)\vert}{E(L)}$ ",fontsize=13)
plt.xticks(size=12)
plt.yticks(size=12)
plt.tight_layout()
plt.show()

# In[ ]:




