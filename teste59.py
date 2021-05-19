import random
contVitorias=0
while True:
    sorteadoPc = random.randint(0,10)
    r = str(input('Par ou ímpar  [p/i] : ')).lower().split()[0]
    n = int(input('digite um número : '))
    soma = n + sorteadoPc
    if soma %2 ==0 and r == 'p':
        print('você ganhou !!')
        contVitorias+=1
        print(f'voce jogou {n} o computador jogou {sorteadoPc} a soma deles é {soma} logo é par.')

print(f'voce jogou {n} o computador jogou {sorteadoPc} a soma deles é {soma} ')
