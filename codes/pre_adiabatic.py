# Importing packages:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importing the data files:
df = pd.DataFrame(pd.read_excel (r"C:\Users\Priyanka\Downloads\g_wsoc00_prim_weight.xlsx"))
#df = pd.DataFrame(pd.read_excel (r"C:\Users\Priyanka\Downloads\g_wsoc100_prim_weight.xlsx"))

k = df ["k"]
E = df ["E"]
w = df ["w"]

# Plotting the E-k diagram
plt.plot(k,E, linewidth=0.3)
plt.xlabel("k"r'$\longrightarrow$')
plt.ylabel("E"r'$\longrightarrow$')
plt.xlim(0,0.4)
plt.ylim(-2,2)
plt.title("Band diagram for a $Bi_2Se_3$ Primitive Cell without Spin-Orbit Coupling")
s = [70**w[n] for n in range(len(w))]

# Assigning weights of the E-k points
plt.scatter(k, E, s=s, c=df.w, cmap='rainbow_r')
plt.colorbar()
plt.show()