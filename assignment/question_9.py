#Question_9
from scipy import random
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    if (x>=3 and x<=7):
        return 0.36
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
    burn_in = int(n_h*0.2)
    current = random.uniform(0, 11)
    for i in range(n_h):
        a_s.append(i)
        states.append(current)
        movement = random.uniform(0,11)
        
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
    
#lines = np.linspace(-3,3,1000)

dist = mcmc(10000)
plt.hist(dist,bins=20) 
plt.grid()
plt.show()