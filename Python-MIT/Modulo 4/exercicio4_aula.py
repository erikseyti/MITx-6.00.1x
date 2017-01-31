# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:45:18 2017

@author: sey_t
"""

#a = 10
#def f(x):
#    return x + a
#a = 3
#r= f(1)
#print(r)
#print(type(r))

x = 12
def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
p =g(x)
print(p)
print(type(p))