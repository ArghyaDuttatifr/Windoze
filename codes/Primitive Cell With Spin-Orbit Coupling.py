# Primitive Cell With Spin-Orbit Coupling:
#Valance Band = 28, Conduction Band =29

# Importing packages:
import pandas as pd
import matplotlib.pyplot as plt

# Importing data:
df = pd.DataFrame(pd.read_excel (r"E:\1.physics TIFR\NM  & experimental notes\bahadur\excel_wsoc_pri_priyanka.xlsx"))

k = df ["k"]
E = df ["E"]
w = df ["w"]

n = 44 # no of bands
# Dividing distribution of different atoms
k1 = []
k2 = []
e1 = []
e2 = []
w1 = []
w2 = []

for i in range(n, 2 * n):
    for j in range (161*(i-1) ,161*i-2):
        k1.append(float(k[j]))
        e1.append(float(E[j]))
        w1.append(15*float(w[j]))

for i in range(2*n,3*n):
    for j in range (161*(i-1) ,161*i-2):
        k2.append(float(k[j]))
        e2.append(float(E[j]))
        w2.append(4*float(w[j]))

s = [75 ** w[n] for n in range(len(w))]

# Designing the graph:
plt.scatter(k1, e1, s=w1, c=w1, cmap = 'winter_r', label = 'Bi')
plt.colorbar()
plt.scatter(k2, e2, s=w2, c=w2, cmap = 'magma', label = 'Se')
plt.colorbar()
plt.ylabel("Energy"r'$\longrightarrow$')
plt.xlabel("K Points"r'$\longrightarrow$')
plt.title("Net Contribution of p orbitals with Spin Orbit Coupling")
plt.xlim(0.25, 0.42)
plt.ylim(-2, 2)
plt.axhline(y = 0.0, linestyle = '--')
plt.axvline(x=0.336812861, marker ='*', markersize =0.5,alpha=0.2)
plt.legend()
plt.show()
