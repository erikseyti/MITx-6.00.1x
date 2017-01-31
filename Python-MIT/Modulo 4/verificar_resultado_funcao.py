# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:00:19 2017

@author: sey_t
"""

def a(x):
   '''
   x: int or float.
   '''
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
   x: Can be int or float.
   y: Can be int or float.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be int or float.
   y: Can be int or float.
   z: Can be int or float.
   '''
   return x >= y and x <= z
   
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
   
print(f(2,9))


