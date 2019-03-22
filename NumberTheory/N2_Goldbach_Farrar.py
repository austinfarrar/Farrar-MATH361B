# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:57:27 2019

@author: Owner
"""
import numpy as np
num = 3
primenumbers = []

def prime_check(x):
    if x > 1:
        for ii in range(2,x):
            if x % ii == 0:
                return False
                break
        else:
            return True
    else:
        return False

while True:
    if prime_check(num):
        primenumbers.append(num)
    else:
        for ii in primenumbers:
            x = np.sqrt(((num-ii)/2))
            if x.is_integer() == True:
                break
        else:
            print('The first odd composite number to break the conjecture is', num)
            break
    num += 2

