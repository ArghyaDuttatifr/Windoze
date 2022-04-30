# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 18:53:45 2022

@author: arghy
"""
def func(yn,xn):
    # This is the right-hand side of the first-order ordinary differential 
    # equation dx/dt = fun.
#    func = 3*t**2 
    func = xn**2 +yn
    return func
def Adaptive(x0, y0, func, integrator, xf, N, exact ):
    eps0 = 1e-9
    eps = eps0/N
    s = 0.9
    h = (xf - x0)/N
    yn = y0
    xn = x0
    while(xn < xf):
        
        y1 = integrator(xn, yn, h, func)
        y2i = integrator(xn, yn, h/2, func)
        y2 = integrator(xn + h/2, y2i, h/2, func)

        delta = abs(y2 - y1)
        if (delta <= eps):
            yn = (16*y2 - y1)/15
            xn = xn + h
            h = s*h*pow((eps/delta),1/4)
        else:
            h = s*h*pow((eps/delta),1/5)
            y1 = integrator(xn, yn, h, func)
            y2i = integrator(xn, yn, h/2, func)
            y2 = integrator(xn + h/2, y2i, h/2, func)
            yn = (16*y2 - y1)/15
            xn = xn + h


        error = abs(exact(yn, xn) - yn)
        return error

print ( error)

