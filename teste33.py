print('-'*30)
print('ANALISADOR DE TRIÂNGULOS ')
print('-'*30)

l1 = float(input('Digite um segmento : '))
l2 = float(input('Digite outro segmento : '))
l3 = float(input('Digite outro segmento : '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 :
    print('pode existir.')
    if l1 == l2 == l3 :
        print('é um triângulo equilátero')
    elif l1 != l2 != l3 != l1:
         print('é um triângulo escaleno.')
    else :
        print('é um isócele.')     
else : 
    print('não pode existir :( ')