# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:02:23 2017

@author: sey_t
"""

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    y= x%2
    return y!=0


x=odd(3)
print(x)