#Question 2 ( Eigen values changes because of finite L )
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

LL = np.linspace(2,16, 8)
for k in b:
    E1, E2, E3 = [], [], []
    for L in LL:
        eigenvalues = getEigVal(L, k)
        E1.append(eigenvalues[0])
        E2.append(eigenvalues[1])
        E3.append(eigenvalues[2])
    
    DE1 = [(E1[i+1] - E1[i])/E1[i] for i in range(7)]
    DE2 = [(E2[i+1] - E2[i])/E2[i] for i in range(7)]
    DE3 = [(E3[i+1] - E3[i])/E3[i] for i in range(7)]
    
    '''plt.plot(LL[:7], DE1, color='b')
    plt.plot(LL[:7], DE2, color='y')
    plt.plot(LL[:7], DE3, color='r')
    plt.title('For k = '+str(k))
    plt.xlabel("Lenth of Box",fontsize=15)
    plt.ylabel("Energy difference",fontsize=13)'''
   
    
    
    plt.plot(LL, E1, color='g')
    plt.plot(LL, E2, color='r')
    plt.plot(LL, E3, color='y')
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.title('For k = '+str(k))
    plt.xlabel("Length of Box",fontsize=15)
    plt.ylabel("Energy eigenvalue",fontsize=13)
    plt.grid()
    
    plt.show()
   
   