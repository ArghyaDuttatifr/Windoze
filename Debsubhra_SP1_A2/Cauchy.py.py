#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
def cauchy_dis(x):
    return (param/np.pi)*(1/(x**2+param**2))
font = {'family': 'cursive',
        'color':  'k',
        'weight': 'bold',
        'size': 14,
        }
a=np.random.rand(50000)


dis_val=[]
param=float(input("Enter value of a:"))
x_vals=np.linspace(-10*param,10*param,80)
if (param<0):
    print("Error: a is out of the range.")
else:
    for i in range(0,len(a)):
        c=np.tan(np.pi*(a[i]-0.5))
        dis_val.append(param*c)
n, bin, patches=plt.hist(dis_val, bins=x_vals, facecolor='green',density=True, alpha=0.5)
plt.ylabel("No of Counts/Total counts", fontdict=font)
plt.xlabel("Values", fontdict=font)
plt.plot(x_vals,cauchy_dis(x_vals),'r--', label="Expected distribution")
plt.title(r"Histogram of Cauchy distribution with $a=$"+str(param), fontdict=font)
plt.xticks(size=13)
plt.yticks(size=13)
plt.legend()
plt.tight_layout()
plt.savefig("Cauchy_dis.png")


# In[ ]:




