import random
print('insira os números sorteados : ')
n1 = int(input('número 1 : '))
n2 = int(input('número 2 : '))
n3 = int(input('número 3 : '))
n4 = int(input('número 4 : '))
n5 = int(input('número 5 : '))
lista = [n1, n2, n3, n4, n5]
random.shuffle(lista)
print('a sequência sorteada é : ',)
print(lista)