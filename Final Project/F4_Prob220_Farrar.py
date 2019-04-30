# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:03:37 2019

@author: Owner
"""
import matplotlib.pyplot as plt

def string(N):
   a = "aRbFR"
   b = "LFaLb"
   D0 = "Fa"
   for ii in range(N):
      for jj in range(len(D0) - 1,-1,-1):
         if D0[jj] == "a":
            D0 = D0[:jj] + a + D0[jj+1:]
         elif D0[jj] == "b":
            D0 = D0[:jj] + b + D0[jj+1:]
#   print(D0)
   return D0

#turns the string into coordinates and changes
#coordinate direction
def coords(s):
   p = 90
   x = [0]
   y = [0]
   for ii in s :
      if ii == "a" or ii == "b": 
          continue
      elif ii == "L":
         p += 90
         p = norm(p)
      elif ii == "R":
         p -= 90
         p = norm(p)
      elif ii == "F":
         if p == 0:
            x.append(x[-1] + 1)
            y.append(y[-1])
         elif p == 90:
            x.append(x[-1])
            y.append(y[-1] + 1)
         elif p == 180:
            x.append(x[-1] - 1)
            y.append(y[-1])
         elif p == 270:
            x.append(x[-1])
            y.append(y[-1] - 1)
   return x, y

#normalizes the left and right turning in the 
#coords function
def norm(x):
   while x >= 360: 
       x -= 360
   while x < 0: 
       x += 360
   return x

#plot function
def plot(coord):
    plt.plot(coord[0],coord[1])
    plt.title('Heighway Dragon')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.show()


N = 10
plot(coords(string(N)))