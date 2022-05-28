#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvals


z=np.loadtxt(r'E:\1.physics TIFR\Comp. Phys\corr.dat')
mean_corr=[]
mean_corr_1=[]
error_corr=[]
error_corr_1=[]
error_corr_2=[]

#The calculation of average and rms error using two loops 
for i in range (0,96):
    sum=0
    for j in range(i,4800,96):
        sum=sum+z[j,1]
    mean_corr.append(sum/50)

for i in range (0,96):
    sum=0
    for j in range(i,4800,96):
        sum=sum+(z[j,1]-mean_corr[i])**2
    error_corr.append(np.sqrt((sum/50)*(1/49)))

#####################################################################

#The calculation of average and rms error using one loop but with more roundoff errors
for i in range (0,96):
    sum=0
    sum1=0
    for j in range(i,4800,96):
        sum=sum+z[j,1]
        sum1=sum1+(z[j,1])**2
    error_corr_1.append(np.sqrt((1/49)*((sum1/50)-(sum/50)**2)))
print("\n")
###########################################################################

#The calculation of average and rms error using one loop but not more roundoff errors
        
for i in range (0,96):
    mean=0
    var=0
    count=0
    for j in range(i,4800,96):
        count=count+1
        mean1=mean+(z[j,1]-mean)/count
        var1=var+(z[j,1]-mean1)*(z[j,1]-mean)
        mean=mean1
        var=var1
    mean_corr_1.append(mean)
    error_corr_2.append(np.sqrt(var/49))
print('\n')

##############################################################################
fig, ax=plt.subplots(1,2)
ax[0].plot(z[0:96,0],mean_corr)
ax[0].set_yscale("log")
ax[0].set_ylabel(r"$\bar{C}(t)$",fontsize=15)
ax[0].set_xlabel("t", fontsize=15)




ax[1].plot(z[0:96,0],error_corr)
ax[1].set_yscale("log")
ax[1].set_ylabel("rms error",fontsize=15)
ax[1].set_xlabel("t", fontsize=15)

plt.tight_layout()
plt.show()
###############################################################################

#Calculation of the covariance matrix and evaluation of its eigenvalues

cov_arr=[]
for i in range(0,30):
    cov_col=[]
    for j in range(0,30):
        meani=0
        meanj=0
        count=0
        cov=0
        t1=np.arange(33+i,4800,96)
        t2=np.arange(33+j,4800,96)
        for k in range(len(t1)):
            count=count+1
            meani1=meani+(z[t1[k],1]-meani)/count
            meanj1=meanj+(z[t2[k],1]-meanj)/count
            cov=cov+(z[t1[k],1]-meani)*(z[t2[k],1]-meanj1)
            meani=meani1
            meanj=meanj1
        cov_col.append(cov/50)
    cov_arr.append(cov_col)

cov_arr=np.array(cov_arr)
eigenvalues=eigvals(cov_arr)
print("The eigenvalues of the covariance matrix are: ",eigenvalues)


# In[ ]:




