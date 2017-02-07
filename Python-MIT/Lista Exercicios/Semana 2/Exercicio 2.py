# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:50:25 2017

@author: sey_t
"""
balance = 3926
annualInterestRate =0.2
valorTaxaInteresse =0
valorFixoPagamento= 0
updateBalance=0
mes=1
valorTaxaInteresse =0

def payDebt(balance, annualInterestRate):
    mes=1
    valorFixoPagamento = 0.01
    valorTaxaInteresse = annualInterestRate/ 12
    updateBalance =0
    valorFixo2Casas=0
    while updateBalance >=0:
        valorFixoPagamento = valorFixo2Casas+ 0.01
        while mes<13:
            if mes == 1:
                updateBalance = balance
            print("O valor do balanço bancario no começo do mês "+ str(mes)
            + " é: "+ str(updateBalance))
            updateBalance = updateBalance - valorFixoPagamento
            print("balanço: " + str(updateBalance))
            updateBalance = updateBalance + (valorTaxaInteresse* updateBalance)
            mes = mes + 1
            valorFixo2Casas = round(valorFixoPagamento,2)
        mes = 1
    return valorFixoPagamento

x =payDebt(balance, annualInterestRate)
print(x)
        