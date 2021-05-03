print('-'*40)
print('PAGAMENTO')
print('-'*40)
precoProduto = float(input('Digite o valor do produto : '))

formaPagemento = float(input('''SELECIONE UMA FORMA DE PAGAMENTO 
[ 1 ] A VISTA OU CHEQUE 10 % DE DESCONTO
[ 2 ] À VISTA NO CARTÃO 5% DE DESCONTO
[ 3 ] EM ATÉ 2X NO CARTÃP SEM JUROS
[ 4 ] 3X NO CARTÃO OU MAIS 
'''))
#PROCESSAMENTO DE DADOS

calculoPagamento1 = precoProduto - (precoProduto * 0.10) 
calculoPagamento2 = precoProduto -(precoProduto * 0.05)
calculoPagamento3 = precoProduto / 2
calculoPagamentoJuros4 = precoProduto + (precoProduto * 0.20)

# SAÍDA DE DADOS

if formaPagemento == 1 :
    print('Voce deve pagar R$ ',calculoPagamento1,)

elif formaPagemento == 2 :
    print('voce deverá pagar R$', calculoPagamento2)

elif formaPagemento == 3 :
    print('A duas parcelas serão de R$ ',calculoPagamento3)

elif formaPagemento == 4 : 
    
     parcelas = int(input('quantas parcelas ? '))
     print('O valor a ser pago R$ ', calculoPagamentoJuros4)
     calculoParcelas = precoProduto / parcelas 
     print('As parcelas são de R$ ',calculoParcelas)
else :
    print('Digite um número entre 1 e 4 !')