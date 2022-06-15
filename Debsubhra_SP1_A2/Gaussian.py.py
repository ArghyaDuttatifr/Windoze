#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
def gaussian_dis(x):
    return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-x**2/(2*sigma**2))
font = {'family': 'cursive',
        'color':  'k',
        'weight': 'bold',
        'size': 14,
        }
a=np.random.rand(10000)
b=np.random.rand(10000)

gauss_dis=[]
sigma=float(input("Enter value of the standard deviation:"))
x_vals=np.linspace(-4*sigma,4*sigma,40)
if (sigma<0):
    print("Error: sigma is out of the range.")
else:
    for i in range(0,len(a)):
        c=np.sqrt(-2*np.log(a[i]))*np.cos(2*np.pi*b[i])
        gauss_dis.append(sigma*c)
n, bin, patches=plt.hist(gauss_dis, bins=x_vals, facecolor='green',density=True)
plt.ylabel("No of Counts", fontdict=font)
plt.xlabel("Values", fontdict=font)
plt.plot(x_vals,gaussian_dis(x_vals),'r--', label="Expected distribution")
plt.title(r"Histogram of Gaussian distribution with $\sigma=$"+str(sigma), fontdict=font)
plt.legend()
plt.xticks(size=13)
plt.yticks(size=13)
plt.tight_layout()
plt.savefig("Gauss_dis.png")


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
font = {'family': 'cursive',
        'color':  'k',
        'weight': 'bold',
        'size': 15,
        }

def func(x,a):
    b=np.log(x)
    return (1/np.sqrt(2*np.pi))*(1/x)*np.exp(-b**2/2)*(1+a*np.sin(2*np.pi*b))

x=np.linspace(0.01,5,1000)
plt.plot(x,func(x,0),linewidth=2,label='a=0')
plt.plot(x,func(x,0.5),linewidth=2, label='a=0.5')
plt.xlabel("x",fontdict=font)
plt.ylabel("P(x)",fontdict=font, fontstyle='italic')
plt.legend(frameon=False, fontsize=12)
plt.title("Modified Log Normal Distribution", fontdict=font)
plt.tight_layout()
plt.savefig("SP2_P9_a.png")
plt.show()


# In[31]:


import numpy as np
from scipy.integrate import simpson
def func(x):
    return np.exp(-x**2/2)*np.cos(2*np.pi*x)
x_vals=np.linspace(-20,20,1000)
f_vals=func(x_vals)
print(simpson(f_vals,x_vals))
print(np.sqrt(2*np.pi)*np.exp(-2*np.pi**2))


# In[ ]:





# In[ ]:




