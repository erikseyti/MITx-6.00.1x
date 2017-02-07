# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:18:08 2017

@author: sey_t
"""

a= listA = [1, 4, 3, 0]
b = listB = ['x', 'z', 't', 'q']

a = listA.sort()
print(a)
print(type(a))
print("-------------------------")
print(listA)
print(type(listA))
print("-------------------------")
listA.insert(0, 100)
print(listA.insert(0, 100))
print(type(listA.insert(0, 100)))
print("-------------------------")
print(listA)
print(type(listA))
print("-------------------------")
listA.append(7)
print(listA.append(7))
print(type(listA.append(7)))
print("-------------------------")
print(listA)
print(type(listA))
print("-------------------------")
listC = listA + listB
print(listC)
print(type(listC))
print("-------------------------")
listB.sort()
listB.pop()
print(listB)
print(type(listB))
print("-------------------------")
print(listB.count(a))
print(type(listB.count(a)))
print("-------------------------")
#erro no console
#print(listB.remove(a))
#print(type(listB.remove(a)))
print("AQUI")
print(listA.extend([4, 1, 6, 3, 4]))
print(type(listA.extend([4, 1, 6, 3, 4])))
print("-------------------------")
print(listA.count(4))
print(type(listA.count(4)))
print("-------------------------")
print(listA.index(1))
print(type(listA.index(1)))
print("-------------------------")
print("AQUI")
listA
print(listA.pop(4))
print(type(listA.pop(4)))
print("-------------------------")
listA.reverse()
print(listA)
print(type(listA))



