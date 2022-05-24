real = float(input('Quanto dinheiro você tem na carteira ? R$'))
dolar = real / 5.00
print('Com tanto R$ {:.2f} voce pode comprar o equivalente a U${:.2f}'.format(real, dolar))