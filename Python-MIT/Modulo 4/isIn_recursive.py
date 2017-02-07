# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:02:44 2017

@author: sey_t
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    def validar(char,aStr):
        if len(aStr) == 0:
            return False
        if len(aStr) == 1:
            if char == aStr:
                return aStr
            else:
                return False
    def contabilizar(char,aStr  ):
        
        valorBaixo =0
        valorAlto =len(aStr)
        chute = round((valorBaixo+ valorAlto)/2)
        chuteNumerico = aStr[chute]
        
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
                return numeroCarac * isIn(numeroCarac-1)

carac= isIn("u","abcdefghijklmnopqrstuvw")
print(carac)    
