
#Calculation of average and Varience using two loops 

import numpy as np
import matplotlib.pyplot as plt

x=np.loadtxt(r"E:\1.physics TIFR\python code\neel codes\corr.dat")
mean=[]
mean_2=[]
error=[]
error_1=[]
error_2=[]


for i in range (0,96):
    sum=0
    for j in range(i,4800,96):
        sum+=x[j,1]
    mean.append(sum/50)

for i in range (0,96):
    sum=0
    for j in range(i,4800,96):
        sum+=(x[j,1]-mean[i])**2
    error.append(np.sqrt((sum/50)*(1/49)))


#One loop_High error

for i in range (0,96):
    sum1=0
    sum2=0
    for j in range(i,4800,96):
        sum1+=x[j,1]
        sum2+=(x[j,1])**2
    error_1.append(np.sqrt((1/49)*((sum2/50)-(sum1/50)**2)))


#Lowering Error

for i in range (0,96):
    mean=0
    var=0
    count=0
    for j in range(i,4800,96):
        count+=1
        mean1=mean+(x[j,1]-mean)/count
        var1=var+(x[j,1]-mean1)*(x[j,1]-mean)
        mean=mean1
        var=var1
    mean_2.append(mean)
    error_2.append(np.sqrt(var/49))

#Plotting Errors
fig, G= plt.subplots(1,2)

G[0].plot(x[0:96,0],mean)
G[0].set_yscale("log")
G[0].set_ylabel("Mean error")
G[0].set_xlabel("t")

G[1].plot(x[0:96,0],error)
G[1].set_yscale("log")
G[1].set_ylabel("rms error")
G[1].set_xlabel("t")




plt.tight_layout()
plt.show()