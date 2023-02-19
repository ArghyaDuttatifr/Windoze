
import numpy as np
from scipy.optimize import curve_fit
def test(x,a,b):
    return a+b*x^2
xdata=[0,3,7,10.5]
ydata=[0.001,0.01,0.022,0.045]
xdata=np.asarray(xdata)
ydata=np.asarray(ydata)
param, param_cov = curve_fit(test,xdata,ydata)
fit_a=param[0]