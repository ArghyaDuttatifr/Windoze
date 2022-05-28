
'''
von neumann algorithm
 X_i+1 ={ X_i * a + c} n mod(m)        LCG   X_i  Seed

 '''
import matplotlib.pyplot as plt
a = 230659
c = 9761320
m = 4976
n = 195
x = 3
r = []
num = []

for i in range (n):
    x = (a*(x) + c )%m
    r.append(x)
    num.append(i)
print(r)
plt.scatter(num, r)
plt.show()

#%%
'''
def rng(m=2**32, a=1103515245, c=12345):

    rng.current = (a*rng.current + c) % m
    return rng.current/m

# setting the seed
rng.current = 1
for i in range(10):

    rng()
'''



# %%
