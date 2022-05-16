
'''
von neumann algorithm
 X_i+1 ={ X_i * a + c} n mod(m)        LCG   X_i  Seed

 '''
a = 230659
c = 9761320
m = 4976
n = 100
x = 3
r = []
for i in range (n):
    x = (a*(x) + c )%m
    r.append(x)

print(r)




























































































