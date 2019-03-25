# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:26:06 2019

@author: Owner
"""

m = 7
zeros = []

for ii in range(1,m):
    for jj in range(1,m):
        if (ii + jj) % m == 0:
            zeros.append([ii,jj])
            
print('The zero divisors are:', zeros)
            