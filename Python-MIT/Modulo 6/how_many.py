# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:21:31 2017

@author: sey_t
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)
print(len(animals))