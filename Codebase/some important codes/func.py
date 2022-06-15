# Define the function

from cmath import exp
from init_val import y0, x0

# dy/dx
def func(y, x):
    return 3*y

# exact
def exact(y, x):
    return y0*exp(3*x)