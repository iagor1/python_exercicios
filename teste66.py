texto = ('swujhbv','imiuyb','uibafioi','uytreaflll')
for i in texto:
    print(f'Na palavra {i}')
    for vogais in i:
        if vogais.lower() in 'aeiou':
            print(f'temos {vogais}')