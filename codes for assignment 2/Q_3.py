#QUESTION 3
#PART A
#libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

font = {'family': 'cursive',
        'color':  'b',
        'weight': 'normal',
        'size': 14,
        }                 # take this font idea from Debsubhra

'''Importing the corr.dat file'''
data = np.loadtxt(r'E:\1.physics TIFR\Comp. Phys\corr.dat')
t= data[:,0]     # time in seconds
corr= data[:,1]      # values of measurement of correlation fn at different times

n2=50 #"measurements" of the correlation function
n1=96  # observation number , ranges 0 to 95

mean =[]
C_M =[] 
T =[]    #time 
var1 = []
var2 = []
rms= []
m_u= []
error_u = []

cov1=[]



#Creating the matrix 
C=np.zeros([n1, n2])
for i in range(n2):
    for j in range(n1):
        C[j][i]=corr[j+ 96*i]   # as the values for same t after 96 values
        C_M.append(C[j][i])
                    
#print (C_M) 
#print (C) 
for i in range(n1):
    T.append(t[i])
#Now calculate the mean and variance(by 2nd formula )

m = np.zeros(96)  #row of 96 element
m2 = np.zeros(96)  
m3 = np.zeros(96)  
v = np.zeros(96)
s = np.zeros(96)
for i in range(96):
    for j in range (n2):
        m[i] += C[i][j]
        #m2[i] += C[i][j]
        v[i] += (C[i][j])**2
        
    mean.append (m[i]/50)
    var2.append(( v[i])/50 - (mean[i])**2 )
    rms.append(((var2[i])/49)**(1/2))
#variance by 1st formula   
for i in range(n1):
    for j in range(n2):
        m2[i]+= (C[i][j] - mean[i] )**2
    var1.append(m2[i]/50)   
#print ('Variance using 1 st formula ', var1)
#print ('Variance using 2 nd formula ', var2)
plt.plot( T, rms )
'''plt.plot( T,mean )
plt.plot( T, var1 )
plt.title( 'Mean changes with time ')
plt.ylabel('mean and variance', fontdict = font)'''

plt.xlabel('Time ', fontdict = font )
plt.ylabel('RMS VALUE', fontdict = font)
plt.title( 'RMS Value changes with time ', size = '15')
#plt.plot( T, var2)
plt.yscale("log") 
#plt.legend(["Mean", "Variance"]) 
#print ('var2 ', var2)
#print ('var1', var1)
plt.legend(["rms value"])
 
##
# To get Mean and Variance in a single loop

for i in range (0,96):
    mean1=0
    var=0
    count=0
    for j in range(i,4800,96):
        count=count+1
        mean2 = mean1+ ( data[j,1]-mean1 )/count
        var1=var+( data[j,1]-mean2 )*( data[j,1]- mean1 )
        mean1 =mean2
        var=var1
    m_u.append(mean)
    error_u.append(np.sqrt(var/50))
#print(mean)

#PART B

'''cov = np.zeros([30, 30])   #not in use
for i in range (30):
    for j in range (30):
        for k in range (50):
            cov[i][j]+= ( C[i+33][k]- mean[i+33] ) * ( C[j+33][k]- mean[j+33] )
        cov[i][j]= cov[i][j]/50
        cov1.append(cov)
'''      
#print (cov)  
cor=np.zeros((30,30))
for i in range(33,63):
    for j in range(33,63):
        n=0
        for k in range(0,4800,96):
            n= n+ ( data[i+k,1]-mean[i])*(data[k+j,1]-mean[j])
            k1= n/ (np.sqrt(var2[i]*var2[j]))
        cor[i-33, j-33] = k1 /50
eigs = eigh( cor, eigvals_only=True)
#eigenvalues,eigv = eig(cor)
print ('Eigen values are ',eigs)

'''cor = np.zeros([30,30])     #not in use 
  
for i in range(30):
    for j in range (30):
        cor[i][j] = cov[i][j]/((var2[i])**0.5 * var2[j]**(0.5))
#print (cor[i][j])


'''




