from random import randint
from time import sleep
computador = randint (0, 100)#faz o computador "PENSAR'"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 100.Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei ? '))#jogador tenta adivinhar
print('Processando...')
sleep(10)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no  número {}'.format(computador, jogador))
