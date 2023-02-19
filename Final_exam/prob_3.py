import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
z=np.loadtxt('data.txt')
F=CubicSpline(z[:,0],z[:,1])
x=z[:,0]
y=[]
for k in range(len(x)):
    y.append(F(x[k]))
fig,ax=plt.subplots(1,2)
ax[0].scatter(z[:,0],z[:,1],c="red")
ax[0].set_xlabel("X_Vals")
ax[0].set_ylabel("Y_Vals")
ax[1].plot(x,y)
ax[0].set_title("Data Point")
ax[1].set_xlabel("X_Vals")
ax[1].set_ylabel("Y_Vals")
ax[1].set_title("The interpolated Curve")
plt.show()
def bisection(a,b,ep):
    r=(a+b)/2
    while(abs(F(r))>ep):
        if (F(r)*F(a)>0):
            a=r
        else:
            b=r
        r=(a+b)/2
    return r

print("The root of the interpolated function found to be: ",bisection(-1,1,1e-8))


