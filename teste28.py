valorCasa = int(input('digite o valor da casa em reais : '))
salario = int(input('digite seu salário : '))
financiamento = int(input('anos de investimentos : '))
calculoPrestacao = valorCasa/(financiamento*12) #prestação mensal
naosei = salario * 0.30
if calculoPrestacao> naosei:
    print('o valor da prestação mensal é {:.2f} reais, o seu financiamento foi rejeitado pois a prestação execeu mais de 30 porcento do seu salário '.format(calculoPrestacao))
else : 
    print('O seu financiamento será aprovado :) ')   