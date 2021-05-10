p = str(input('digite : ')).strip().upper().replace('','')
if p == p[::-1]:
    print('é um palíndromo.')
    print(p)
else: 
    print('não é palíndromo.')
    print(p)
