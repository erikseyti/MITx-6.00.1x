# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:05:04 2017

@author: sey_t
"""


maiorAlfabeto=""
#maior valor conseguido até o momento
maiorValor=""
#valor atribuido a ele 
valorAtual=""
#valor presente na sentença

#contador =0
#maiorAlfabeto=""
#maiorValor=""
#valorAtual=""    
#for caracter in s:
#    contador = contador+ 1
#    print ("contador: "+ str(contador))
#    if maiorAlfabeto != "" and maiorAlfabeto > caracter:
#        maiorAlfabeto =""
#    if caracter >= valorAtual:
#        print("Valor 1: " + str(valorAtual))
#        valorAtual = caracter
#        print("Valor 2: " + str(valorAtual))
#        maiorAlfabeto = maiorAlfabeto + caracter
#        print("Valor 3: " + str(maiorAlfabeto))
#        if len(maiorValor) < len(maiorAlfabeto):
#            maiorValor = maiorAlfabeto
#            print("Valor 4: " + str(maiorAlfabeto))
#    elif caracter < valorAtual:
#        maiorAlfabeto = ""
#        valorAtual = ""
#        maiorAlfabeto = maiorAlfabeto + caracter
#        print("Valor 5: " + str(maiorAlfabeto))
#print("Longest substring in alphabetical order is: " +str(maiorValor))

s = "ebxbhmoomozwxf"

contador =0
maiorAlfabeto=""
maiorValor=""
valorAtual=""    
for caracter in s:
    contador = contador+ 1
    print ("contador: "+ str(contador))
    if maiorAlfabeto != "" and maiorAlfabeto > caracter:
        maiorAlfabeto =""
    if caracter >= valorAtual:
        print("Valor 1: " + str(valorAtual))
        valorAtual = caracter
        print("Valor 2: " + str(valorAtual))
        maiorAlfabeto = maiorAlfabeto + caracter
        print("Valor 3: " + str(maiorAlfabeto))
        if len(maiorValor) < len(maiorAlfabeto):
            maiorValor = maiorAlfabeto
            print("Valor 4: " + str(maiorAlfabeto))
    elif caracter < valorAtual:
        maiorAlfabeto = ""
        valorAtual = ""
        maiorAlfabeto = maiorAlfabeto + caracter
        print("Valor 5: " + str(maiorAlfabeto))
print("Longest substring in alphabetical order is: " +str(maiorValor))

