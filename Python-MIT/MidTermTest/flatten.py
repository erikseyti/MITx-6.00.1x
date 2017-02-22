# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:26:14 2017

@author: sey_t
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    a= []
    a = flatten_executed(aList, a)
    return a
    
def flatten_executed(aList, a):
    ''' 
    aList: tem como parametro uma lista
    a: uma lista vazia
    retorna uma copia da list Alist, a funcionalidade flatten de forma a ser executado n vezes dentro de um for
    para uma variavel a (que entra como vazia no inicio) e a cada iteração retorna os elementos sem os [] separando 
    cada um deles, de forma a trazer no final uma lista "plana" para cada um das suas variaveis 
    
    '''
    for i in aList:
        if isinstance(i, list):
            flatten_executed(i, a)
        else:
            a.append(i)
    return a
            
    
l = flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(l)