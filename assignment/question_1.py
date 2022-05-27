#Question 1
import matplotlib.pyplot as plt
import numpy as np
'''von neumann algorithm
 X_i+1 ={ X_i * a + c} n mod(m)        LCG   X_i  Seed'''


a = 230659
c = 9761320
m = 497656
n = 10000
x = 345   #seed
r = []
num = []

for i in range (n):
    x = (a*(x) + c )%m
    r.append(x/(m-1))
    num.append(i)
#print(r)
plt.hist( r, bins=50 )


plt.show()

