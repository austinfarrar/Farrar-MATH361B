# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:00:35 2019

@author: Owner
"""

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

numprimes = 20 #number of primes being checked
plist = []
check = 2 #number being checked first

while len(plist) < numprimes:
    prime = False
    while prime == False:
        prime = prime_check(check)
        check += 1
    
    plist.append(check - 1)

print('Here is a list of the first {} primes: {}'.format(numprimes, plist))