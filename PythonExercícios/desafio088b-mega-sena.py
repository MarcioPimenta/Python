import random
import time

lista = list()
apostas = list()
print('-=' * 30)
print(f'{'MEGA SENA':^60}')
print('-=' * 30)
n = int(input('Deseja sortear quantos jogos? '))
jogos = 1
while jogos <= n:
    c = 0
    while True:
        numero = random.randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            c += 1
        if c >= 6:
            break
    lista.sort()
    apostas.append(lista[:])
    lista.clear()
    jogos += 1

print('-=' * 10, f'{'SORTEANDO':^18}', '-='*10)

for i, l in enumerate(apostas):
    print(f'JOGO {i+1}: {l}')
    time.sleep(0.8)
print('-=' * 10, f'{'< BOA SORTE! >':^18}', '-=' * 10)
