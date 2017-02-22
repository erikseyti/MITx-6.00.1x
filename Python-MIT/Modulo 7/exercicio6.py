# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:53:23 2017

@author: sey_t
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print(x)
    print(a)
    print("  ")
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
x = rem(7, 5)
print(x)