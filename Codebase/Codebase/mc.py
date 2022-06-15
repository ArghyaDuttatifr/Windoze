from math import exp
import random as rnd
import numpy as np
import matplotlib.pyplot as plt

# print(rnd.uniform(5.1, 5.6))

# poi_arr = np.random.normal(size=10000)
# plt.hist(poi_arr, bins=100)
# plt.show()

def pdf(x):
    y = x*x
    return y

def sampler(range, nPoints, nBins):
    pFunc = np.vectorize(pdf)
    max_val = np.ndarray.max(pFunc(np.linspace(range[0], range[1], nBins)))
    dist_arr = []
    while(len(dist_arr) < nPoints):
        x = rnd.uniform(range[0], range[1])
        y = rnd.uniform(0, max_val)
        if y < pFunc([x])[0]: dist_arr.append(x)
    return dist_arr

plt.hist(sampler([-3., 3.], 10000, 100), bins=100, density=True)
x = np.linspace(-3., 3., 100)
y = pdf(x)/(18)
plt.plot(x,y,'r')
plt.show()