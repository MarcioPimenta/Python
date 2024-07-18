'''

# as funções sin, cos e tan retornam os valores de radianos, não de graus, então temos que transformar o
# os graus em redianos antes de chamar a função, ou chamar uma função dentro de outra.
# ex.:
# ang = ...
# seno = math.sin(math.radians(ang))

import math

ang = float(input('Digite o ângulo que você deseja: '))

an = math.radians(ang)
seno = math.sin(an)
cosseno = math.cos(an)
tangente = math.tan(an)

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))
'''

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))

an = radians(ang)
seno = sin(an)
cosseno = cos(an)
tangente = tan(an)

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))
