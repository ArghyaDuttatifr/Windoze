#question 5

import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphas
def generator(n):
    u1 = np.random.rand(n)
    u2 = np.random.rand(n)
    u = - np.sqrt(-2* np.log(u1))
    X = u*np.cos(2*np.pi* u2)
    Y = u*np.sin(2*np.pi* u2)
    plt.hist(X, bins=50, alpha= 1, color='violet')
    #plt.show()
    normal = np.random.normal(0, 1, n)    
    plt.hist(normal , bins=50, alpha = 0.8, color='red')
    plt.grid()
    plt.legend(['Box-Mullar', 'Inbuilt random no. generator'])
    plt.xlabel("Random numbers")
    plt.ylabel("Probability distribution")
    plt.show()

generator(10000)
