#faça um porgrama que leia tres numeros e mostre qual é o maior e qual é o menor
from time import sleep
a = int(input('Digite o Primeiro Valor: '))
b = int(input('Digite o Segundo Valor:  '))
c = int(input('Digite o Terceiro Valor: '))
# Verificando quem é menor
menor = a
if b<a and b<c:
        menor = b
if c<a and c<b:
        menor = c
# Verificando quem é o maior
maior = a 
if b>a and b>c:
        maior = b
if c>a and c>b:
        maior = c
print('Processando...')
sleep(10)
print('O menor valor digitado foi {}'.format(menor)) 
print('O maior valor digitado foi {}'.format(maior)) 