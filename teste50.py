
n1 = int(input('digite um número : '))
n2 = int(input('digite um número : '))
opcao = 0 
while opcao!=5:
    print(''' 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa 
''')
    opcao = int(input('selecione uma opção : '))
    if opcao == 1:
        print('voce escolheu soma')
        soma = n1+n2 
        print('a soma é ',soma)
    elif opcao ==2: 
        print('voce escolheu multiplicação')
        multiplicacao = n1*n2 
        print('o resultado é =',multiplicacao)
    elif opcao ==3:
       if n1 > n2 : maior = n1
       else: maior= n2
       print('o maior Número entre os dois foi :', maior)
    elif opcao==4:
        n1 = int(input('digite um número : '))
        n2 = int(input('digite um número : '))
    elif opcao==5:
        print('fim do programa. :)')
    else:
        print('opção inválida, digite novamente!')