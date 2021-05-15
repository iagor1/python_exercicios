print('='*40)
print('10 TERMOS DE UMA P.A.')
print('='*40)
numerosDePA = 0
cont = 1
termo1 = int(input('Digite um numero : '))
razao = int(input('Razão : '))
inicio = 10
total = 0 
while inicio != 0:
    total= total+ inicio    
    while cont <=total: 
        print('a razão dos termos é', termo1)
        termo1+=razao
        cont+=1
        numerosDePA+=1
    print('número de P.A.',numerosDePA)
    print('PAUSA')
    inicio = int(input('quantos números a mais você quer? '))
print('número de totais da P.A.',numerosDePA)
print('the end.')