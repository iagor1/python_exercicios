teste = ('seferf',84,'afawefw', 2323,'srgvsr', 7676)
for i in range(0, len(teste)):
    if i % 2 ==0:
        print(f'{teste[i]:.<25}', end='')
    else:
        print(f'{teste[i]:.>}')