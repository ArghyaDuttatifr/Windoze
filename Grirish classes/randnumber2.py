from cmath import pi
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
'''np.pi = pi
n = 2000
x_range = np.linspace(0, 5, 1000)
y_func = 2*np.sqrt(2/pi) * np.exp(-x_range**2 /2)
x = np.random.random(n)*10
y = np.random.random(n)*1
print (x)
x_good = []
for i in range(n):
    if (y[i]<np.sqrt(2/pi) * np.exp(-x[i]**2 /2) ):
        x_good.append(x[i])
plt.hist(x_good, bins= 100)
plt.scatter(y, x, vmin=-0.0, vmax=1.1, lw=0, s=5)
plt.plot(x_range, y_func)
'''



import numpy as np
import matplotlib.pyplot as plt

N=10000
arr = []
ar1 = []
x = np.zeros(N)
a = 26801522
c = 152783930
m = 250678291
ini = 1256822
arr.append(ini)
ar1.append(ini/(m-1))

for i in range (1,N):
    x[i] = i
    ty = ((arr[i-1]*a+c)%m)
    ar1.append(ty/(m-1)) 
    arr.append(ty)

plt.hist(ar1)
plt.show()








plt.show()
