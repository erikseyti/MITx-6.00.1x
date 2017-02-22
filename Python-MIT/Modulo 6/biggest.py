# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:57:56 2017

@author: sey_t
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    valorAtual = 0
    maiorValor = 0
    valorMaior = ""
    contador = 0
    
    for c in aDict.keys():
        print(aDict.values())
        valorAtual = len(aDict[c])
        valorMaior = aDict[c][contador]
        if valorAtual >= maiorValor:
            maiorValor = valorAtual
            valorMaior = valorMaior
        contador = contador
    return valorMaior
    
x = biggest(animals)
y = animals.keys()
print(x)
#print(x)

