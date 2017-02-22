# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:49:27 2017

@author: sey_t
"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

    
x = how_many(animals)
print(x)