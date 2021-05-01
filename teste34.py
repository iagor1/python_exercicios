print('-'*40)
print('Calcule seu IMC')
print('-'*40)
peso = float(input('Digite seu peso : '))
altura = float(input('Digite sua altura com ponto Ex(1.70): '))
IMC = peso / (altura**2)
if IMC < 18.5 :
    print('Você está abaixo do peso.')
elif IMC > 18.5 and IMC <= 25:
    print('Voce está no peso ideal.')
elif IMC > 25 and IMC <= 30 :
    print('Voce está sobrepeso.')
elif IMC > 30 and IMC <= 40 :
    print('voce está obeso(a)')
else :
    print('obesidade mórbida.')

print('Seu IMC é : ',IMC)
