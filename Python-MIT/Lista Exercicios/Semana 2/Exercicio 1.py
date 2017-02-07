# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:01:04 2017

@author: sey_t
"""
import decimal
balance = 114
annualInterestRate=0.15
monthlyPaymentRate =0.05


def bankPayment(balance,annualInterestRate, montlyPaymentRate):
    mes=1
    valorMinimoMes =0
    valorTaxaInteresse =0
    valorAproximado =0
    while mes <13:
        print("o valor do balanço bancario no começo do mês "+ str(mes)
        + " é: " + str(balance))
        print(montlyPaymentRate)
        valorMinimoMes = balance * montlyPaymentRate
        print("o valor da taxa mensal é: "+ str(valorMinimoMes))
        balance = balance - valorMinimoMes
        print("o valor do balanço após pago a taxa mensal é: "+ str(balance))
        valorTaxaInteresse = (annualInterestRate/12) * balance
        print("o valor da taxa mensal de Interesse é"+ str(valorTaxaInteresse))
        balance = balance + valorTaxaInteresse
        valorAproximado = round(balance,2)
        print("o valor do balanço no final do mês "+ str(mes) +" é: " +str(balance))
        #Unico saída que deverá ser exibida para a entrega
        print("Month "+ str(mes) +" Remaining balance: "+ str(valorAproximado))
        mes = mes + 1
        

mes=1
valorMinimoMes =0
valorTaxaInteresse =0
valorAproximado =0
while mes <13:
    valorMinimoMes = balance * monthlyPaymentRate
    balance = balance - valorMinimoMes
    valorTaxaInteresse = (annualInterestRate/12) * balance
    balance = balance + valorTaxaInteresse
    valorAproximado = round(balance,2)
    mes = mes + 1       
print("Remaining balance: "+ str(valorAproximado))