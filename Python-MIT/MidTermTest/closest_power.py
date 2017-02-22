# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:35:15 2017

@author: sey_t
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    expoente = -1
    #valor referente ao numero elevado
    valorPotencial =0
    #valor da diferença entre valorPotencial e a numero escolhido (num)
    diferençaPotencial =-1
    #valor mais proximo entre a base elevada e o num
    valorMaisProximo =0
    valorDiferençaPotencial =0
    valorMaisAproximado =0
    if num == 1:
        return 0
    while diferençaPotencial == -1 or valorDiferençaPotencial <=0:
        expoente = expoente + 1
        valorPotencial = base ** expoente
        print("valor do Potencial "+str(valorPotencial))
        diferençaPotencial = num - valorPotencial 
        print("Diferença Potencial : "+ str(diferençaPotencial))
        valorDiferençaPotencial = valorMaisProximo - diferençaPotencial
        print("ValorDiferençaPotencial : "+ str(valorDiferençaPotencial))
        print("valorMaisProximo: "+ str(valorMaisProximo))
        valorMaisAproximado = valorDiferençaPotencial - valorMaisProximo
        print(valorMaisAproximado)
        if valorMaisAproximado >= valorMaisProximo:
            valorMaisProximo = diferençaPotencial
        print("oi")
    return expoente 
        
        
       
        

s = closest_power(3,12)
print(s)
    