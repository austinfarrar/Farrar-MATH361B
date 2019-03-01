# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:05:06 2019

@author: Owner
"""

import numpy as np
import math

my_array = np.zeros([0,4])

#my_array = np.vstack( [my_array, np.array( ['a','b','c','a+b+c'] )] )

for ii in range(1,450):
    for jj in range(ii,450):
        c = math.sqrt(ii**2 + jj**2)
        if c.is_integer() == True:
            my_array = np.vstack ( [my_array, np.array( [ii, jj, c, ii+jj+c])])
            break
print("The Pythagorean Triple is:", my_array[np.where(my_array[:,3]==1026)])