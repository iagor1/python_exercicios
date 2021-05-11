
sexo = str(input('digite seu sexo [M/F] : ')).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input('Digite uma letra válida!! Digite seu sexo [M/F] : ')).strip().upper()[0]
print('sexo registrado com sucesso, sexo : ',sexo) 