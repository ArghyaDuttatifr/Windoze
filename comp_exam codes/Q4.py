#Question_4_exam
#take help from 3 rd the assignment
#Answer
#packages
from turtle import color
import numpy as np
from scipy import random
import matplotlib.pyplot as plt
from scipy import stats

#uniform probability density
def func(x):
    if (x>3 and x<7):
        return 0.25     
    else:
        return 0

def density(p):
    unif = random.uniform(0,1)
    if unif>=p:
        return False
    else:
        return True
#Metropolis algorithm  
def mcmc(n_h):
    states = []
    a_s =[]
    burn_in = int(n_h*0.20)                   # number of burn-in iterations
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
    
    plt.plot(a_s[burn_in:], states[burn_in:])         #1st part
    plt.title('Histogram of Sample')
    plt.axhline(y=5,alpha=0.4, color='k')
    plt.grid(alpha=0.3)
    plt.show()
    return states[burn_in:]

#2nd part   
lines = np.linspace(1,10,500)
curve = [func(l) for l in lines]
dist = mcmc(10000)
plt.hist(dist,bins=20, density=True)
plt.plot(lines, curve) 
plt.title('Expected Histogram')
plt.grid()
plt.show()

#3rd part
dist_ks = stats.ks_1samp(dist, stats.norm.cdf)
if (( dist_ks[0] <=1 and  dist_ks[0] >=0.99) or ( dist_ks[0] >=0 and  dist_ks[0] <0.01)):
    print("It is 'Not sufficiently random' .")

elif ( dist_ks[0] <=0.05 or  dist_ks[0] >=0.95):
    print("In the 'Suspect' range .")

elif( dist_ks[0] <=0.1 or  dist_ks[0] >=0.9):
    print("It is 'almost suspect' .") 

elif( dist_ks[0] >0.1 and  dist_ks[0] <0.9):
    print("It is 'Sufficiently random' .")

else:
    print("Wrong distribution")
print ('The results of KS test is ',dist_ks[0])






