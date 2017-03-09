# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:13:46 2017

@author: sey_t
"""

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

    
x = linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
print(x)
y = linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
print(y)