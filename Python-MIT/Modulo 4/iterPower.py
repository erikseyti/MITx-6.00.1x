# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:44:08 2017

@author: sey_t
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    resultado =1
    contador=0
    while contador < exp:
        resultado = resultado*base
        contador= contador +1
    return resultado
    
w= iterPower(7,2)
print(w)
    