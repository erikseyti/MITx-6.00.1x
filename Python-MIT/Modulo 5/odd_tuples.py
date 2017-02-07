# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:15:57 2017

@author: sey_t
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
      
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    contador = 0
    resultado = ()
    for t in aTup:
        if contador % 2 == 0:
           resultado = resultado + (t,)
        contador = contador + 1
    return resultado
        
        
x = oddTuples(("josh", 15, 3, 22, 25))
print(x)