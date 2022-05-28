#%%
import matplotlib.pyplot as plt
import numpy as np

def func(x,a):
    b= np.log(x)
    return (1/np.sqrt(2*np.pi))*(1/x)*np.exp(-b**2/2)*(1+a*np.sin(2*np.pi*b))

x=np.linspace(0.001 ,6,1000)


plt.plot(x,func(x,0),label='a=0',color= 'r')
plt.plot(x,func(x,0.5), label='a=0.5', color='b')

plt.title("Modified Log-Normal Distribution")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend( fontsize=10)

plt.grid()
plt.show()



