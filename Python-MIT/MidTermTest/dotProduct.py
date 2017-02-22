# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:21:30 2017

@author: sey_t
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    resultado =0
    listC =  [a*b for a,b in zip(listA,listB)]
    #print(listC)
    for c in listC:
        resultado = resultado + c
        #print(resultado)
    return resultado
        

x = dotProduct([1,2,3],[4,5,6])
print(x)