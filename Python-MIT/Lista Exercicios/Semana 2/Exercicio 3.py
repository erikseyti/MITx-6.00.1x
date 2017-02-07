# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:08:45 2017

@author: sey_t
"""

#balance = 320000
#annualInterestRate =0.2
#valorTaxaInteresse =annualInterestRate/ 12
#valorFixoPagamento= 0
#updateBalance=0
#mes=1
#valorTaxaInteresse =0
#aproximacao = 0.01
#menorValor = balance/12
#maiorValor = (balance*(1+valorTaxaInteresse)**12)/12 
#
#def payDebt(balance, annualInterestRate):
#    mes=1
#    valorTaxaInteresse = annualInterestRate/ 12
#    menorValor = balance/12
#    maiorValor = (balance*(1+valorTaxaInteresse)**12)/12 
#    valorFixoPagamento = (menorValor + maiorValor)/12
#    updateBalance = balance
#    while abs(updateBalance-balance) !=aproximacao:
#        if abs(updateBalance)> aproximacao:
#            print("valor: "+ str(maiorValor))
#            maiorValor = valorFixoPagamento
#            print("maior Valor: "+ str(maiorValor))
#        elif abs(updateBalance)< aproximacao:
#            menorValor = valorFixoPagamento
#            print("mario valor@@@@")
#        print("@@ValorFixoPagamento: "+ str(valorFixoPagamento))
#        valorFixoPagamento = (menorValor + maiorValor)/2
#        print("##ValorFixoPagamento: "+ str(valorFixoPagamento))
#        while mes<13:
#            if mes == 1:
#                updateBalance = round(balance,2)
#            #print("O valor do balanço bancario no começo do mês "+ str(mes)
#            #+ " é: "+ str(updateBalance))
#           # print("o valor Fixo é: "+ str(valorFixoPagamento))
#           # updateBalance = updateBalance - valorFixoPagamento
#           # print("balanço: " + str(updateBalance))
#            updateBalance = updateBalance + (valorTaxaInteresse* updateBalance)
#            mes = mes + 1
#        mes = 1
#    return valorFixoPagamento
#
#x =payDebt(balance, annualInterestRate)
#print(x)

balance = 320000
annualInterestRate =0.2
monthlyInterestRate = annualInterestRate/12

def payDebt(balance, annualInterestRate):
    aproximacao = 0.1
    mes=1
    valorFixoPagamento = 0
    valorTaxaInteresse = annualInterestRate/ 12
    updateBalance =balance
    valorMontantePagamento =0
    valorMontanteJuros = 0
    low = balance/12
    high = (balance* (1+ monthlyInterestRate)**12)/12
    valorFixoPagamento = (high + low)/2.0
    while updateBalance >=aproximacao:
        if valorMontantePagamento > valorMontanteJuros:
            low = round(valorFixoPagamento,1)
        elif valorMontantePagamento < valorMontanteJuros:
            high = round(valorFixoPagamento,1)
        valorFixoPagamento = (low + high)/2.0
        valorMontantePagamento =0
        while mes<13:
            if mes == 1:
                updateBalance = balance
                valorMontanteJuros =updateBalance
            print("O valor do balanço bancario no começo do mês "+ str(mes)
            + " é: "+ str(updateBalance))
            updateBalance = round(updateBalance - valorFixoPagamento,1)
            print("balanço: " + str(updateBalance))
            updateBalance = round(updateBalance + (valorTaxaInteresse* updateBalance),2)
            mes = mes + 1
            valorMontantePagamento = valorMontantePagamento + valorFixoPagamento
            valorMontanteJuros = valorMontanteJuros + (valorTaxaInteresse *updateBalance)
        
           # print(valorMontantePagamento)
            #print(valorMontanteJuros)
        mes = 1
    return valorFixoPagamento

x =payDebt(balance, annualInterestRate)
print(x)




        