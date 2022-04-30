#ques 3
#all packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigs
from scipy import sparse as sparse


#hbar=1          #take in natural units

m_charm =1.32     #in GeV units 
mu = 1.32/2.0        # m_charm /2
alpha =0.471
sigma =0.2025         #in GeV^2 units

N= 2500
l= 1
r = np.linspace(14, 0.0, N, endpoint =False)    #set the range of r 


def poten(r):
    V = -alpha/r + sigma*r
    pot_term=sparse.diags((V))
    return pot_term
def angular(r):
    angular = l*(l+1)/r**2
    angular_term =sparse.diags((angular))
    return angular_term
def laplace_rule(r):
    h = r[1]-r[0]
    main_diagonal = -2.0/h**2 * np.ones(N)
    off_diagonal = 1.0/h**2 *np.ones(N-1)
    laplace_term = sparse.diags([main_diagonal, off_diagonal, off_diagonal],(0,-1,1))
    return laplace_term

def tot_hamiltonian(r):  #build the main hamiltonian
    l_t = laplace_rule(r)
    a_t = angular(r)
    p_t = poten(r)
    
    hamiltonian = -1.0/(2.0 * mu) *(l_t - a_t) + p_t
    return hamiltonian

def plot(r, density,eigenvalue ):
    energies = [ '{: >5.5f}'.format(eigenvalue[i].real ) for i in range(2) ]
    plt.plot( r , density[0], 'g', label= ('E = ', energies[0], 'in Gev') )
    plt.plot(r , density[1], 'r', label= ( 'E = ', energies[1], 'in GeV') )
    plt.xlabel('X ($GeV^{-1}$)')
    plt.ylabel('Probability Density ( $GeV$ )')
    plt.legend()
    plt.grid()
    plt.title('Plot of probablity density for l=1 ')
    plt.show()
    Ea= float(energies[0])
    Eb= float(energies[1])
    
    print ( 'energy of the lowest l = 1 state is =\n',energies[0], 'GeV')               #banswer as output
    print ( 'The mass of the lightest P-wave meson is = \n' ,(Ea + 2*m_charm))   #answer as output
    print ( 'energy of the next l = 1 state is =\n',energies[1], 'GeV')               #banswer as output
    print ( 'The mass of the next lightest P-wave meson is = \n' ,(Eb + 2*m_charm))   #answer as output

    return    

hamiltonian = tot_hamiltonian(r)

number_of_eigenvalue =35
eigenvalue , eigenvector = eigs(hamiltonian, k=number_of_eigenvalue, which='SM')
eigenvectors = np.array([x for _, x in sorted( zip(eigenvalue, eigenvector.T), key=lambda pair: pair[0])])
eigenvalues= np.sort(eigenvalue)
density = [ np.absolute(eigenvectors[i, :])**2 for i in range(len(eigenvalues)) ]


plot(r, density, eigenvalues)
  