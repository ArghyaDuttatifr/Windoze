import numpy as np

D=0.003
vo=19.44
m=0.45
g=9.8
def f(t,y,p):
	return np.array([p[0],p[1]])

def g(t,y,p):
	ddx=-(D*np.sqrt((p[0]*p[0])+(p[1]*p[1]))*p[0])/m
	ddy=-((D*np.sqrt((p[0]*p[0])+(p[1]*p[1]))*p[1])/m)-9.8
	return np.array([ddx,ddy])

def rk4(t,y,theta,h,vo):
    p=[vo*np.cos(theta),vo*np.sin(theta)]
    for i in range(1000000000):
        y1=y
        m1=f(t,y,p)
        k1=g(t,y,p)
        m2=f(t+0.5*h,y+0.5*h*m1,p+0.5*h*k1)
        k2=g(t+0.5*h,y+0.5*h*m1,p+0.5*h*k1)
        m3=f(t+0.5*h,y+0.5*h*m2,p+0.5*h*k2)
        k3=g(t+0.5*h,y+0.5*h*m2,p+0.5*h*k2)
        m4=f(t+h,y+h*m3,p+h*k3)
        k4=g(t+h,y+h*m3,p+h*k3)
        y=y+(h*(m1+2*m2+2*m3+m4))/6
        p=p+(h*(k1+2*k2+2*k3+k4))/6
        t=t+h
        if y[0]>=22.255:
            return y[1]
            break

y=np.array([0,0])
#theta_1=np.pi/4
theta_1=0.2617
theta_2=np.pi/6
t=0
h=0.01  
u1=rk4(t,y,theta_1,h,vo)
u2=rk4(t,y,theta_2,h,vo)


def secant(theta_1,theta_2,uf,u1,u2):     #secant method definition
	return theta_1+(uf-u1)*(theta_2-theta_1)/(u2-u1) 

i=0
while i<100:
    if np.abs(u2-2.14)<0.00001:
   # if u2<2.14001 and u2>2.13999 :
        print("the value of angle is ")
        print(theta_2*180/np.pi)
        break
    else:
        theta_f=secant(theta_1,theta_2,2.14,u1,u2)
        theta_1=theta_2
        theta_2=theta_f
        u1=u2
        u2=rk4(t,y,theta_2,h,vo)
    i=i+1    