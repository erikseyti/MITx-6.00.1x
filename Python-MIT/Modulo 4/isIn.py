# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:56:09 2017

@author: sey_t
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
        
    valorBaixo =0
    valorAlto =len(aStr)
    numeroCarac = valorAlto
    contador =0
    chute = round((valorBaixo+ valorAlto)/2)
    chuteNumerico = aStr[chute]
    print(valorAlto)
    print(chute)
    print(chuteNumerico)
    print(char)
   
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    while numeroCarac > contador:
        contador = contador + 1
        if char == chuteNumerico:
            print(char)
            print(chuteNumerico)
            return True
        else:
            if chuteNumerico > char:
                print("entrou")
                valorAlto = chute
                chute = round((valorBaixo + valorAlto)/2)
                chuteNumerico = aStr[chute]
                print(chuteNumerico)
            else:
                print("entrou 2")
                valorBaixo = chute
                chute = round((valorBaixo + valorAlto)/2)
                chuteNumerico = aStr[chute]
                print(chuteNumerico)

carac= isIn("u","")
print(carac)    