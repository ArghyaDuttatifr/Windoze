#Q1
import numpy as np
import matplotlib.pyplot as plt

n =20
h = (np.log(2)) / n
x = np.linspace(-np.log(2), 0, n+1)
    # Get A
A = np.zeros((n+1, n+1))
A[0, 0] = 1                    #because of boundary condition
A[n, n] = 1
   
for i in range(1, n):
    A[i, i-1] = 1
    A[i, i] = -2-2*h**2
    A[i, i+1] = 1

    # Get b
b = np.zeros(n+1)

b[1:-1] = h**2* np.sin(-x[i]*np.pi/180)
b[-1] = 0
b[-1:]= -np.log(2)
print(b)
y = np.linalg.solve(A,b)
print(y)
#for plot
t = np.linspace(0, 5, 21)

plt.figure(figsize=(10,8))
plt.title('Time vs solution of y')
plt.grid()
plt.xlabel('Time (t)')
plt.ylabel('y')
plt.plot(t, y)

plt.show()