# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:00:07 2017

@author: sey_t
"""

print("digite algum valor para ser exibido no console")

text = input("digite algo: ")
print("O valor digitado é: " + text)

print("para valores que não sejam do tipo String, é necessario realizar o Cast"+
"ou seja a conversão desse numero para ser exibido")

print("como exemplo peguei um int:")

valorInt = int(input("digite um valor do tipo int: "))
print("o valor esta convertido para int (se possivel essa conversão)")
print(type(valorInt))



