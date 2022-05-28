import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig
x=np.loadtxt("a.txt")         #reading given txt file
mean=[]
T=np.linspace(0,95,96)        #creating T array
for t in range(96):
    c=0
    for i in range(0,4709,96):
        c=c+x[t+i,1]
    c0=c/50
    mean.append(c0)
A=[]
B=[]
E=[]
F=[]
G=[]
S=[]
for t in range(96):
    d=0
    r=0
    f=0
    for i in range(0,50):
        d=d+((x[t+i*96,1])**2)
        r=r+((x[t+i*96,1]-mean[t])**2)
    variance1=(d/50)-((mean[t])**2)      #variance using first formulae
    variance2=r/50                       #variance using second formulae
    y=variance2 - variance1
    error1=np.sqrt(variance1/49)         #error calculation using first variance
    error2=np.sqrt(variance2/49)         #error calculation using second variance
    S.append(y)
    E.append(error2)
    G.append(error1)
    B.append(variance2)
    A.append(variance1)


cor=np.zeros((30,30))
for t1 in range(33,63):
    for t2 in range(33,63):
        n=0
        for i in range(0,4709,96):
            n=n+(x[t1+i,1]-mean[t1])*(x[t2+i,1]-mean[t2])
            k=n/np.sqrt(A[t1]*A[t2])
        cor[t1-33,t2-33]=k/50
eigenvalues,eigv=eig(cor)
print(eigenvalues)
plt.plot(T,mean)
plt.errorbar(T,mean,yerr=E,fmt='o')
#plt.plot(T,E)
#plt.plot(T,A)
#plt.plot(T,S)
plt.title("round off error")
plt.show()