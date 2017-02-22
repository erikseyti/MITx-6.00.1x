# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:23:58 2017

@author: sey_t
"""
def f(i):
    return i + 4
def g(i):
    if i >= 17:
        return True
    else:
        return False
    
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    listaMutada = []
    if L == []:
        return -1
    for i in L:
        x = f(i)
        #print(x)
        y = g(x)
        if y == True:
            listaMutada += [x]
            #print(listaMutada)
        #print(y)
    L[:] = []
    L.extend(listaMutada)
    if L != []:
        x = max(L)
    else:
        x = []

    return x
        
    
    

    
    
L = [0, 22, 73,55]
x = applyF_filterG(L, f, g)
print(x)
print(L)

