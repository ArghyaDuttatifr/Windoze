
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(12000)
y= -np.log(x)
plt.hist(y, bins=55)
plt.show()