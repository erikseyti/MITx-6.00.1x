# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:14:58 2017

@author: sey_t
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def abs(a):
    if (a>0):
        return a
    else:
        return a * -1
        
        
testList = [1, -4, 8, -9]

testList= applyToEach(testList, abs)
print(testList)