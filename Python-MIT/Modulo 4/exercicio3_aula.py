# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:34:56 2017

@author: sey_t
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
    
#s = a(False, 2, 3)
#print(s)
#print(type(s))

#d = b(3, 2)
#print(d)
#print(type(d))

#g = a(3>2, a, b)
#print(g)
#print(type(g))

m = b(a, b)
print(m)
print(type(m))