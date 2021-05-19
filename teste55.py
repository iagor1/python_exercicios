print('digite valores, pra parar digite 999.')

num = c = soma = 0 # essa gambiarra foi antes da aula de break 

while num != 999:
    num= int(input('digite um número : '))
    c+=1
    soma += num
    
print('a soma entre eles é ',soma-999)
print('a total de numeros é', c-1)