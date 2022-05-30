# calcula o preco da sua passagem baseada nos km rodado abaixo de 200 igual a 50 centavos acima igual a 45 centavos
from time import sleep
distância = float(input('Qual é a distância da sua viagem? '))
print('Calculando...')
sleep(10)
if distância <= 200:
    preco = distância * 0.50
else:
    preco = distância * 0.45
print('E o preco da sua passagem será de R${:.2F}'.format(preco))