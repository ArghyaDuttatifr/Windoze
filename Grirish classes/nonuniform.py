
import matplotlib.pyplot as plt
import numpy as np

sigma = 1
mu = 0
fig, axe = plt.subplots(dpi=80)
data = np.random.normal(mu, sigma, 3000)
n, bins, _ = axe.hist(data, bins=40, density=True)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
axe.plot(bins, y, '--', color='r')
plt.show()