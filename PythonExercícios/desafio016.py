'''
import math
num = float(input('digite um número: '))
inteira = math.trunc(num)
print('O número {} tem a parte inteira {}.'.format(num, inteira))

from math import trunc
num = float(input('Digite um número: '))
inteira = trunc(num)
print('O número {} tem a parte inteira {}.'.format(num, inteira))
'''

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, int(num)))