salario = int(input('DIGITE SEU SALÁRIO PARA CALCULAR O AUMENTO : '))
if salario > 1250 :
    calculo1 = salario * 0.10 + salario
    print('seu aumento é de : ',calculo1)
else : 
    calculo2 = salario * 0.15 + salario
    print('seu aumento é de : ',calculo2)
print('-'*20, 'FIM','-'*20 )