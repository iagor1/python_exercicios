maiores =homens=mulheres20= 0
while True:
    idade= int(input('idade : '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('sexo [m/f] ? ')).lower().strip()[0]
    if idade>=18 : maiores += 1
    if sexo=='m': homens+=1
    if sexo=='f' and idade<20: mulheres20+= 1
    p=' '
    while p not in 'sn':
        p = str(input('deseja continuar [s/n]? ')).lower().strip()[0]
    if p == 'n':break
print(f'há {maiores} maiores de idade, tem {homens} homens registrados e há {mulheres20} mulheres com menos de 20 anos.') 