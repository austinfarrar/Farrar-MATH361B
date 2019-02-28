# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:44:28 2019

@author: Owner
"""

import numpy as np

N = 50

#list1 = []
#prod1= 1
#a_n = lambda n: n**2 + 9*n - 7
#
#for ii in range(1,N):
#    parprod = a_n(ii)
#    prod1 *= parprod
#    list1.append(prod1)
#
#print('The first 15 terms of the a_n sequence are', list1[:15])
#print('The last 15 terms of the a_n sequence are', list1[-15:])
#print()

list2 = []
prod2 = 1
f_n = lambda n: n**3 + 1.0
g_n = lambda n: n**2 + 1

for ii in range(1,N):
    b_n = 1 + (f_n(ii) / g_n(ii))
    prod2 *= b_n
    list2.append(b_n)

print('The first 15 terms of the b_n sequence are', list2[:15])
print()
print('The last 15 terms of the b_n sequence are', list2[-15:])
print()
print()

list3 = []
prod3 = 1
b = 2

for ii in range(1,N):
    c_n = 1 + b**ii
    prod3 *= c_n
    list3.append(c_n)

print('The first 15 terms of the c_n sequence are', list3[:15])
print()
print('The last 15 terms of the c_n sequence are', list3[-15:])