# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:57:24 2017

@author: sey_t
"""
balance = 320000
annualInterestRate =0.2
monthlyInterestRate = annualInterestRate/12.0
aproximacao = 0.1
mes=1
valorFixoPagamento = 0

updateBalance =balance
valorMontantePagamento =0
valorMontanteJuros = 0
low = balance/12
high = (balance* (1+ monthlyInterestRate)**12)/12.0
valorFixoPagamento = (high + low)/2.0
valorTotalPagamento = (balance * (1 + monthlyInterestRate)**12)
while abs(updateBalance) >= aproximacao:
    if (valorFixoPagamento*12) < balance:
        high = valorFixoPagamento
    else: 
        low = valorFixoPagamento
    valorFixoPagamento = (low + high)/12.0
    valorMontantePagamento =0
    print('low = ' + str(low) + ' high = ' + str(high) + "vp = "+ str(valorFixoPagamento))
    mes = 1
    while mes<13:
        if mes == 1:
            updateBalance = balance
            valorMontanteJuros =updateBalance
       # print("O valor do balanço bancario no começo do mês "+ str(mes)
       # + " é: "+ str(updateBalance))
        updateBalance = round(updateBalance - valorFixoPagamento,1)
       # print("balanço: " + str(updateBalance))
        updateBalance = round(updateBalance + (monthlyInterestRate* updateBalance),1)
        mes = mes + 1
        valorMontantePagamento = valorMontantePagamento + valorFixoPagamento
        valorMontanteJuros = valorMontanteJuros + (monthlyInterestRate *updateBalance)
print("Lowest Payment: "+ str(valorFixoPagamento))