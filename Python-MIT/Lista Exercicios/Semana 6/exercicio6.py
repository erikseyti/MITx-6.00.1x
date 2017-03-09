# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:45:14 2017

@author: sey_t
"""

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

    
##x = swapSort([1,2,3,4,5,6,7,8,9])
##print("valor da primera lista em ordem crescente")
#xm = modSwapSort([1,2,3,4,5,6,7,8,9])
#print("novo valor da primera lista em ordem crescente")
##y = swapSort([9,8,7,6,5,4,3,2,1])
##print("valor da segunda lista em ordem decrescente")
#ym = modSwapSort([9,8,7,6,5,4,3,2,1])
#print("novo valor da segunda lista em ordem decrescente")
#wm = modSwapSort([8,7,9,5,6,3,32,11,1,0,10])
#print("novo valor da terceira lista em ordem aleatoria")
#em = modSwapSort([0,0,0,0,0,1,1,1,2,2,3,4,5,7,8,9,85,458,44,55,66,88,11,12])
#fm = modSwapSort([0,0,1,22,45,14,10,12,2,2,3,4,5,6,7,8,98,100,25])
gm = modSwapSort([11,12,-5,-6-7,-88,-11,-1,10,0,1,12,11,-1,0])
hm = modSwapSort([10000,1,0,-1,-10000000,100000.2,1.1,0,-1.2,-100000000000.1])

#h = 12* 666**67
#print(h)
