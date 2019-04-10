# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:04:41 2019

@author: Owner
"""

import numpy as np
from math import tan
N = 100
TOL = 10**(-4)
tol = 2
z0 = 100
itter = 0
Newton = np.zeros([0,2])

f_z = lambda x: tan(x)-x-2
g_z = lambda x: tan(x)*tan(x)

while tol > TOL and itter < N:
    z1 = z0 - (f_z(z0) / g_z(z0))
    tol = abs(z1 - z0)
    z0 = z1
    itter += 1
    Newton = np.vstack([Newton, np.array([z1,tol])])

print(Newton)
    