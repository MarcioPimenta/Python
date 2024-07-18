from random import randint
from time import sleep

lista = list()


def sorteia(lst):
    c = 0
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    sleep(1)
    while True:
        num = randint(1, 10)
        lst.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.5)
        c += 1
        if c >= 5:
            break
    print('PRONTO!')


def somaPar(lst):
    tot = 0
    for n in lst:
        if n % 2 == 0:
            tot +=n
    print(f'Somando os valores pares de {lista}, temos {tot}.')


#programa principal
sorteia(lista)
somaPar(lista)
