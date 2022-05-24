pp = float(input('Qual preco do item que você está comprando? R$ '))
desc = pp - (pp * 5 / 100)
print('O preco do item e R${: .2f}, com desconto de 5% ficou R${: .2f}.'.format(pp, desc))


