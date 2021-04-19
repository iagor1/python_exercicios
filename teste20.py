import random
from time import sleep
sorteado = random.randint(0, 5)
print('sortearei um número entre 0 e 5 tente acertar ')
# entrada de dados 
tentativa = input('tente adivinhar qual número eu escolhi : ')
# saída de dados
print('Processando...') #aquela zueirinha de leves 
sleep(2)
if tentativa == sorteado :
    print('acertou miseravi ')
else: 
    print('errou miseravi, a resposta era ', sorteado)