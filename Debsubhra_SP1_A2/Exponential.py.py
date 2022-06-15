#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
def pdf_exp_dis(x):
    return d*np.exp(-d*x)
font = {'family': 'cursive',
        'color':  'k',
        'weight': 'bold',
        'size': 14,
        }
a=np.random.rand(10000)
x_vals=np.linspace(0,20,40)
exp_dis=[]
d=float(input("Enter value of the parameter d:"))
if (d<0):
    print("Error: d is out of the range.")
else:
    for i in a:
        exp_dis.append(-(1/d)*np.log(1-i))
n, bin, patches=plt.hist(exp_dis, bins=x_vals, facecolor='green',density=True)
plt.ylabel("No of Counts/Total counts", fontdict=font)
plt.xlabel("Values", fontdict=font)
plt.plot(x_vals,pdf_exp_dis(x_vals),'r--', label="Expected distribution")
plt.title(r"Histogram of Exponential distribution with $\lambda=$"+str(d), fontdict=font)
plt.legend()
plt.xticks(size=13)
plt.yticks(size=13)
plt.tight_layout()
plt.savefig("Exp_dis.png")


# In[ ]:




