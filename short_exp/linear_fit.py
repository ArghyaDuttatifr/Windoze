import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
x = [0.0, 0.013, 0.027, 0.040]
y = [0.0, 50, 103, 153] # 10, not 9, so the fit isn't perfect
m, b, *_ = stats.linregress(x, y)
plt.axline(xy1=(0, 0), slope=m)




m, b = np.polyfit(x, y, deg=1)

#plt.axline(xy1=(0, 0), slope=m')
plt.legend()
plt.xlabel('Path difference(in $mm$)')
plt.ylabel('No. of fringes')
plt.title('Plot For Green LASER')
print ('The wavelenghth is' , 2/m, '$m$', b)
plt.scatter(x, y, color ='#88c999')
plt.show()