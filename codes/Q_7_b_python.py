


import numpy as np
import matplotlib.pyplot as plt


def exp_dist(x):
    return lambda_ * np.exp(- x *lambda_ )

a=np.random.rand(5000)

x_vals=np.linspace(0,5,100)
dist =[]

lambda_ =float(input(" enter value of $\lambda$ = "))

for k in a:
    dist.append(-(1/ lambda_ )* np.log(1- k))
n, bin, patches = plt.hist(dist , bins=x_vals, facecolor='green',density=True)

plt.plot(x_vals ,exp_dist(x_vals),'b+', label="Expected given distribution")
plt.title( " Histogram of Exponential distribution for $\lambda=$"+str(lambda_ ), color='b' ) 
plt.ylabel("total counts", color='r')
plt.xlabel("Values" )

plt.legend()





