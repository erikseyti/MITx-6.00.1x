# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:06:48 2017

@author: sey_t
"""

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(7, 8)
#print(w1.getX())
#print(type((w1.getX())))
#print(w1.getY())

w2 = Wild(X, Y)
#print(w2.getX())
#print(type(w2.getX()))
#print(w2.getY())
#print(type(w2.getY()))
w3 = Wild(17, 18)
#print(w3.getX())
#print(type(w3.getX()))
#print(w3.getY())
#print(type(w3.getY()))

w4 = Wild(X, 18)
#print(w4.getX())
#print(type(w4.getX()))
#print(w4.getY())
#print(type(w4.getY()))
X = w4.getX() + w3.getX() + w2.getX()
#print(X)
#print(type(X))
#print(w4.getX())
#print(type(w4.getX()))
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
#print(Y)
#print(type(Y))
print(w2.getY())
print(type(w2.getY()))





