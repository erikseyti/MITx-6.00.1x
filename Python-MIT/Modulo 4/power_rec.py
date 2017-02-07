# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:50:56 2017

@author: sey_t
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp ==1:
        return base
    elif exp ==0:
        return 1
    else:
        return base * recurPower(base, exp-1)
    
w= recurPower(2,0)
print(w)