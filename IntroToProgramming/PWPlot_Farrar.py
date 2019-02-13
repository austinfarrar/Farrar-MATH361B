# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:40:06 2019

@author: Owner
"""

import matplotlib.pyplot as plt
import numpy as np
import math

N = 10000

x = np.linspace(-3,3,N)


def f(x):
    if x.any() < -2:
        return -3*(x+2)**2 + 1
    elif -2 <= x.any() and x.any() < -1:
        return 1
    elif -1 <= x.any() and x.any() <= 1:
        return (x-1)**3 + 3
    elif 1 < x.any() and x.any() < 2:
        return np.sin(math.pi*x) + 3
    else:
        3*math.sqrt(x-2) + 4

y = f(x)
plt.plot(x,y)
plt.title('Piecewise Function')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show


        


