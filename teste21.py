entrada =  float(input('digite a velocidade em km/h : '))
if entrada > 80 :
    sla = entrada - 80  
    multa = sla * 7
    print('Você foi multado, e pagará : ',multa )
else : 
    print('não foi multado. ')
