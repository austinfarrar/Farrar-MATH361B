# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:04:22 2019

@author: Owner
"""

def divide(p1,p2):
    ratio = (p1[-1]/p2[-1])
    deg = (len(p1)-len(p2))
    term = [0]*(deg + 1)
    term[deg] = ratio
    return term

def addition(p1,p2):
    if len(p1) > len(p2):
        add = list(p1)
        for ii in range(len(p2)):
            add[ii] = p1[ii]+p2[ii]
    else:
        add = list(p2)
        for jj in range(len(p1)):
            add[jj] = p1[jj]+p2[jj]
    return add

def subtraction(r,g):
    if len(r) > len(g):
        subtract = list(r)
        for ii in range(len(g)):
            subtract[ii] = r[ii]-g[ii]
    else:
        subtract = [0]*len(g)
        for ii in range(len(r)):
            subtract[ii] = r[ii]-g[ii]
        for jj in range(len(r),len(g)):
            subtract[jj] = 0-g[jj]
    return subtract
    
def multiply(r, ratio):
    multi = [0]*(len(r)+len(ratio)-1)
    last = ratio[-1]
    for ii in range(len(r)):
        index = ii + len(ratio)-1
        multi[index] = last*r[ii]
    return multi

import numpy as np
#Erase high degree terms that are now zero
# Assumed that highest degree of p is last element of list
def clean_poly(p):
    highest_deg = len(p) - 1   
    for ii in range(len(p)-1,-1,-1):
#        print('highest', highest_deg)
#        print('pii', p[ii])
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1
    del p[highest_deg+1:]
    return p

def poly(f,g):
    q = [0]
    r = f
    while r != 0 and len(g) <= len(r):
        L = divide(r,g)
        q = addition(q,L)
        rL = multiply(g,L)
        r = subtraction(r,rL)
        clean_poly(r)
    return q,r

f = [7,6,5,4] #x^3-1
print(f)
g = [1,3] #2x - 1
print(g)


q, r = poly(f,g)
print(q)
print(r)

        