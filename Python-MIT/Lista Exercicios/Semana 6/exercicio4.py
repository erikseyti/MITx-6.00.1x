# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:40:29 2017

@author: sey_t
"""
#
#def modten(n):
#    return n%10
#
#
#
#x = modten(2555555555500000000000000000000000000000000)
#print(x)



#def multlist(m, n):
#    '''
#    m is the multiplication factor
#    n is a list.
#    '''
#    result = []
#    for i in range(len(n)):
#        result.append(m*n[i])
#    return result
#
#
#y = multlist(33,[1, 22, 4, 5, 8, 87, 99, 555, 5555, 66666, 7777, 10, 1, 1, 1, 1,1 ,1 ])
#print(y)

#def foo(n):
#    print("oi")
#    print(n)
#    if n <= 1:
#        return 1
#    return foo(n/2) + 1
#
#c = foo(200)
#print(c)


#def recur(n):
#    if n <= 0:
#        return 1
#    else:
#        return n*recur(n-1)
#
#        
#v = recur(20)
#print(v)

def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )
            
b = baz(6)
print(b)


