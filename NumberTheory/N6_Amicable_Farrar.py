# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:58:28 2019

@author: Owner
"""


def divide(n):
    divisors = []
    for ii in range(1,n):
        if n % ii == 0:
            divisors.append(ii)
    
    return divisors
          

N = 10000
amicable = []

for ii in range(N):
    b = sum(divide(ii))
    if sum(divide(b))== ii and ii != b:
        amicable.append(ii)
    

print('The amicable numbers up to', N ,'are', amicable) 
