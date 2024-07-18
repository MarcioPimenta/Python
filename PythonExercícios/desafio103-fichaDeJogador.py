def ficha(jogador='<desconhecido>', gols=''):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols.isnumeric():
        gol = int(gols)
    else:
        gol = 0
    return f'O jogador {jogador} fez {gol} gols no campeonato.'


print('-'*30)
jog = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
print(ficha(jog, gol))
