#two dice problem
import numpy as np
N = 144
a1 = np.random.randint(1 , high=7, size=N)
a2 = np.random.randint(1 , high=7, size=N)
a = a1+a2
from scipy.stats import chi2
print(a)
v, n = np.unique(a, return_counts=True)
print (v)
prob = N * np.array([1,2,3,4,5,6,5,4,3,2,1])/36
y = np.sum((n-prob)**2/prob)
out = chi2.cdf(y, 10)
print (out)
