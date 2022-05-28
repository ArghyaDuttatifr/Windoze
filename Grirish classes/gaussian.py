#%%
''''
import numpy as np
import matplotlib.pyplot as plt
x1= np.random.rand(100000)
x2= np.random.rand(100000)
y1= np.sqrt(-2*np.log(x1))* np.cos(2*np.pi*  x2)
y2= np.sqrt(-2*np.log(x1))* np.sin(2*np.pi*  x2)
plt.hist(y1, bins=50)
plt.show()



'''
import numpy as np
import matplotlib.pyplot as plt
#x = np.random.rand(10000)
def gauss(x):
    return np.sqrt(2/np.pi)* np.exp(-np.pi * x**2)

xs = np.linspace(-2, 2 ,100000)
ys = gauss(xs)
#plt.hist(ys)

plt.plot(xs, ys)


plt.fill_between(xs, ys, 0, alpha=0.2)
plt.xlabel("x"), plt.ylabel("f(x)")

def batch_sample_2(function, num_samples, xmin=-10, xmax=10, ymax=1.0):
    
    x = np.random.uniform(low=xmin, high=xmax, size=num_samples)
    y = np.random.uniform(low=0, high=ymax, size=num_samples)
    passed = (y < function(x)).astype(int)
    
    return x, y, passed

x, y, passed = batch_sample_2(gauss, 1000)

plt.scatter(x, y,c=passed,  cmap="RdYlGn", vmin=-0.0, vmax=1.1, lw=0, s=5)
plt.xlabel("x"), plt.ylabel("y"), plt.xlim(-5, 5), plt.ylim(0, 1.0)
plt.hist(passed)

print(f"Efficiency is only {passed.mean() * 100:0.1f}%")

plt.show()


# %%
