print('CALCULO DE FATORIAL ')

n = int(input('digite um número :'))
c = n
f =1

while c >0:
    print('{}'.format(c) ,end=' ')
    print(' x ' if c >1 else' = ', end=' ')
    f *= c
    c -= 1 # se essa linha ficar acima do f*=c, o c vai zerar e printar 0 

print('o resultado do fatorial de',n, 'é :',f)