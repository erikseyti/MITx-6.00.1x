# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:22:14 2017

@author: sey_t
"""

def a(x):
   '''
   x: int or float.
   '''
   print(x)
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2     
   

#x=-5.3
#z = a(x)

#y = a(a(a(6)))

#print(y)
#print(type(y))

#w = c(a(1),b(1))
#print(w)
#print(type(w))

#r= d('apple',11.1)
#print(r)
#print(type(r))

#t = e(a(3), b(4), c(3, 4))
#print(t)
#print(type(t))

j = f
print(j)
print(type(j))





