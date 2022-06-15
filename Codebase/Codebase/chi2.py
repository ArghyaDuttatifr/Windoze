import numpy as np
from scipy.stats import chi2

N = 1000
A1 = np.random.randint(1, high=7, size=N)
A2 = np.random.randint(1, high=7, size=N)

A = A1 + A2
v, n = np.unique(A, return_counts=True)

Exp = N*np.asarray([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])/36
V = np.sum((n-Exp)*(n-Exp)/Exp)

print(chi2.cdf(V, 10))