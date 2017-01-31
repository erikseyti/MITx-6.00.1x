# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 20:11:42 2017

@author: sey_t
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 