import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

npoints = 100000

def getVol(ndim, npoints):
    accepted = 0

    for i in range(npoints):
        rnd = rng.uniform(size=ndim)
        accepted += 1*(np.sum(rnd*rnd) < 1)
    
    return pow(2, ndim)*accepted/npoints

Vol = []
for ndim in range(1,11):
    Vol.append(getVol(ndim, npoints))

plt.plot(range(1,11), Vol)
plt.xlabel("dim")
plt.ylabel("Vol")
plt.savefig("sphr.png")