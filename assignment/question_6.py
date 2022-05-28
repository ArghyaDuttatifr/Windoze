#Question 6
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x):

  return np.sqrt(2/np.pi)* np.exp(-np.pi * x**2)
x = np.linspace(-3,3,100)
y = gaussian(x)
plt.plot(x, y)

def gaussian_rejection(N):
    x0 = -3
    xmax = 3
    gaussian_max = 0.8     #set the range of x and 0.8 is the maximum value of y

    n_accept=0
    x_list = [] 
    while n_accept < N:
        t = x0 + (xmax-x0)* np.random.rand() 
        y = np.random.rand()
        if y < gaussian(t) / gaussian_max:     
            n_accept += 1             #accept the value according to this condition
            x_list.append(t)
    print(len(x_list))
    return x_list

x1 = gaussian_rejection(10000)
plt.hist(gaussian_rejection(10000), density =  True , bins=20)
plt.grid()
plt.show()