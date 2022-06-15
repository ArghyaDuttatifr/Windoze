#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
font = {'family': 'cursive',
        'color':  'k',
        'weight': 'bold',
        'size': 12,
        }
a=np.random.rand(100)
Bernouli=[]
p=float(input("Enter the Value of 'p' for the Bernouli distribution: "))
if (p>1 or p<0):
    print("Error: P is out of the range.")
else:
    for i in a:
        if (i<p):
            Bernouli.append(1)
        else:
            Bernouli.append(0)
n, bin, patches=plt.hist(Bernouli,bins=[-0.01,0.01,0.99,1.01], density=True)
plt.ylabel("No of Counts", fontdict=font)
plt.xlabel("Values", fontdict=font)
plt.title("Histogram of Bernoulli distribution with P="+str(p), fontdict=font)
plt.xticks(size=13)
plt.yticks(size=13)
plt.tight_layout()
plt.savefig("Bernoulli_dis.png")


# In[ ]:





# In[ ]:




