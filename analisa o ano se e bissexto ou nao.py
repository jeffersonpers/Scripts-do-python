# analisa o ano se e bissexto ou não
from datetime import date
from time import sleep
ano = int(input('Que ano você quer analisar ? Coloque 0 para analisar o ano atual:'))
print('Checando os calendários...')
sleep(8)
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {:.0f} é BISSEXTO Ou seja fevereiro tem 29 dias'.format(ano))
else:
    print('O ano {:.0f} não e BISSEXTO ou seja fevereiro tem 28 dias'.format(ano))