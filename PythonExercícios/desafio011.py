alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))
area = alt * lar
lata = area / 2
print('Sua parede tem {}mX{}m3, totalizando uma área de {}m².\nSão necessárias {}l de tinta pra pintar sua parede.'.format(alt, lar, area, lata))