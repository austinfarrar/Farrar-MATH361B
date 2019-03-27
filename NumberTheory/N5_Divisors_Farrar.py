# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:02:49 2019

@author: Owner
"""


divisors = []

def divide(n):
    for ii in range(1,n+1):
        if n % ii == 0:
            divisors.append(ii)


    print('the divisors of {} are {}'.format(ii,divisors))

divide(100)