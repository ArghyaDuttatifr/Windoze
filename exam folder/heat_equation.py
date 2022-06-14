
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import random
import numpy as np


#defining the required constants
l = 50                             # lenght of the plate
t = 500                            # maximum iteration time

x = 2
y = 1

delta_t = (y ** 2)/(4 * x)
gamma = (x * delta_t) / (y ** 2)


u = np.empty((t, l, l))


# defining the boundary conditions
utop = 100.0
uleft = 0.0
ubottom = 0.0
uright = 0.0

# putting the initial condition
u.fill(0.0)

u[:, (l-1):, :] = utop
u[:, :, :1] = uleft
u[:, :1, 1:] = ubottom
u[:, :, (l-1):] = uright


# solving for u
def calculate(u):
    for k in range(0, t-1, 1):
        for i in range(1, l-1, y):
            for j in range(1, l-1, y):
                u[k + 1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]

    return u

# making the plot
def plotheatmap(u_k, k):
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()

    return plt

u = calculate(u)

# making the animation
def animate(k):
    plotheatmap(u[k], k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=t, repeat=False)
anim.save("heateq_sol_1.gif")



# Initializing solution for the second case: the grid of u(k, i, j)
u =np.random.rand(t, l, l)*100.0



# defining the boundary conditions for the second case
utop = 100.0
uleft = 100.0
ubottom = 0.0
uright = 0.0


# defining the initial conditions for the boundary
u[:, (l-1):, :] = utop
u[:, :, :1] = uleft
u[:, :1, 1:] = ubottom
u[:, :, (l-1):] = uright


u = calculate(u)

def animate(k):
    plotheatmap(u[k], k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=t, repeat=False)
anim.save("heateq_sol_2.gif")
plt.show()
'''



import numpy as np
import scipy 
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import matplotlib
import matplotlib.pylab as plt
import time
from math import sinh

#import matplotlib.pyplot as plt

# Change some default values to make plots more readable on the screen
LNWDT=2; FNT=15
plt.rcParams['lines.linewidth'] = LNWDT; plt.rcParams['font.size'] = FNT

# Set temperature at the top
Ttop=100
Tbottom=10
Tleft=0.0
Tright=0.0

xmax=1.0
ymax=1.5
 
# Set simulation parameters
#need hx=(1/nx)=hy=(1.5/ny)

Nx = 20
h=xmax/Nx
Ny = int(ymax/h)

nx = Nx-1
ny = Ny-1
n = (nx)*(ny)            #number of unknowns
print(n, nx, ny)

d = np.ones(n) # diagonals
b = np.zeros(n) #RHS
d0 = d*-4
d1 = d[0:-1]
d5 = d[0:-ny]

A = scipy.sparse.diags([d0, d1, d1, d5, d5], [0, 1, -1, ny, -ny], format='csc')

#alternatively (scalar broadcasting version:)
#A = scipy.sparse.diags([1, 1, -4, 1, 1] , [-5, -1, 0, 1, 5], shape=(15, 15)).toarray()

# set elements to zero in A matrix where BC are imposed
for k in range(1,nx):
    j = k*(ny)
    i = j - 1
    A[i, j], A[j, i] = 0, 0
    b[i] = -Ttop

b[-ny:]+=-Tright       #set the last ny elements to -Tright       
b[-1]+=-Ttop           #set the last element to -Ttop
b[0:ny-1]+=-Tleft      #set the first ny elements to -Tleft 
b[0::ny]+=-Tbottom     #set every ny-th element to -Tbottom

tic=time.time()
theta = scipy.sparse.linalg.spsolve(A,b)                    #theta=sc.linalg.solve_triangular(A,d)
toc=time.time()
print('sparse solver time:',toc-tic)
 
tic=time.time()
theta2=scipy.linalg.solve(A.toarray(),b)
toc=time.time()
print('linalg solver time:',toc-tic)

# surfaceplot:
x = np.linspace(0, xmax, Nx + 1)
y = np.linspace(0, ymax, Ny + 1)

X, Y = np.meshgrid(x, y)

T = np.zeros_like(X)


# set the imposed boudary values
T[-1,:] = Ttop
T[0,:] = Tbottom
T[:,0] = Tleft
T[:,-1] = Tright


for j in range(1,ny+1):
    for i in range(1, nx + 1):
        T[j, i] = theta[j + (i-1)*ny - 1]

    
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, T, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(0, Ttop+10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T [$^o$C]')


nx=4
xticks=np.linspace(0.0,xmax,nx+1)
ax.set_xticks(xticks)

ny=8
yticks=np.linspace(0.0,ymax,ny+1)
ax.set_yticks(yticks)

nTicks=5
dT=int(Ttop/nTicks)
Tticklist=list(range(0,Ttop+1,dT))
ax.set_zticks(Tticklist)

#fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
'''
#https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/