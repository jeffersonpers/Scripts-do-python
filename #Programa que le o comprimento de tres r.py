#Programa que le o comprimento de tres retas e retorna se da pra formar um triangulo ou não
from time import sleep
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
 print('Analisando as possibilidades...')
 sleep(10)
 print('Os segmentos acima podem Formar triângulo!')
else:
    print('Analisando as possibilidades...')
    sleep(10)
    print('Os segmentos acima não forma um triângulo')