import numpy as np
import scipy.linalg as lg
A = np.array ( [[4,-2,-2,1], [1,3,1,3], [1,2,-1,-2], [2,1,-1,-1]])
print (A)
P, L, U = lg.lu(A)
print (L)
print ('U', U)


B = np.array ( [[4,-2], [1,3], [1,2]])
Q, R = lg.qr(B)
print (Q)
print (R)