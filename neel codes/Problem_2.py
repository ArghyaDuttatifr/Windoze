import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse as sparse
from scipy.sparse.linalg import eigs


k=float(input("Enter the value of k "))
lamda=float(input("Enter the value of Lambda "))
N=4000


def Kinetic(r):               #Writing Kinetic term in terms of Matrix
    h=r[1]-r[0]
    main_diag=-2/h**2* np.ones(N)
    off_diag=1/h**2 *np.ones(N-1)
    bv1_diag=np.array([1.0/h**2])
    bv2_diag=np.array([1.0/h**2])
    kinetic_M=sparse.diags([main_diag, off_diag, off_diag,bv1_diag,bv2_diag],(0,-1,1,(N-1),-(N-1)))
    return kinetic_M

def potential(r):              #Writing Potential term in terms of Matrix
    V=0.5*k*r**2+(1/24)*lamda*r**4
    potential_M=sparse.diags(V)
    return potential_M

def hamiltonian(r):             #Writing Total Hamiltonian in terms of Matrix
    hamiltonian = - 0.5*(Kinetic(r))+ potential(r)
    return hamiltonian

# Eigenvalue Determination
r=np.linspace(-10,10, N,endpoint=False)
hamiltonian_1=hamiltonian(r)
N_eigen=10                        # Number of Eigenvalues to find
eigenvalues, eigenvectors =eigs(hamiltonian_1, k=N_eigen, which='SM')
print("Energy Eigenvalues: ", eigenvalues.real)
eigenvectors = np.array([x for _, x in sorted(zip(eigenvalues, eigenvectors.T), key=lambda pair: pair[0])])

#Plotting

def plot(r, densities,eigenvalues):
    plt.xlabel('X (Distance)')
    plt.ylabel('Probability density')
    energies = ['E = {: >5.5f} '.format(eigenvalues[i].real) for i in range(6)]

    plt.plot(r , densities[0]/np.sqrt(r[1]-r[0]), color='red',  label=energies[0])
    plt.plot(r , densities[1]/np.sqrt(r[1]-r[0]), color='Orange', label=energies[1])
    plt.plot(r , densities[2]/np.sqrt(r[1]-r[0]), color='green',  label=energies[2])
    plt.plot(r , densities[3]/np.sqrt(r[1]-r[0]), color='cyan',  label=energies[3])
    plt.plot(r , densities[4]/np.sqrt(r[1]-r[0]), color='blue',  label=energies[4])
    plt.plot(r , densities[5]/np.sqrt(r[1]-r[0]), color='violet',  label=energies[5])
    plt.legend()
    plt.show()
