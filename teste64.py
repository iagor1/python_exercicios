
num = tuple(int(input('digite um n : '))for i in range(0,4))
print('o número 9 apareceu ',num.count(9),'vezes ')
if 3 in num:
    print('o número 3 apareceu na ',num.index(3),' posição ')
else:
    print('não foi achado o 3')
for n in num:
    if n % 2 ==0:
        print(n)