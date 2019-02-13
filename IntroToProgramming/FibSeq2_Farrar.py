# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:13:46 2019

@author: Owner
"""

N = 10000
F0 = 0
F1 = 1
m = 3

my_list = [F0,F1]
multiples = []

for ii in range(N):
    my_list.append(my_list[ii] + my_list[ii+1])

for ii in my_list:
    if ii % m == 0:
        multiples.append(ii)
    
    
#print(multiples)
#print(len(multiples))

