# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:23:50 2017

@author: sey_t
"""

#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) < epsilon:
#        break
#    else:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))
    
    
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) >= epsilon:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))
    
    
x = 775
epsilon = 0.01
step = 0.1
guess = 0.0
tentativa =0
while abs(guess**2-x) >= epsilon:
    tentativa = tentativa + 1
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print(guess)
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
print(tentativa)
    
    