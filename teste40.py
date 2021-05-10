cont = 0
soma = 0
for c in range(1,7):
    n = int(input('digite o {} valor : '.format(c)))
    if n % 2 == 0 :
         soma = soma + n
         cont = cont + 1 
print('a soma dos números é {} e a qtd de valores pares é {}'.format(soma,cont))