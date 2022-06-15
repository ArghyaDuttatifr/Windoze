# python imports
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# initialise rng
rng = np.random.default_rng()

# proposal pdf (walker)
def proposal(theta):
    theta_p = rng.normal(loc = theta)
    return theta_p

# target distribution
def target(theta):
    rv = norm(loc = 2., scale=2.)
    return rv.pdf(theta)

# metropolis algorithm
def metropolis(theta_i):
    theta = theta_i
    while (all(theta==theta_i)):
        temp = proposal(theta_i)
        theta = temp if all(target(temp)/target(theta_i) > rng.uniform(size = ndim)) else theta_i
    return theta

# params
ndim = 2
npoints = 10000
theta_i = np.zeros(ndim)

# sample list
sample = [theta_i]

# sampler
for i in range(npoints):
    sample.append(metropolis(sample[-1]))

# plotter
plt.hist([A[0] for A in sample])
plt.show()