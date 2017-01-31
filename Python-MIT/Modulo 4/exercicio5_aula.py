# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:43:08 2017

@author: sey_t
"""

#def foo(x, y = 5):
#   def bar(x):
#      return x + 1
#   return bar(y * 2)
#          
#z= foo(3)
#
#print(z)
#print(type(z))

#def foo(x, y = 5):
#   def bar(x):
#      return x + 1
#   return bar(y * 2)
#          
#w= foo(3, 0)
#print(w)
#print(type(w))

#def foo (x):
#   def bar (z, x = 0):
#      return z + x
#   return bar(3, x)
#
#n = foo(2)
#print(n)
#print(type(n))

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

u = foo(5)
print(u)
print(type(u))


