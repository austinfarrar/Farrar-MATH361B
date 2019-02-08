# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:42:24 2019

@author: Owner
"""

import numpy as np

N = 10000
x = np.zeros((10))

list1 = []
list2 = []
list3 = []
sum1 = 0
sum2 = 0
sum3 = 0

for ii in range(1,N):
    s_n = (np.log((ii**4)+ii+3))/((np.sqrt(ii))+3)
    sum1 += s_n
    list1.append(sum1)
    
    t_n = (np.exp(ii/100)/ii**10)
    sum2 += t_n
    list2.append(sum2)
    
    a_n = (((ii+7) + 3^ii)/((np.exp(ii+4))))
    sum3 += a_n
    list3.append(sum3)
    
    
print('The first 15 terms of the S_n sequence are', list1[:15])
print('The last 15 terms of the S_n sequence are', list1[-15:])
print()
print('The first 15 terms of the T_n sequence are', list2[:15])
print('The last 15 terms of the T_n sequence are', list2[-15:])
print()
print('The first 15 terms of the A_n sequence are', list3[:15])
print('The last 15 terms of the A_n sequence are', list3[-15:])

