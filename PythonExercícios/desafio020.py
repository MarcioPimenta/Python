'''
import random
nome = input('Qual o nome do aluno? ')
nomes = []
while nome != '':
    nomes.append(nome)
    nome = input('Qual o nome do aluno? ')

print(nomes)
random.shuffle(nomes)
print('A ordem é {}'.format(nomes))
'''

from random import shuffle
nome = input('Qual o nome do aluno? ')
nomes = []
i = 1
while nome != '':
    i += 1
    nomes.append(nome)
    nome = input('Qual o nome do {}º aluno? '.format(i))

print(nomes)
shuffle(nomes)
print('A ordem é {}'.format(nomes))
