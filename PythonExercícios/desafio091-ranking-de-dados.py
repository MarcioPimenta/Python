import random
import time
import operator

jogador = { 'jogador1': random.randint(1, 6),
            'jogador2': random.randint(1, 6),
            'jogador3': random.randint(1, 6),
            'jogador4': random.randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(0.8)

ranking = sorted(jogador.items(), key = operator.itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(0.8)