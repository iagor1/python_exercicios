n = int(input('digite um número : '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont+=1
        print('\033[34m',n, c)
    else:
        print('\033[1;33m',n , c)    
print('o número ', n, 'foi dividido', cont)
if cont==2 :
    print('	\033[0;0m o número é primo.')
else:
    print('o número n é primo pois o número tem mais de 2 divisores.')