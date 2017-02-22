# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:19:10 2017

@author: sey_t
"""
#exercicio 3.1
#stuff  ="iQ"
#for thing in stuff:
#    if thing == 'iQ':
#        print("Found it")


#exercicio 3.2
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x



y = Square()
print(y)
