l = float(input('Digite a largura da sua parede em metros: '))
a = float(input('Digite a altura da sua parede em metros: '))
area = a*l
tinta = area/2
print('A área da sua parede é {:.2f}m² e vai precisar de {:.2f} litros de tinta.'.format(area, tinta))
