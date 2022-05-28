#Question_9
#take help from https://towardsdatascience.com/bayesian-statistics-metropolis-hastings-from-scratch-in-python-c3b10cc4382d

import numpy as np
from scipy import random
import matplotlib.pyplot as plt

def func(x):
    if (x>=3 and x<=7):
        return 0.25     #probability density
    else:
        return 0

def density(p):
    unif = random.uniform(0,1)
    if unif>=p:
        return False
    else:
        return True
    
def mcmc(n_h):
    states = []
    a_s =[]
    burn_in = int(n_h*0.20)    # number of burn-in iterations
    current = random.uniform(0, 10)
    for i in range(n_h):
        a_s.append(i)
        states.append(current)
        movement = random.uniform(0,10)       # uniform random number
        
        curr_prob = func(current)
        move_prob = func(movement)

        if ( curr_prob==0):  
            acceptance = 1
        else:
            acceptance = min(move_prob/curr_prob,1)

        if density(acceptance):
            current = movement
    plt.plot(a_s[burn_in:], states[burn_in:])
    plt.show()
    return states[burn_in:]
    
lines = np.linspace(1,10,500)
curve = [func(l) for l in lines]
dist = mcmc(10000)
plt.hist(dist,bins=20, density=True)
plt.plot(lines, curve) 
plt.grid()
plt.show()