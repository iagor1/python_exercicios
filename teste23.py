entrada = float(input('a sua viagem de quantos km ? '))
if entrada <= 200 :
    preco = entrada * 0.50
    print('O total a pagar é R$ ',preco)
else : 
    preco2 = entrada * 0.45
    print('O total a pagar é R$ ', preco2)
    