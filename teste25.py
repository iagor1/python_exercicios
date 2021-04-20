a = int(input('digite um número e mostrará seu menor e maior : '))
b = int(input('digite outro número e mostrará seu menor e maior : '))
c = int(input('digite outro número e mostrará seu menor e maior : '))
#Menor ->
menor = a 

if b<a and b<c :
    menor = b 
if c<a and c<b :
    menor = c    
print('O menor deles é', menor)
#Maior ->
maior = c 
if b>c and b>a :
    maior = b
if a>c and a>b :
    maior = a
print('O maior é', maior)