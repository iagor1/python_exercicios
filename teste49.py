import random

sorteado = random.randint(0, 10)

print('sortearei um número entre 0 e 10 tente acertar ')

acertou = False
qtdTentativas = 0

while not acertou :
    
    tentativa = int(input('tente adivinhar qual número eu escolhi : '))
    qtdTentativas +=1

    if tentativa == sorteado : 
        acertou = True
    else:
        if tentativa < sorteado: print('tente um numero maior...')
        elif tentativa > sorteado: print('tente um numero menor...')        
print('acertou miseravi, você demorou  vezes pra acertar.',qtdTentativas) 