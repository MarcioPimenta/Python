from random import randint
from time import sleep

computador = randint(0, 10)
print('Sou o computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > 10:
            print('Escolha um número dentro do intervalo!')
        else:
            if jogador > computador:
                print('Menos...')
            elif jogador < computador:
                print('Mais...')
print('Parabéns! Acertou com {} tentativas.'.format(palpites))
