# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:21:31 2017

@author: sey_t
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

exemplo = {'s': ['aardvark', 'mamute', 'centauro'],'b' :['aa',"cv","ww"]}

#print(animals)
#print(len(animals))
d = animals
c= exemplo
print(c)
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    contador = 0
    
    for c in aDict.keys():
        contador = contador + len(aDict[c])

    return contador
    
    
    
x = how_many(animals)
print(x)