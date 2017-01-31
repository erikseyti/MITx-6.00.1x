# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:29:23 2017

@author: sey_t
"""

valorBaixo = 0
valorAlto = 100
chute = 50
escolhaUsuario = ""
print("Please think of a number between 0 and 100!")
while escolhaUsuario != 'c':
    print("Is your secret number "+ str(chute) + " ?")
    escolhaUsuario = str (input("Enter 'h' to indicate the guess is too high. "
    +"Enter 'l' to indicate the guess is too low. " +
    "Enter 'c' to indicate I guessed correctly."))
    if escolhaUsuario == "h":
        valorAlto = chute
    elif escolhaUsuario == "l":
        valorBaixo = chute
    elif escolhaUsuario == "c":
        print("Game over. Your secret number was: "+ str(chute))
        break
    else:
        print ("Sorry, I did not understand your input.")
    chute = int ((valorAlto + valorBaixo)/2)
    #se o valor apresentado for quebrado, deverá ser feito uma aproximação
    #deste valor 
