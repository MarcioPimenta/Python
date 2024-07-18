from random import randint
from time import sleep

quina = []
jogo = list()
aposta = 0

while True:
    c = 0
    print(f'Sorteando jogo {aposta + 1}.')
    sleep(0.8)
    while True:
        numero = randint(1, 80)
        if numero not in jogo:
            jogo.append(numero)
            c += 1
        if c >= 5:
            break
    jogo.sort()
    quina.append(jogo[:])
    jogo.clear()
    aposta += 1
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break

for i, l in enumerate(quina):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('Boa sorte!')
