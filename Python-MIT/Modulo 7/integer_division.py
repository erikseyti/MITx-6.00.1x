# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:37:13 2017

@author: sey_t
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count
    
    
x = integerDivision(5, 3) 
print(x)