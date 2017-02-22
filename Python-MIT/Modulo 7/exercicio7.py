# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:07:12 2017

@author: sey_t
"""
def f(n):
   """
   n: integer, n >= 0.
   """
   print("antes da primeira condição: " + str(n))
   if n == 0:
      print("dentro da primeira condição: " + str(n))
      return 1
   else:
      print("dentro do else: " + str(n))
      return n * f(n-1)
      
      
      
      
      
      
x = f(3)
print(x)