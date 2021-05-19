s = c = 0 
while True:
    n = int(input('digite um valor [999 pra parar] : '))
    if n == 999:break
    s+=n
    c+=1
print(f'fim. A soma de todos foi {s} você somou {c} valores')