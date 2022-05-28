#question 4
import numpy as np

import matplotlib.pyplot as plt

#generate random numbers
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
y = np.array(r)
#print (y)

expo = -0.5* np.log(r)
    
plt.hist(expo,bins=20)
plt.grid()
plt.title("Exponential generator")

plt.show()








