# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:11:08 2017

@author: sey_t
"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

x = search([10,30],30)
y = newsearch([10,30],30)
print(x)
print(y)