# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:55:33 2017

@author: sey_t
"""

s = "bobobbboopopbyoboybzzzzzbbboooobobbob"

palavrabob=""
numeroBob = 0
for caracter in s:
    if caracter == 'b' or caracter == "o":        
        if caracter == 'b':
            print("entrou")
            palavrabob = palavrabob + "b"
            if palavrabob == "bb":
                palavrabob = "b"
            elif palavrabob == "ob":
                palavrabob = "b"
        elif caracter == 'o':
            palavrabob = palavrabob + "o"
            print(palavrabob)
            if palavrabob == "boo":
                palavrabob =""
            elif palavrabob == "oo":
                palavrabob=""
        if palavrabob == "bob":
            print(palavrabob)
            numeroBob = numeroBob + 1
            palavrabob = "b"
    else:
        palavrabob =""
print("Number of times bob occurs is: " +str(numeroBob))

        

  
    
    
