#esse programa calcula multa para carro que tiver acima de 80 km por hora cada km excedente ele calcula 7 reais por km

velocidade = float(input('Qual e a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
