larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg *alt
print('Sua parede tem a dimensão de {} x {} e sua area e de {}m².'.format(larg, alt, area))
tinta = area / 2 
print('para pintar esse parede voce vai precisar de {}l de tinta e nao seja mao de vaca.'.format(tinta))