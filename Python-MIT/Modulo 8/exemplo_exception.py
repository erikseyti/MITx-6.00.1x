# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:19:16 2017

@author: sey_t
"""

while True: 
    try: 
        n = input("Please enter an integer: ") 
        n = int(n) 
        break 
    except ValueError: 
        print("Input not an integer; try again") 
print("Correct input of an integer!")