# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:31:34 2017

@author: sey_t
"""

varA = 2
varB = 3

if type(varA) == str or  type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")
    
    
