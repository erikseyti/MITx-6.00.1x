# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:29:24 2017

@author: sey_t
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    # tupla que contem como variaveis os dicionarios: dicionarioAdd e dicionarioDiferenca
    intersecao = ()
    # dicionario da interseção das 2 listas, caso uma chave aparece em ambos os dicionarios, este dicionario
    # ira guardar a soma de seus valores
    dicionarioAdd = {}
    # dicionario que irá guardar todas os valores de chave que aparecem apenas no d1 ou apenas no d2
    dicionarioDiferenca = {}
    # variavel que contem os valores do d1
    dicionarioAuxiliarA = d1
    # varivel que contem os valores do d2
    dicionarioAuxiliarB = d2
    # variavel que contem o valor da respectiva soma dos elementos dos 2 dicionarios
    somaValoresDicionario =0
    # referente ao numero de valores presentes dentro do Dicionario d1
    tamanhoDicionarioA = len(d1)
    # referente ao numero de valores presentes dentro do dicionario d2
    tamanhoDicionarioB = len(d2)
    
    #print("tamanho do dicionario d1: " + str(tamanhoDicionarioA))
    #print("tamanho do dicionario d2: " + str(tamanhoDicionarioB))
    
    if tamanhoDicionarioA >= tamanhoDicionarioB:
        #print("biscoito")
        for dictA in d1:
            if dictA in d2:
                if dicionarioAuxiliarA[dictA] <= dicionarioAuxiliarB[dictA]:
                    #print("entrou A")
                    #print(dicionarioAuxiliarA[dictA])
                    #print(dicionarioAuxiliarB[dictA])
                    dicionarioAdd[dictA] = True
                    #print(dicionarioAdd)
                else:
                    #print("entrou B")
                    #print(dicionarioAuxiliarA[dictA])
                    #print(dicionarioAuxiliarB[dictA])
                    dicionarioAdd[dictA] = False
                    #print(dicionarioAdd)
            if not dictA in d2:
                dicionarioDiferenca[dictA] = dicionarioAuxiliarA[dictA]
        for dictB in d2:
            if not dictB in d1:
                dicionarioDiferenca[dictB] = dicionarioAuxiliarB[dictB]
                
        intersecao += (dicionarioAdd,)
        intersecao += (dicionarioDiferenca,)
        #print(intersecao)
        return intersecao
    
    
    else:
        for dictA in d1:
            #print(dictA)
            if dictA in d2:
                #print("valor da interseção: "+ str(dictA))
                #print(dicionarioAuxiliarA[dictA])
                #print(dicionarioAuxiliarB[dictA])
                somaValoresDicionario = dicionarioAuxiliarA[dictA] + dicionarioAuxiliarB[dictA]
                #print(somaValoresDicionario)
                dicionarioAdd[dictA] = somaValoresDicionario
                #print(dicionarioAdd)
            if not dictA in d2:
                dicionarioDiferenca[dictA] = dicionarioAuxiliarA[dictA]
                #print(dicionarioDiferenca)
        for dictB in d2:
            if not dictB in d1:
                dicionarioDiferenca[dictB] = dicionarioAuxiliarB[dictB]
                #print(dicionarioDiferenca)
        intersecao += (dicionarioAdd,)
        intersecao += (dicionarioDiferenca,)
        #print(intersecao)
        return intersecao
        
        
        

        
        
        
        

        
        
        
        
        
        
data = dict_interdiff({1: 0, 2: 1, 3: 2, 4: 3, 5: 0}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2})
print(data)