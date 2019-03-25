# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:56:50 2019

@author: Owner
"""

m = 7
inverse = []

for ii in range(1,m):
    for jj in range(1,m):
        if (ii * jj) % m == 1:
            inverse.append([ii,jj])

print('The elements with inverses and their inverses are:', inverse)