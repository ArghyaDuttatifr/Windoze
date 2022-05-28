#question 10
# take help from - https://emcee.readthedocs.io/en/stable/tutorials/line/
import numpy as np
import scipy.optimize
import emcee
from matplotlib import pyplot as plt

x = np.array([201,244,47,287,203,58,210,202,198,158,165,201,157,131,166,160,186,125,218,146  ])
y = np.array([592,401,583,402,495,173,479,504,510,416,393,442,317,311,400,337,423,334,533,344])
sigma_y = np.array([61,25,38,15,21,15,27,14,30,16,14,25,52,16,34,31,42,26,16,22])

def log_likelihood(theta, x, y, sigma_y):
    a, b, c = theta[0], theta[1], theta[2]
    y_1 = 0
    for j in range (len(x)):
        model= a*x[j]**2 + b*x[j] + c
        sigma = sigma_y[j]**2
        y_1 += 0.5*(y[j]-model)**2/sigma + 0.5*np.log(2*np.pi*sigma)
        
    return y_1
def log_pre(theta):
    a, b, c = theta[0], theta[1], theta[2]
    if -1000<a<1000 and -1000<b<1000 and -1000<c<1000:
        return 0
    return -np.inf
def log_prob(theta,x,y,sigma_y):        #full log-probability function 
    lp = log_pre(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp - log_likelihood(theta,x,y,sigma_y)
guess=( 1.0,1.0,1.0 )
soln=scipy.optimize.minimize(log_likelihood,guess,args=(x,y,sigma_y))
print(soln)
pos = soln.x + 1e-4*np.random.randn(50, 3)
nwalkers, ndim = pos.shape
sampler=emcee.EnsembleSampler(nwalkers, ndim, log_prob, args=(x, y, sigma_y))
sampler.run_mcmc(pos,4000, progress = True)
samples= sampler.get_chain()    #accessed of samples
print('best fit parameters',samples)
plt.plot(samples[:, :, 0])
plt.show()

fig, axes = plt.subplots(3, figsize=(10, 7), sharex=True)
samples = sampler.get_chain()
labels = ["a", "b", "c"]
for i in range(ndim):
    ax = axes[i]
    ax.plot(samples[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(samples))
    ax.set_ylabel(labels[i])
    ax.yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel("step number");
plt.show()


flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
print(flat_samples.shape)

import corner

fig = corner.corner(
    flat_samples, labels=labels,truths=[a_true , b_true, c_true] )
plt.show()
