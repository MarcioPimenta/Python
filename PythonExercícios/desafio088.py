import random
import time

num = list()
jogos = list()
i = 1
print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
while i <= n:
    c = 0
    while True:
        numeros = random.randint(1, 60)
        if numeros not in num:
            num.append(numeros)
            c += 1
        if c >= 6:
            break
    num.sort()
    jogos.append(num[:])
    num.clear()
    i += 1

print('-=' * 3, f'SORTEANDO {n} JOGOS ', '-=' * 3)
for j in range(len(jogos)):
    print(f'JOGO {j+1}: {jogos[j]}')
    time.sleep(0.8)
print('-=' * 3, f'{'BOA SORTE':^18}', '-=' * 3)
