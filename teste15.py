import math

hipotenusa = int (input('informe a hipotenusa : '))

cateto1 = int (input('informe o 1 cateto : '))

calculocateto = hipotenusa**2+cateto1**2

calculocateto = math.sqrt(calculocateto)

print('o valor da hipotenusa é', calculocateto)

