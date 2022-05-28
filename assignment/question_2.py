#Question 2
import numpy as np
import matplotlib.pyplot as plt 

N = 10000
den = np.random.rand(N)
plt.hist(den, bins=50)
plt.grid()

plt.show()