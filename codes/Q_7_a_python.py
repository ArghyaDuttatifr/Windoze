
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli, binom
import seaborn as sns

p = float(input("Enter the Value of 'p' for the distribution: "))
X = bernoulli(p)

print(np.round(X.pmf(1),3))

print(np.round(X.pmf(0), 3))

X_samples = np.random.rand(5000)      #random number generates
sns.histplot(X_samples, stat="density", discrete=True, shrink=0.1);
plt.ylabel("Number of Counts")
plt.xlabel("Values")
plt.title("7(a) : Histogram plot of Bernoulli distribution with p = "+str(p))
plt.xticks(size=13)
plt.yticks(size=13)
