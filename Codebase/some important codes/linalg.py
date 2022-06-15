import numpy as np
from scipy import linalg

a = np.array([[2,1,1], [4, 2.001, 0], [-2, 7, 2]])
b = np.array([5, 0, 9])

x = linalg.solve(a, b)
print(x)

