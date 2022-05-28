
import numpy as np
import matplotlib.pyplot as plt
def cauchy_dist(x):
    return (B /np.pi)*(1/( x**2 + B**2))

a =np.random.rand(5000)

int_val=[]

B =float(input("Enter value of a = "))
x_vals = np.linspace(-20*B ,20*B , 100)

if ( B<0):
    print("Error: a is out of the range.")
else:
    for i in range(0,len(a)):
        const =np.tan(np.pi*(a[i]- 0.5))
        int_val.append(B *const )
n, bin, patches = plt.hist(int_val, bins = x_vals, facecolor='blue',density=True, alpha=0.7)
plt.ylabel("Total counts")
plt.xlabel("Value")

plt.title("Histogram of Cauchy distribution with $a=$"+str(B))


