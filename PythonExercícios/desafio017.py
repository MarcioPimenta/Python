'''
oposto = float(input('Qual o comprimento do cateto oposto? '))
adj = float(input('Qual o comprimento do cateto adjacente? '))
hip = ((oposto**2) + (adj**2))**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(hi))