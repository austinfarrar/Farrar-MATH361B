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
catalan = [F1,F2]
for ii in range(N):
    fibonacci.append(fibonacci[ii] + fibonacci[ii+1])

for ii in range(N):
    catalan.append(catalan[ii]**2 - catalan[ii+1]*catalan[ii-1])

print('The last 10 terms of the sequence created are:',catalan[-10:])

