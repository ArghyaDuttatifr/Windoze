
import numpy as np
import matplotlib.pyplot as plt
a=np.random.rand(100)
bernouli=[]
p=float(input("Enter the Value of 'p' for the distribution: "))
if (p>1 or p<0):
    print("Error: P is out of the range.")
else:
    for i in a:
        if (i<p):
            bernouli.append(1)
        else:
            bernouli.append(0)
n, bin, patches=plt.hist(bernouli,bins=[-0.1,0.1,0.99,1.01])
plt.ylabel("No of Counts")
plt.xlabel("Values")
plt.title("Histogram of Bernoulli distribution with P="+str(p))
plt.xticks(size=13)
plt.yticks(size=13)
plt.tight_layout()

