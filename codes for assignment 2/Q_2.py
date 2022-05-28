
import numpy as np
from scipy import linalg as sc
from scipy import sparse as sparse
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt
b=[-1,1]
 #hcross =1 
    #defining some required constants
def getEigVal(L, k):
    m=1
    N=1000
    eps=L/(N)
 #defining the kinetic energy matrix
    diagonal = 2/(eps**2*m)*np.ones(N)
    off_diagonal = -1/(m*eps**2)*np.ones(N-1)
    #A=sparse.diags([diagonal,off_diagonal,off_diagonal],(0,-1,1))
    bv1_diag= np.array([-1.0/ eps**2])
    bv2_diag= np.array([-1.0/ eps**2])
    H = sparse.diags([diagonal , off_diagonal , off_diagonal ,bv1_diag ,bv2_diag ],(0,-1,1,(N-1),-(N-1)))
    #H = sparse.diags([diagonal , off_diagonal , off_diagonal ],(0,-1,1))
    x= np.linspace(-L/2,L/2,N, endpoint=False)
    V= np.zeros([N,N])
    
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
    
    number_of_eigenvalues = 30
    eigenvalues, eigenvectors = eigsh( Hamiltonian , k=number_of_eigenvalues, which='SA')
    eigenvectors = np.array([x for _, x in sorted(zip(eigenvalues, eigenvectors.T), key=lambda pair: pair[0])])
    eigenvalues = np.sort(eigenvalues)/2
    
    return eigenvalues

LL = np.linspace(2,10,6)
for k in b:
    E1, E2, E3 = [], [], []
    for L in LL:
        eigenvalues = getEigVal(L, k)
        E1.append(eigenvalues[0])
        E2.append(eigenvalues[1])
        E3.append(eigenvalues[2])
    
    DE1 = [(E1[i+1] - E1[i])/E1[i] for i in range(5)]
    plt.plot(LL[:5], DE1, color='b')
    '''plt.plot(LL, E2, color='g')
    plt.plot(LL, E3, color='r')'''
    
    plt.show()
    input()
    print("here")
    '''
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
    #H = sparse.diags([diagonal , off_diagonal , off_diagonal ,bv1_diag ,bv2_diag ],(0,-1,1,(N-1),-(N-1)))
    H = sparse.diags([diagonal , off_diagonal , off_diagonal ],(0,-1,1))
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
    plt.title('The wavw function graph is for k = '+str(k))

    plt.xlim(-5, 5)
    plt.legend(['E = {: >2.2f}'.format(eigenvalues.real[0]),'E = {: >2.2f}'.format(eigenvalues.real[1]), 'E = {: >2.2f}'.format(eigenvalues.real[2]), 'E = {: >2.2f}'.format(eigenvalues.real[3]) ], loc="upper right")

    plt.grid()
    plt.show()
print (H.toarray())
'''

