#aumento salarial - calcula uma porcentagem do salário e agrega ao salário
from time import sleep
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print('Processando...')
sleep(10)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. ' .format(salário, novo))