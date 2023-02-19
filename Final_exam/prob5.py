import numpy as np
import math as m

def func(x,y):
    return m.sqrt(4-x**2-y**2)

def I_mid_2D(xi,xf,yi,yf,nx,ny):
    hx=(xf-xi)/nx
    hy=(yf-yi)/ny
    x=np.linspace(xi,xf,(nx+1))
    y=np.linspace(yi,yf,(ny+1))
    x_mid=(x[1:]+x[:nx])/2
    y_mid=(y[1:]+y[:ny])/2
    integration=0
    for i in range (nx):
        for j in range (ny):
            integration+=func(x_mid[i],y_mid[j])
    integration*=hx*hy
    return integration 
print(4*I_mid_2D(0,1,0,1,100,100))

 
