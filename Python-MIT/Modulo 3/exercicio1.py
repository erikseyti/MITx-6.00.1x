# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:19:22 2017

@author: sey_t
"""

#iteration = 0
#count = 0
#while iteration < 5:
#    # the variable 'letter' in the loop stands for every 
#    # character, including spaces and commas!
#    for letter in "hello, world": 
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
    
    
    
#iteration = 0
#while iteration < 5:
#    count = 0
#    for letter in "hello, world":
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
    
    
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 