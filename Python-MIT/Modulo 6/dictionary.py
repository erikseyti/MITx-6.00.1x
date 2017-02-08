# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:34:48 2017

@author: sey_t
"""
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'

print(animals)
print("==========================")
print(animals['c'])
print("==========================")
#print(animals['donkey'])

print(len(animals))
print("==========================")
animals['a'] = 'anteater'
print(animals['a'])
print("==========================")
print(len(animals['a']))
print("==========================")
print('baboon' in animals)
print("==========================")
print('donkey' in animals.values())
print("==========================")
print('b' in animals)
print("==========================")
print(animals.keys())
print("==========================")
del animals['b']
print(len(animals))
print("===========================")
print(animals.values())