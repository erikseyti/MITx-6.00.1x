# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:38:08 2017

@author: sey_t
"""
def square (x):
    '''
    x: int or float.
    '''
    # Your code here
    return x **2
    
def fourthPower(x):
    '''
    x: int or float.
    Essa função eleva o valor fornecido(x) em 4
    '''
    # Your code here
    return square(x) * square(x)

    
x= fourthPower(2)
print(x)
