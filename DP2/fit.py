import numpy as np
from scipy.optimize import curve_fit

# Define the model function
def model_func(I, a, b):
    return a**2 * (I**2 - b**2)**(0.5)

# Generate some example data
I_data = np.linspace(-1.2, 1.2, num=21)
V_data = np.array([0.0, 0.4, 0.7, 0.9, 1.0, 1.1, 1.1, 1.0, 0.9, 0.7, 0.4,
                   0.0, -0.4, -0.7, -0.9, -1.0, -1.1, -1.1, -1.0, -0.9, -0.7])

# Fit the model to the data
popt, pcov = curve_fit(model_func, I_data, V_data)

# Print the parameter values
a_fit, b_fit = popt
print(f"Fitted parameters: a = {a_fit}, b = {b_fit}")
import matplotlib.pyplot as plt

# Define the range of I values to plot
I_range = np.linspace(-1.2, 1.2, num=100)

# Compute the model predictions using the fitted parameters
V_fit = model_func(I_range, a_fit, b_fit)

# Plot the experimental data and the fitted model

plt.plot(I_range, V_fit, label='Fitted model')
plt.show()