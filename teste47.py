maiorIdadeHomem = 0 
contMulher20= 0
somaIdade= 0
maisVelho = 0 
for i in range(1,5):
    idade = int(input('digite a sua idade: '))
    nome = str(input('digite seu nome : ')).strip()
    sexo = str(input('Sexo [M/F] ? ')).strip()
    print('-'*40)
    somaIdade += idade

    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        maisVelho = nome
    elif sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        maisVelho = nome
    elif sexo in 'Ff' and idade >20:
        contMulher20+=1
mediaIdades = somaIdade/4
print('o mais velho foi ',nome,end ='.')
print('a média de idades é ',mediaIdades ,end ='.')
print('tem ', contMulher20,'mulheres abaixo de 20 anos.')