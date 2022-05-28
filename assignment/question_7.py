#Question 7
import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats, random 

N = 144
''' scipy.stats.chi2.cdf(18.7625,10.00)
a= np.random.randint(1, 7, size=N) 
b= np.random.randint(1, 7, size=N) 
x = a+b'''
p = N* np.array([1,2,3,4,5,6,5,4,3,2,1])/36
l=0
n = np.array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])
# sum =0
#n = np.array([3,7,11,15,19,24,21,17,13,9,5])

for i in range (0,11):
    l = l + ((n[i]- p[i])**2) / p[i]

print('chi square =',l)

result = stats.chi2.cdf(l, 10.0)
print( result )

if (( result <=1 and  result >=0.99) or ( result >=0 and  result <0.01)):
    print("It is 'Not sufficiently random' .")

elif ( result <=0.05 or  result >=0.95):
    print("In the 'Suspect' range .")

elif( result <=0.1 or  result >=0.9):
    print("It is 'almost suspect' .") 

elif( result >0.1 and  result <0.9):
    print("It is 'Sufficiently random' .")

else:
    print("Wrong distribution")

