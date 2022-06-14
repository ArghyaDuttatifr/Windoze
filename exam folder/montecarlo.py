#monte carlo in n dim
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps


def func1(x):
    # function f(x)= 10 + sum_i(-x_i^2)
    # for 2D: f(x)= 10 - x1^2 - x2^2
    return 10 + np.sum(-1*np.power(x, 2), axis=1)

def domain_unit_circle(x):
    # integration domain: sum of x^2 <= 1 . # For 2d, it's a unit circle; for 3d it's a unit sphere  # returns True for inside domain, False for outside
    return np.power(x,2).sum() <= 1
  
def mc_integrate(func, a, b, dim, n = 1000):
    # Monte Carlo integration of given function over domain from a to b (for each parameter)
    x_list = np.random.uniform(a, b, (n, dim))
    y = func(x_list)
    
    y_mean =  y.sum()/len(y)
    domain = np.power(b-a, dim)
    
    integ = domain * y_mean
    
    return integ


def mc_integrate1(func, given_func, a, b, dim, n = 1000):
    # Monte Carlo integration of given function over domain specified by given_func
    # dim: dimensions of function
    
    # sample x
    x_list = np.random.uniform(a, b, (n, dim))
    
    # determine whether sampled x is inside or outside of domain and calculate its volume
    in_dom = [given_func(x) for x in x_list]
    frac_dom = sum(in_dom)/len(in_dom)           #fraction in domain
    domain = np.power(b-a, dim) * frac_dom
    
    # calculate expected value of func inside domain
    y = func(x_list)
    y_mean = y[in_dom].sum() / len(y[in_dom])
    
    # estimated integration
    integ1 = domain * y_mean
    
    return integ1

print("For f(x)= 10 - x1\u00b2 - x2\u00b2, integrated over unit circle")
print(f"Monte Carlo solution: {mc_integrate1(func1, domain_unit_circle, -2, 2, 2, 10000): .3f}")
# Examples
print("For f(x)= 10 - x1\u00b2 - x2\u00b2, integrated from -2 to 2 (for all x's)")
print(f"Monte Carlo solution for : {mc_integrate(func1, -2, 2, 2, 10000): .3f}")
print("For f(x)= 10 - x1\u00b2 - x2\u00b2 - x3\u00b2, integrated from -2 to 2 (for all x's)")
print(f"Monte Carlo solution: {mc_integrate(func1, -2, 2, 3, 10000): .3f}")

'''
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
 #plot
def f(x, y):
    return  np.sqrt(10 + (x ** 2 + y ** 2))
 
# x and y axis
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
  
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_wireframe(X, Y, Z, color ='green')
ax.set_title('f(x)= 10 - x1\u00b2 - x2\u00b2 - x3\u00b2')
plt.show()

'''
#for 1 d graph

def fn(x):
    return (1 + xs**2) * np.exp(-(xs**2)/2) / np.sqrt(2 * np.pi)

xs = np.linspace(-2 * np.pi , 2 * np.pi, 100)
ys = fn(xs)
area = simps(ys, x=xs)

width = 2.0 * np.pi + 2.0 * np.pi  # The width 
samples = np.random.uniform(low=0, high=width, size=1000000)
mc_area = fn(samples).mean() * width
#error = np.std(samples * width) / np.sqrt(samples.size)

plt.plot(xs, ys, label="Function")
plt.fill_between(xs, 0, ys, alpha=0.1)
plt.text(0, 0.4, f"Area from Simps is {area:0.3f}", fontsize=12)
plt.text(0, 0.3, f"Area from MC Integration is {mc_area:0.3f}", fontsize=12)
plt.xlabel("x"), plt.legend()
plt.show()



'''
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def jointplot():
    """Tool function to create a 3 part grid plot."""
    f = plt.figure(figsize=(10,10))
    gs0 = gridspec.GridSpec(5, 5, figure=f, wspace=.02, hspace=.02)
    ax1 = f.add_subplot(gs0[1:, :-1])
    ax2 = f.add_subplot(gs0[:1, :-1])
    ax3 = f.add_subplot(gs0[1:, -1:])
    return ax1, ax2, ax3

a_1, b_1 = (50,50)
a_2, b_2 = (63,54)

x = pd.Series(np.linspace(.3,.7,1000))
y = stats.beta.pdf(x, a, b)
x_min, x_max = (0, 1)

y_1 = stats.beta.pdf(x, a_1, b_1)
y_2 = stats.beta.pdf(x, a_2, b_2)

X, Y = np.meshgrid(y_1, y_2)
Z = X * Y

# PLOT
ax1, ax2, ax3 = jointplot()

ax1.contourf(x, x, Z, cmap= 'Blues')
ax1.plot(x, x, color = 'orange', label = '$x_A = x_B $')
ax2.plot(x, y_1)
ax3.plot(y_2, x)

ax1.set_xlabel('$X_A$')
ax1.set_ylabel('$X_B$')

ax3.set_axis_off()
ax2.set_axis_off()

ax1.legend()
plt.show()
'''
#https://pub.towardsai.net/monte-carlo-simulation-an-in-depth-tutorial-with-python-bcf6eb7856c8



'''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
'''
'''import random

# Paste your code here
def drawing_without_replacement_sim(numTrials):

    # Your code here
    counter = 0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        picks = []
        for j in range(3):
            k = random.choice(bucket)
            picks.append(k)
            bucket.remove(k)
        if picks[0] == picks[1] == picks[2]:
            counter += 1
    return counter/numTrials                    
    
print(drawing_without_replacement_sim(1000))
'''
