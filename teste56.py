opcao = 's'

c= soma = media = 0 

while opcao == 's':
    n = int(input('digite um número :'))
    opcao = str(input('quer continuar [s/n] ?')).lower().strip()[0]
    c+=1
    soma +=n
    if c ==1:
        
        maior = menor = n
    
    else:

        if n > maior: maior = n
        
        if n < menor: menor = n

media = soma/c
print('a media é : ', media)
print('o total de números é :', c)
print('o maior número foi ',maior, 'o menor foi ', menor)