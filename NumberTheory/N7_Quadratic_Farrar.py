# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:02:39 2019

@author: Owner
"""
import numpy as np

def prime_check(x):
    if x > 1:
        for ii in range(2,x):
            if x % ii == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
m = 200
count_array = np.zeros([0,2])
neg_one = np.zeros([0,2])

for ii in range(0,m):
    if prime_check(ii):
        quads = []
        
        appears = 'False'
        for jj in range(0,ii):
            num = (jj**2)%ii
            quads.append(num)
            
            if (ii - 1) == num:
                appears = 'True'
            
        quads = set(quads)
        count = len(quads)
        count_array = np.vstack([count_array,np.array([ii,count])])
        neg_one = np.vstack([neg_one,np.array([ii,appears])])
        
print(count_array)
print(neg_one)