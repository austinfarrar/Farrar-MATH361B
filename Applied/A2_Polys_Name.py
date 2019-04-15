# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:57:35 2019

@author: Owner
"""

p = [1,2,3] #x^2 + 2x + 3
d = []
c = 2
a = 1
b = 2

#each program must be run by themselves otherwise it will not work
def polynomial(p,c):
    poly = p
    ex = len(poly)-1
    for ii in range(0,len(p)):
        poly[ii] = poly[ii] *c ** ex
        ex = ex - 1
    print(sum(poly))
   


def derivative(p,c):
    deri = p
    k = len(deri) - 1
    for ii in range(0,len(p)):
        deri[ii] = (deri[ii]* k)*c ** (k-1)
        k = k - 1
    print(sum(deri))
    


def integral(p):
    integ = p
    j = len(integ)-1
    for ii in range(0,len(p)):
        integ[ii] = (((integ[ii]/2)* b) **(j+1))
        -((integ[ii]/2)* a **(j+1))
        j = j -1
    print(integ)
    print(sum(integ))
