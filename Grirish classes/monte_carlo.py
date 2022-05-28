#%%
#area of circle 
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

n= 1000
  
circle_points= 0
square_points= 0
# Total random numbers generated = possible x
# values* possible y values

for i in range(n):
    # np.randomly generated x and y values from a
    # uniform distribution
    rand_x = np.random.uniform(-1, 1)
    rand_y = np.random.uniform(-1, 1)
  
    # Distance between (x, y) from the origin
    R = rand_x**2 + rand_y**2
    theta = np.linspace(0, 2* np.pi , 200)
    a= np.cos(theta)
    b= np.sin(theta)
  
    # Checking if (x, y) lies inside the circle
    if R <= 1:
        circle_points += 1
        
        plt.scatter(rand_x, rand_y)
    else:

        plt.scatter(rand_x, rand_y, marker='*')
    square_points += 1
    area = circle_points/ square_points
    plt.plot(a, b)
   # plt.Circle((0, 0), 1,color='g' ,fill= False)
      
print("Final Estimation of area =", 4 * area )

plt.show()
#%%
'''
#area of any curve 
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return x** np.cos(x) + 2 #np.sqrt(1-x**2)
def g(x):
    return np.sin(x)/x

def definite_integral_show(f, x0, x1, n):

    x = np.arange(x0, x1, 0.01)
    y = f(x)
    f_max = max(y)

    x_rand = x0 + np.random.random(n)*(x1-x0)
    y_rand = 0 +  np.random.random(n)*(f_max)
    #y_rand = -0.3 +  np.random.random(n)*(f_max+0.3)
    

    pt_below = np.where(y_rand < f(x_rand))
    pt_above = np.where(y_rand >= f(x_rand))
    plt.plot(x, y, color = "red")
    plt.scatter(x_rand[pt_below], y_rand[pt_below], color = "green", vmin=-0.1, vmax=1.1, lw=0, s=5)
    plt.scatter(x_rand[pt_above], y_rand[pt_above], color = "blue", vmin=-0.1, vmax=1.1, lw=0, s=5)
    ave = len(pt_below[0])/n
    print("number of pts above the curve:", len(pt_above[0]))
    print("number of pts below the curve:", len(pt_below[0]))
    print("n. below/n.total:", ave)
    print("Rectangle area:", f_max*(x1-x0)) #(0.3+f_max*(x1-x0))
    print("Area under the curve:", f_max*(x1-x0)*ave)#(0.3+f_max*(x1-x0))
    




    return x_rand, y_rand, f_max
#x_rand , y_rand, f_max = definite_integral_show(f1, 0, 20, 15000)
x_rand , y_rand, f_max = definite_integral_show(g, 0.1, 20, 15000)
plt.show()


'''










# %%
