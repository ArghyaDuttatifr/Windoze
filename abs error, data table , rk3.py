# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:12:00 2022

@author: arghy
"""
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('seaborn')

# define equations

def dydt(t, y):
	return np.sin(t)**2*y
def f(t):
	return 2*np.exp(0.5*(t-np.sin(t)*np.cos(t)))
#dy/dt = sin2(theta) * y    , y = func

def RK3(t, y, h):
	# compute approximations
	k_1 = dydt(t, y)
	k_2 = dydt(t+h/2, y+(h/2)*k_1)
	k_3 = dydt(t+h/2, y+h*(-k_1 + 2*k_2))

	# calculate new y estimate
	y = y + h * (1/6) * (k_1 + 4 * k_2 + k_3)
	return y


def RK4(t, y, h):
	# compute approximations
	k_1 = dydt(t, y)
	k_2 = dydt(t+h/2, y+(h/2)*k_1)
	k_3 = dydt(t+h/2, y+(h/2)*k_2)
	k_4 = dydt(t+h, y+h*k_3)

	# calculate new .y estimate
	y = y + h * (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
	return y


# Initialization
ti = 0
tf = 5
h = 0.1
n = int((tf-ti)/h)
t = 0
y = 2
y_rk3 = 2

print("t \ \t\t yRK4 \t\t f(t)")



t_plot = []
y_RK3 = []
y_RK4 = []
y_analytical = []


##
for i in range(1, n+1):
	t_plot.append(t)
	y_RK4.append(y)
	y_RK3.append(y_rk3)
	y_analytical.append(f(t))

	# calculate new y estimate
	y = RK4(t, y, h)
	y_rk3 = RK3(t, y_rk3, h)

	t += h
	print(f"{t:.1f} \t\t {y:4f} \t\t {f(t):.4f}")


t_plot.append(t)
y_RK3.append(y_rk3)
y_RK4.append(y)
y_analytical.append(f(t))


# Visualization
fig, (ax, ax2) = plt.subplots(2, 1)
ax.plot(t_plot, y_analytical, 'ro', label='Analytical solution')
ax.plot(t_plot, y_RK4, '.b', label='Fourth-order Runge-Kutta estimate')
ax.plot(t_plot, y_RK3, '.g', label='Third-order Runge-Kutta estimate')
ax.set_ylabel("y", fontsize=18)
ax.legend()

ax2.plot(t_plot, np.abs(np.array(y_analytical) - np.array(y_RK4)), '.-b', label='Fourth-order Runge-Kutta')
ax2.plot(t_plot, np.abs(np.array(y_analytical) - np.array(y_RK3)), '.-g', label='Third-order Runge-Kutta')
ax2.set_ylabel("Abs Error", fontsize=18)
ax2.legend()
ax2.set_xlabel("t", fontsize=18)
plt.savefig('runge_kutta_analytical.png', dpi=300, bbox_inches='tight')





#%%
#dy1/dt = y2 &dy2/dt= -ty2+ 2*y1 /t
import numpy as np
import matplotlib.pyplot as plt


# Runge-Kutta (RK4) Numerical Integration for System of First-Order Differential Equations


def ode_system(_t, _y):
	"""
	system of first order differential equations
	_t: discrete time step value
	_y: state vector [y1, y2]
	"""
	return np.array([_y[1], -_t * _y[1] + (2 / _t) * _y[0]])


def rk4(func, tk, _yk, _dt=0.01):

	# evaluate derivative at several stages within time interval
	f1 = func(tk, _yk)
	f2 = func(tk + _dt / 2, _yk + (f1 * (_dt / 2)))
	f3 = func(tk + _dt / 2, _yk + (f2 * (_dt / 2)))
	f4 = func(tk + _dt, _yk + (f3 * _dt))

	# return an average of the derivative over tk, tk + dt
	return _yk + (_dt / 6) * (f1 + (2 * f2) + (2 * f3) + f4)


# ==============================================================
# simulation harness

dt = 0.01
time = np.arange(1.0, 4.0 + dt, dt)

# second order system initial conditions [y1, y2] at t = 1
y0 = np.array([0, 1])

# ==============================================================
# propagate state

# simulation results
state_history = []

# initialize yk
yk = y0

# intialize time
t = 0

# approximate y at time t
for t in time:
	state_history.append(yk)
	yk = rk4(ode_system, t, yk, dt)

# convert list to numpy array
state_history = np.array(state_history)

print(f'y evaluated at time t = {t} seconds: {yk[0]}')

# ==============================================================
# plot history

fig, ax = plt.subplots()
ax.plot(time, state_history[:, 0])
ax.plot(time, state_history[:, 1])
ax.set(xlabel='t', ylabel='[Y]', title='Second Order System Propagation')
plt.legend(['y1', 'y2'])
ax.grid()
plt.show()

