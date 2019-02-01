# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:25:55 2019

@author: Owner
"""

x = 1
y = 2
z = 3
mylist = []

comp1 = x + y
mylist.append(comp1)
comp2 = (y * z) + (3 * x)
mylist.append(comp2)
comp3 = (comp1)**2
mylist.append(comp3)
comp4 = (2 * comp2 - .5 * x)/ comp1
mylist.append(comp4)
comp5 = 7 % 3
mylist.append(comp5)
print(mylist)

mylist.insert(2, comp3 + 3)
mylist.remove(comp3)
print(mylist)

mylist.insert(4, comp5 * (3/4))
mylist.remove(comp5)
print(mylist)

print(sum(mylist))
