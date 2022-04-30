# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:24:37 2022

@author: arghya
"""

from scipy.integrate import solve_ivp
import numpy as np

w = 2*np.pi/(24*60*60)
l = 8.5 * np.pi/180
g = -10

def rhs(a, v): 
    return [2*w*(v[1]*np.sin(l) - v[2]*np.cos(l)),-2*w*v[0]*np.sin(l), g+2*w*v[0]*np.cos(l)]

res = solve_ivp(rhs, (0, 0.1), [2, 3, 4])
print(res.y)