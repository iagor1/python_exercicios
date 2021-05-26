numeros = ('zero','um ','dois ','três ','quatro' ,'cinco' ,'seis', 'sete' ,'oito' ,'nove', 'dez', 'onze', 'doze', 'treze',' quatorze',  'quinze', 'dezesseis ',' dezessete' ,'dezoito' ,'dezenove', 'vinte')


while True:
    n = int(input('digite um n de 0 a 20 : '))
    if 0 <= n <=20: break 
print('voce digitou ',numeros[n])

