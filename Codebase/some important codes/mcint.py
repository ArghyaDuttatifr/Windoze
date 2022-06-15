from math import exp, pi, sin, sqrt
import random as rnd
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import scipy.stats as stats

rng = default_rng()

# integrand
def func(u):
    return 1/(np.sum(np.sin(u)*np.sin(u)))

# weight pdf
def w(u):
    return exp(-10*(u[0]-1)*(u[0] - 1))

def rSampler(uMin, uMax, nPoints, nBins):
    pFunc = np.vectorize(w)
    max_val = np.ndarray.max(pFunc(np.linspace(uMin, uMax, nBins)))
    dist_arr = []
    while(len(dist_arr) < nPoints):
        u = rnd.uniform(uMin, uMax)
        y = rnd.uniform(0, max_val)
        if y < pFunc([u])[0]: dist_arr.append(u)
    return dist_arr

# integrator
def mcInt(nPoints, uMin, uMax):
    sum = 0
    mu = 1.
    sigma = 1/sqrt(20)
    X = stats.truncnorm(
                (uMin[0] - mu) / sigma, 
                (uMax[0] - mu) / sigma, 
                loc=mu, 
                scale=sigma,
            )
    for i in range(0, nPoints):
        u = np.concatenate(
            ([X.rvs()],
            rng.uniform(uMin[1:], uMax[1:]))
        )
        sum += func(u)
    return sum*np.prod((np.abs(uMax - uMin)))/nPoints

print(mcInt(1000, np.asarray([0, 0, 0]), np.asarray([pi/2, pi/2, pi/2])))