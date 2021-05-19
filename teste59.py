import random
contVitorias=0
while True:
    sorteadoPc = random.randint(0,10)
    r = ' '
    while r not in 'parimpar':  #recurso pra só digitar par ou impar 
        r = str(input('Par ou ímpar  [p/i] : ')).lower().split()[0]
    n = int(input('digite um número : '))
    soma = n + sorteadoPc
    if soma % 2 == 0 and r == 'p' : #par
        print('você ganhou !!')
        contVitorias+=1
        print(f'voce jogou {n} o computador jogou {sorteadoPc} a soma deles é {soma} logo é par.')
    elif soma % 2 != 0 and r== 'i' : 
        print('você ganhou!!') #impar
        print(f'voce jogou {n} o computador jogou {sorteadoPc} a soma deles é {soma} logo é ímpar.')
        contVitorias+=1
    else:
        print('Você perdeu :( ')
        print(f'voce jogou {n} o computador jogou {sorteadoPc} a soma deles é {soma}. Você acumulou {contVitorias} vitórias.')
        break    
