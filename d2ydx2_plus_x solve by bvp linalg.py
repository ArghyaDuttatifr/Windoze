#y"+3y = 0 solve by bvp linalg

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

#  Define our grid
N = 50
x = np.linspace(0, 2 * np.pi, N)

# Calculate the grid spacing.  Since we are using a uniform sequence, all the values are the same so we only need one entry of the resulting diff array.
Delta = np.diff(x)
Delta = Delta[0]

#  Define the diagonal elements for the second derivative matrix
D = -2 * np.ones(N)
Dm1 = np.ones(N-1)
D1 = np.ones(N-1)

#  Create the matrix
M1 = diags([Dm1, D, D1], [-1, 0, 1], shape = (N, N), format = 'csc')

#  Divide through by 1/Delta**2 prefactor
M1 = M1 / Delta**2

#  Reset the elements corrisponding to the boundary values
M1[0, 0] = 0
M1[0, 1] = 0
M1[-1, -1] = 0
M1[-1, -2] = 0

#  Create out 3y diagonal matrix and set the boundary value elements
M2 = diags( 3 * np.ones(N), 0, shape = (N,N), format = 'csc')
M2[0,0] = 1
M2[-1, -1] = 1

M = M1 + M2

#  This is the vector of known values from the RHS of our matrix above.
b = np.zeros(N)
b[0] = 7

#  Solve the system
y = spsolve(M, b)

#plt.plot(x, return_exact(x), 'k', label='Exact')
plt.plot(x, y, 'b.', label='Finite Difference')
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')