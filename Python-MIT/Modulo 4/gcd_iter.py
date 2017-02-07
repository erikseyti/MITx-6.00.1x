# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:50:25 2017

@author: sey_t
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:37:34 2017

@author: sey_t
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    menorValor =0
    maiorDivisorComum =1
    auxiliar =0
    if a> b:
        menorValor = b
    else:
        menorValor = a
    auxiliar = menorValor
    print(b/menorValor)
    while auxiliar >= 1:
        if a / menorValor != float and b / menorValor != float:
            
            maiorDivisorComum = menorValor
        else:
            menorValor = menorValor -1
        auxiliar = auxiliar - 1
    return maiorDivisorComum

x= gcdIter(9,12)
print(x)