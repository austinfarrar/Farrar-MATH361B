# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:02:49 2019

@author: Owner
"""


divisors = []

def divide(n):
    for ii in range(1,n):
        if n % ii == 0:
            divisors.append(ii)

    print('n =', n)
    print('the divisors are',divisors)

divide(10)