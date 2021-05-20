
total = maisDe1000 = menorpreco =c= 0

while True:
    nomeP = str(input('Nome do produto : ')) 
    preço = int(input('Preço : ')) 
    total+= preço
    c+=1 
    if c==1: menorpreco=preço #setando pra mais de uma entrada 
    else:
        if preço< menorpreco : menorpreco=preço
    
    if preço > 1000: 
        maisDe1000 += 1
    
    if preço > menorpreco:
        menorpreco = nomeP
    

    opcao=' ' 
    while opcao not in 'sn':
        opcao = str(input('deseja continuar [s/n] ? ')).lower().strip()[0]
    if opcao =='n': 
        break


print(f'o total a pagar R$ {total}. Há {maisDe1000} itens acima de 1000 reais. O item mais barato é {menorpreco}') 