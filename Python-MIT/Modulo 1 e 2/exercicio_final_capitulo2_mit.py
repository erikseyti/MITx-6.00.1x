# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:20:46 2017

@author: sey_t
"""
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
