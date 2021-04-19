from datetime import date
ano = int(input('digite o ano que quer analisar, digite 0 para analisar o ano do seu computador : '))
if ano == 0 :
    ano = date.today().year
if ano % 4 and ano % 100 !=0 or ano%400 == 0 :
    print('O ano de ',ano , ' é bissexto' )
else :
    print('uai o ano de ', ano, 'n é bissexto ')