jogador = dict()
gols = []
totgols = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for n in range(partidas):
    gol = int(input(f'Quantos gols na partida {n+1}? '))
    gols.append(gol)
    #gols.append(int(input(f'Quantos gols na partida {n+1}? ')))
    totgols += gol
jogador['gols'] = gols[:]
jogador['tot'] = sum(gols)#esse método realiza a somatória dos itens da lista,
# assim não precisa criar a variável pra somar
jogador['total'] = totgols

print('-='*30)
print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for g in range(partidas):
    print(f'  => Na partida {g+1}, fez {jogador["gols"][g]} gols.')
'''for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
'''
print(f'Fez um total de {jogador["total"]} gols.')
