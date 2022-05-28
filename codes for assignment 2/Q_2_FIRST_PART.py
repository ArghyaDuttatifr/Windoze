#Question 2
#packages
import numpy as np
from scipy import linalg as sc
from scipy import sparse as sparse
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt
b=[-1,1]
 #hcross =1 
for k in b:
    a=[]
    m=1
    N=1000
    eps=10/(N)
 #defining the kinetic energy matrix
    diagonal = 2/(eps**2*m)*np.ones(N)
    off_diagonal = -1/(m*eps**2)*np.ones(N-1)
    #A=sparse.diags([diagonal,off_diagonal,off_diagonal],(0,-1,1))
    bv1_diag= np.array([1.0/ eps**2])
    bv2_diag= np.array([1.0/ eps**2])
    H = sparse.diags([diagonal , off_diagonal , off_diagonal ,bv1_diag ,bv2_diag ],(0,-1,1,(N-1),-(N-1))) # For Periodic boundary condition
    #H = sparse.diags([diagonal , off_diagonal , off_diagonal ],(0,-1,1))   #for dirichit boundary conditions
    
    
    x= np.linspace(-5,5,N, endpoint=False)
    V= np.zeros([N,N])
# defining the potential function
    def pot(x):
        return k*(x**2)/2 + x**4/24
# defining the potential energy matrix
    for i in range(N):
        for j in range(N):
            if i==j:
                V[i,j]=pot(x[i])
            else:
                V[i,j]=0
# defining the hamiltonial matrix by adding potential and kinetic energy terms
    Hamiltonian = (2*V + H)

# finding the eigenvalues and eigenfunctions
    number_of_eigenvalues = 30
    eigenvalues, eigenvectors = eigsh( Hamiltonian , k=number_of_eigenvalues, which='SA')
    eigenvectors = np.array([x for _, x in sorted(zip(eigenvalues, eigenvectors.T), key=lambda pair: pair[0])])
    eigenvalues = np.sort(eigenvalues)/2

# printing the eigenvalues and eigenfunctions
    print("The ground state energy is",eigenvalues.real[0])
    print("The first excited state energy is",eigenvalues.real[1])
    print("The second excited state energy is",eigenvalues.real[2])
    print("The third excited state energy is",eigenvalues.real[3])
    plt.plot(x,eigenvectors.real[0])
    plt.plot(x,eigenvectors.real[1])
    plt.plot(x,eigenvectors.real[2])
    plt.plot(x,eigenvectors.real[3])
    plt.xlabel("Box Size(L)",fontsize=15)
    plt.ylabel("wave function",fontsize=13)
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.title('The wave function graph for PERIODIC boundary condition,is for k = '+str(k))

    plt.xlim(-5, 5)
    plt.legend(['E = {: >2.2f}'.format(eigenvalues.real[0]),'E = {: >2.2f}'.format(eigenvalues.real[1]), 'E = {: >2.2f}'.format(eigenvalues.real[2]), 'E = {: >2.2f}'.format(eigenvalues.real[3]) ], loc="upper right")

    plt.grid()
    plt.show()
print (H.toarray())






