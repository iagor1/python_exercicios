print('='*40)
print('10 TERMOS DE UMA P.A.')
print('='*40)
termo1 = int(input('Digite um numero : '))
razao = int(input('Razão : '))
decimoTermo = termo1+(10-1)*razao 
for c in range(termo1 ,decimoTermo, razao):
    print('os termos são : ', c ,'o último termo é', decimoTermo)
print('fim.')