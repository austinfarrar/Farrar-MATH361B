# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:18:14 2019

@author: Owner
"""

import numpy as np

N = 10000
x = np.zeros((10))

list1 = []
list2 = []
list3 = []
prod1= 1
prod2 = 1
prod3 = 1

for ii in range(2,N):
    P_n = ((ii**3 - 1 ) / (ii**3 + 1))
    prod1 *= P_n
    list1.append(prod1)

print('The first 15 terms of P_n are', list1[:15])
print('The last 15 terms of P_n are', list1[-15:])
print()    

for ii in range(1,N):
    Q_n = ((np.exp(ii/100)) / (ii**10))
    prod2 *= Q_n
    list2.append(prod2)
print('The first 15 terms of Q_n are', list2[:15])  
print('The last 15 terms of Q_n are', list2[-15:])
print()

for ii in range(N):
    A_n = ((ii**2 + 6) / (np.exp(ii + 1)))
    prod3 *= A_n
    list3.append(prod3)
print('The first 15 terms of A_n are', list3[:15])
print('The last 15 terms of A_n are', list3[-15:])  