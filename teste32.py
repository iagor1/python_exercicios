idade = int(input('digite sua idade : '))
if idade < 9 :
    print('Você está na categoria mirim. ')

elif idade >9 and idade <= 14:
    print('Você está na categoria infantil. ')

elif idade > 14 and idade <= 19 :
    print('Você está na categoria junior. ')
elif idade > 19 and idade <=25:
    print('Você está na categoria sênior. ')
elif idade > 25 :
    print('Você está na categoria master. ')
