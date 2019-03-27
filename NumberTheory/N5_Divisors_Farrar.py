# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:02:49 2019

@author: Owner
"""


def divide(n):
    divisors = []
    for ii in range(1,n):
        if n % ii == 0:
            divisors.append(ii)
    return divisors

print(divide(100))