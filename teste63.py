from random import randint
maior = menor = 0
num= (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
for lista in num:
    print(lista, end=' ')
print('\no maior sorteado foi ', max(num))
print('o menor sorteado foi ', min(num))
