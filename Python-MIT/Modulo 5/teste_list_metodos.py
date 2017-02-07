# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:46:21 2017

@author: sey_t
"""

x = "Erik Seyti Johansson"
y = "Erik Seyti Johansson ama muito a Ana Paula Fabrini"
nome = x.split(" ")
amor = y.split(" ")
print(nome)
primeiro_nome = nome[0]
sobrenome = nome[-1]
print(primeiro_nome)
print(sobrenome)
#faz uma troca "aleatoria" dos valores presentes na lista
print(sorted(nome))
#print(amor)
#print(sorted(amor))
amorS2 = amor[:]
##modificou permamentemente o valor de amorS2
amorS2.sort()
print(amorS2)
#revert o valor presente na variavel
amorS3 = amor[:  ]
amorS3.reverse()
print(amorS3)
