print('SEQUÊNCIA DE FIBONACCI')
print('-'*40)

n1 = 0 
n2 = 1



termos = int(input('quantos termos você quer? '))

c = 3 #começa em 3 pois já temos o 1 e o 2 termo.

while c <= termos:
    n3= n1 +n2
    print('a sequência é ',n3) 
    n1 = n2
    n2 = n3
    c+=1
  