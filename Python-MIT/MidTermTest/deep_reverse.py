# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:02:09 2017

@author: sey_t
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    ListD =[]
    ListEmpty =[]
    for d in L:
        for i in reversed(d):
             ListEmpty = ListEmpty + [i]
        ListEmpty = ListEmpty
        ListD = ListD + [ListEmpty]
        ListEmpty =[]
    ListD.reverse()
    L[:] = []  


L =([[1500, 1501, -1000, 0, 2000], [1500, 1501, -1000, 0, 2000]])
deep_reverse(L)
print(L)


