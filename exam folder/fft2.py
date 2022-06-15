'''import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-x**2)
def fft(x):
    return (1/np.sqrt(2))*np.exp(-(x*2)/4)
xmax=50
xmin=-50
numpoints=256
dx=(xmax-xmin)/(numpoints-1)
sampled_data=np.zeros(numpoints)
xarr=np.zeros(numpoints)
for i in range(numpoints):
    sampled_data[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
nft=np.fft.fft(sampled_data,norm='ortho')
karr=np.fft.fftfreq(numpoints,d=dx)
karr=2*np.pi*karr
factor=np.exp(-1j*karr*xmin)

aft=dx*np.sqrt(numpoints/(2.0*np.pi))*factor*nft
fig, ax =plt.subplots(1,2)
ax[1].plot(karr,np.real(aft),'r.')
k_points=np.linspace(-5,5,100)
x_points=np.linspace(-6,6,100)
ax[1].plot(k_points,fft(k_points),c='b',alpha=0.4)
ax[1].set_xlim([-6,6])
ax[1].set_ylim([0,1])
ax[0].plot(xarr,sampled_data,'r.')
ax[0].plot(x_points,f(x_points),c='b',alpha=0.4)
plt.show()'''
import numpy as np 
x = np.log(2)
print (np.sin(-x))


