import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 
def func(t, x):
    h,v = x
    dhdt = 98.0 * h + 198.0 * v
    
    dvdt = -99.0 *h -199.0 *v
    
    return [dhdt, dvdt]


t_span = [0.0, 2.0]

x0 = [1.0 , 0.0]

result = solve_ivp( func , t_span, x0)

h = result.y[0]
v = result.y[1]
t = result.t
plt.plot(t, h)
plt.plot(t, v)
plt.grid()
plt.minorticks_on()
plt.xlabel("t")
plt.ylabel("h/v")
plt.legend(['healthy', 'infected'])
