n = int(input('digite um número inteiro pra ser convertido : '))
print('''selecione uma base  
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
''')
opcao = int(input('digite a opção : '))

if opcao == 1:
    print('resultado : {}'.format(bin(n) [2:]))
elif opcao == 2 : 
    print('resultado : {}'.format(oct(n)[2:]))
elif opcao == 3 : 
    print('resultado : {}'.format(hex(n)[2:]))
else : 
    print('digite uma opção válida!')