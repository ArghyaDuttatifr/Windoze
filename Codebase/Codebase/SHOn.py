from math import cos, exp, pi, sin, sqrt
from scipy.constants import hbar
import matplotlib.pyplot as plt
import numpy as np

from colors import *
from integration import *

# np.seterr(all = 'raise')

# mass, E
E = 0

# potential
def V(u, t):
    return -1/t

# derivative kernel
def kernel (u, t):
    psi_d = u[1]
    psi_d_d = (V(u,t)-E)*u[0]*2 # Schrodinger eqn

    return np.array([psi_d, psi_d_d])

# Integration routine
def Integrator(u0, t0, tf, N, kernel, routine, nNodes):
    h = (tf -t0)/N

    # initialise vars
    un = u0

    # initialise psi array
    psi_arr = [un[0]]

    # node counter
    nodes = 0
    # iterator
    for i in range (0, N):
        

        # Check for nodes
        try:
            un = routine(t0 + i*h, un, h, kernel)
            psi_arr.append(un[0])
            if (np.sign(psi_arr[i+1]) != np.sign(psi_arr[i]) and psi_arr[i] != 0):
                nodes += 1
                if (nodes > nNodes):
                    return [nodes], False
        except FloatingPointError:
            return [nodes], False

        
    if (nodes < nNodes):
        return [nodes], False

    return un, True

# Secant method for root finding
def secant(v1, v2, x1, x2, xf):
    return v1 + (xf - x1)*(v1 - v2)/(x1 - x2)

# Main Solver for Schrodinger eqn
def Solver(psi_0, psi_d_0, t0, tf, E1, E2, N, tol, nNodes):

    global E
    u0 = [psi_0, psi_d_0]

    E = E1
    u1, flag = Integrator(u0, t0, tf, N, kernel, rk4, nNodes)
    while(flag == False):
        print("here")
        x = 2 if nNodes > u1[0] else 1.5
        print(u1[0])
        input()
        E1 = E1*pow(x, nNodes - u1[0])
        E = E1
        u1, flag = Integrator(u0, t0, tf, N, kernel, rk4, nNodes)
    print(E)
    E = E2
    u2, flag = Integrator(u0, t0, tf, N, kernel, rk4, nNodes)
    while(flag == False):
        print("here")
        x = 2 if nNodes > u2[0] else 1.5
        print(x)
        E2 = E2*pow(x, nNodes - u2[0])
        E = E2
        u2, flag = Integrator(u0, t0, tf, N, kernel, rk4, nNodes)
    print(E)
    # luck check
    if (abs(u1[1] - 0) < tol):
        print(E)

    # iterator
    i=0

    # iteration loop
    while (i < 100):
        # exit condition
        if (abs(u2[0] - 0) < tol):
            # plt.plot(np.linspace(t0, tf, N+1), x2_arr, linewidth=1, color= blue)
            # plt.plot(np.linspace(t0, tf, N+1), y2_arr, linewidth=1, color= red)
            # plt.plot(x2_arr, y2_arr, linewidth=1, color= red)
            print(i)
            print(E)
            break
        else:
            Em = secant(E1, E2, u1[0], u2[0], 0)
            E1 = E2
            E2 = Em
            u1[0] = u2[0]
            print(E2)
            print(u2[0])
            input()
            E = E2
            u2, flag = Integrator(u0, t0, tf, N, kernel, rk4, nNodes)
            while(flag == False):
                x = 2 if nNodes > u2[0] else 1.5
                E2 = E2*pow(x, nNodes - u2[0])
                E = E2
                u2, flag = Integrator(u0, t0, tf, N, kernel, rk4, nNodes)
            i += 1


        
psi_0 = 0.
psi_d_0 = -0.00001
t0 = 8
tf = 0
tol = 1e-7
# E1, E2 should not be ratioed in powers of 2, 1.5
E1 = -0.13
E2 = -0.14
N = 1000

Solver(psi_0, psi_d_0, t0, tf, E1, E2, N, tol, 1)