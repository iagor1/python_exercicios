ano = int(input('digite o ano atual :'))
nascimentoAno = int(input('digite a data de nascimento : '))
idade = ano - nascimentoAno

if ano < nascimentoAno :
    print('o ano atual não pode ser menor que o ano de nascimento !')

elif idade == 18:
    print('você precisa se alistar!')
    print('Você nasceu em ',nascimentoAno, ' e tem', idade, 'anos ')

elif idade > 18 :
    saldo = idade - 18
    print('Você está atrasado para o alistamento! Você deveria ter le alistado há ', saldo,' anos')
    print('Você nasceu em ',nascimentoAno, ' e tem', idade, 'anos ')

elif idade <18 :
    saldo = idade - 18     
    print('Você ainda não precisa se alistar, ainda falta', saldo,' anos')
    print('Você nasceu em ',nascimentoAno, ' e tem', idade, 'anos ')
    