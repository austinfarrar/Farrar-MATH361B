# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:02:44 2019

@author: Owner
"""

a0 = 600
N = 200

collatz = [a0]
itter = 1

for ii in range(N):
    if a0 % 2 == 0:
        a0 = a0 / 2
    else:
        a0 = (3 * a0) + 1
    collatz.append(a0)
    
    if a0 == 1:
        itter += 1
        break
    else:
        itter += 1
print(collatz)
print('It took', itter  ,'terms')