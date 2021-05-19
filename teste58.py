#tabuada 3.0
c=0
while True:
    n = int(input('digite um numero pra fazer a tabuada de multiplicação : '))
    if n <0:break
    for c in range(0, 10):
        c+=1
        print(f'{n} x {c} = {n*c}')        
print('fim.')
    