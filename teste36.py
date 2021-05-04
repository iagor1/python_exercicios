import random
from time import sleep
#############################
itens = ('pedra', 'papel', 'tesoura')
computador = random.randint(0, 2)
#############################
print('-'*40)
print('Pedra, papel, ou tesoura? ')
print('-'*40)
escolhaUser = int(input(''' 
[0] PEDRA
[1] PAPEL
[2] TESOURA
'''))

print('computando os votos...')  # aquele frufruzin
sleep(1)

print('O universo conspirou e jogou', itens[computador])
print('-'*40)
print('Você jogou ', itens[escolhaUser])


if computador == 0:  # pc escolheu pedra
    if escolhaUser == 0:
        print('EMPATE !')
    elif escolhaUser == 1:
        print('A FORÇA DO UNIVERSO FOI DERROTADA, VOCÊ VENCEU!')
    elif escolhaUser == 2:
        print('VOCÊ PERDEU!')
    else:
        print('escolha inválida!!!')
elif computador == 1:  # pc escolheu papel
    if escolhaUser == 0:
        print('A FORÇA DO UNIVERSO VENCEU VOCÊ!')
    elif escolhaUser == 1:
        print('EMPATE!!')
    elif escolhaUser == 2:
        print('A FORÇA DO UNIVERSO FOI DERROTADA, VOCÊ VENCEU!')
    else:
        print('escolha inválida!!!')

elif computador == 2:  # pc escolheu tesoura

    if escolhaUser == 0:
        print('A FORÇA DO UNIVERSO FOI DERROTADA, VOCÊ VENCEU!')
    elif escolhaUser == 1:
        print('A FORÇA DO UNIVERSO VENCEU VOCÊ!')
    elif escolhaUser == 2:
        print('EMPATE !')
    else:
        print('escolha inválida!!!')
