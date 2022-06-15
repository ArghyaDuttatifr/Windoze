
import numpy as np
import matplotlib.pyplot as plt
import time

#this is an example distribution, feel free to change it
def p(x):
    return  np.sin(x-0.5)**2 * np.exp(-x**2) + .2*np.exp(-x**2) #note, this one is not normalized pdf #note, this one is not normalized pdf
x = np.linspace(-3, 3, 1000)
plt.plot(x, p(x))

def accept_reject(N):
    start = time.time()
    xmin = -3
    xmax = 3
    pmax = 0.8

    n_accept=0
    x_list = [] 
   
    while n_accept < N:
        x1=np.random.rand()
        y = np.random.rand()
        t = (xmax-xmin)* x1 + xmin
        if y < p(t)/ pmax:
            n_accept += 1
            x_list.append(t)
    end = time.time()
    print("Time: ", end-start)
    return x_list
    
    

x = accept_reject(100000)
bins, edges, patches = plt.hist(x, bins=50, density=True)
plt.show()



'''
xmin = -3
xmax = 3
pmax = 0.8
N_MC = 100000

t = np.random.uniform(xmin,xmax,N_MC)  #get uniform temporary x values
y = np.random.uniform(0,pmax,N_MC)  # get uniform random y values
# plot all the t-y pairs
plt.scatter(t,y, s=0.1, c='orange')
#make a mask that keeps index to the accepted pairs. Plot them
mask = y<p(t)
plt.scatter(t[mask],y[mask], s=0.1)
plt.show()

'''

