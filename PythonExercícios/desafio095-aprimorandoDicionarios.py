time = list()
jogador = dict()
gols = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if res == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    e = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if e == 999:
        print('<< VOLTE SEMPRE! >>')
        break
    if e >= len(time):
        print(f'ERRO! Não existe jogador com código {e}! Tente Novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[e]['nome']}:')
        for i, g in enumerate(time[e]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
