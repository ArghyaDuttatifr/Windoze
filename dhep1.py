from turtle import color
import numpy as np
import matplotlib.pyplot as plt
  
# x axis values
x = [1074,1168,1277,1386,1485,1520,1594]
# corresponding y axis values
y = [0,np.log(10),np.log(122),986,2069,2925,2033]
  

  
# plotting the points 
plt.plot(x, y, '-',color='r')
plt.scatter(x,y, c='g')
  
# naming the x axis
plt.xlabel('High Voltage')
# naming the y axis
plt.ylabel('Efficiency')
plt.axhline(y=1, alpha=0.3)
plt.grid(alpha=0.5)
plt.title('Efficiency of Paddle 4')
  
plt.show()