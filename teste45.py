contMenor = 0
contMaior = 0
for c in range(1,8):
     idades = int(input('em que ano a {} nasceu?  '.format(c)))
     calculoIdade = 2021 - idades
     if calculoIdade >= 18:
        contMaior +=1
        print('essa pessoa é MAIOR de idade.')
        
     else:
        contMenor+=1
        print('essa pessoa é MENOR de idade.')
print('Ao todo tem ', contMaior,'pessoas maiores de idade.')

print('Ao todo tem ', contMenor,'pessoas menor de idade.')