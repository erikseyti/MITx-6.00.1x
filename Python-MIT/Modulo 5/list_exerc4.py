# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:43:05 2017

@author: sey_t
"""

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
print(aList == bList)
print(type(aList == bList))
print("--------------------------")
print(aList is bList)
print(type(aList is bList))
print("--------------------------")
print(aList)
print(type(aList))
print("--------------------------")
print(bList)
print(type(bList))
print("--------------------------")
cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
print(cList == dList)
print(type(cList == dList))
print("--------------------------")
print(cList is dList)
print(type(cList is dList))
print("--------------------------")
cList[2] = 20
print(cList)
print(type(cList))
print("--------------------------")
print(dList)
print(type(dList))



