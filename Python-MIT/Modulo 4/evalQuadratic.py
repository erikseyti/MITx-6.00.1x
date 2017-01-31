# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:15:49 2017

@author: sey_t
"""
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    e = a*(x*x)+ b *x + c
    return e

print(evalQuadratic(3.06,5.23,7.12,-1.97))