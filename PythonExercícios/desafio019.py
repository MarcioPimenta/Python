import random
nomes = []
nome = input('Qual o nome do aluno? ')
while nome != '':
    nomes.append(nome)
    nome = input('Qual o nome do aluno? ')
print(nomes)
escolhido = random.choice(nomes)
print('O aluno {} foi o escolhido pra apagar o quadro.'.format(escolhido))
