entrada =  float(input('digite a velocidade em km/h : '))
if entrada > 80 :
    sla = entrada - 80  
    calculo = sla * 7
    print('Você foi multado, e pagará : ',calculo )
else : 
    print('não foi multado. ')
