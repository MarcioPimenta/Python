from random import randint
from time import sleep

num = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('Pensando....')
sleep(1)
print('Pronto')
print('-=-' * 20)
tentativa = 1

esc = int(input('Qual valor o computador pensou? '))

while esc != num:
    if esc > 10:
        print('Número inválido.\nTente Novamente.')
    else:
        tentativa += 1
        if esc != num:
            print('Errou!!! Escolha outro número...')
            esc = int(input('Talvez o: '))
print('Parabéns!!! Você me venceu. Eu pensei no {} e você escolheu o {}.'.format(num, esc))
print('Você precisou de {} tentativas.'.format(tentativa))