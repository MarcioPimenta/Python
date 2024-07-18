tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico', 'Cruzeiro',
          'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco da Gama', 'Sport',
          'América-MG', 'Vitória', 'Paraná')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 30)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 30)
print(f'A Chapecoense está na {tabela.index('Chapecoense')+1}ª posição.')
