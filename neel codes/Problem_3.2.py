import numpy as np
from numpy.linalg import eigvals

x=np.loadtxt(r"Location/corr.dat")
mean=[]
error=[]
cov_arr=[]
for i in range(0,30):
    cov_col=[]
    for j in range(0,30):
        mean1=0
        mean2=0
        count=0
        cov=0
        t1=np.arange(33+i,4800,96)
        t2=np.arange(33+j,4800,96)
        for k in range(len(t1)):
            count+=1
            mean1+=(x[t1[k],1]-mean1)/count
            mean2+=(x[t2[k],1]-mean2)/count
            cov+=(x[t1[k],1]-mean1)*(x[t2[k],1]-mean2)
        cov_col.append(cov/50)
    cov_arr.append(cov_col)

cov_arr=np.array(cov_arr)
evalues=evals(cov_arr)
print("The eigenvalues of the covariance matrix are: ",evalues)
