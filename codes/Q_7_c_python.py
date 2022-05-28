# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:17:53 2022

@author: arghy
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv

def main() :
    x =np.random.rand(50000)
    
    y_gaussian =np.zeros(len(x))
    sigma= 100
    
    y_gaussian = sigma*np.sqrt(sigma)* erfinv(2*x -1)
    plt.hist(y_gaussian)
    plt.title(" Histogram of gaussian distribution ", color='b') 
    plt.ylabel("total counts", color='r')
    plt.xlabel("Values" )
    plt.grid()
    plt.legends()
    plt.show()
if __name__=="__main__":
    main()
