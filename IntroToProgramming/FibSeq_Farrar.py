# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:01:48 2019

@author: Owner
"""

N = 100
F0 = 0
F1 = 1
F2 = 1

fibonacci = [F0,F1]
cassini = [F1,F2]
for ii in range(N):
    fibonacci.append(fibonacci[ii] + fibonacci[ii+1])


for ii in range(N):
    cassini.append(fibonacci[ii]**2 - fibonacci[ii+1]*fibonacci[ii-1])

print('The last 10 terms of the sequence created are:',cassini[-10:])

