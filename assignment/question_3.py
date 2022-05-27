#Question 3
import matplotlib.pyplot as plt
import numpy as np
import time

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
start_time_1 = time.time()
plt.hist( r, bins=50 )
dt = time.time() - start_time_1
print("Congruential random number generator took ", (time.time() - start_time_1), "seconds")

start_time_2 = time.time()
den2 = np.random.rand(n)
print("The inbuilt random no. generator took ",(time.time() - start_time_2), "seconds")

plt.hist(den2, bins=60 )
plt.xlabel("Random no. between 0 & 1")
plt.ylabel("Probability distribution")
plt.grid()
plt.show()