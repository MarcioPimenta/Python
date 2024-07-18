import random

import time

num = random.randint(0, 10)
esc = 11
tentativa = 0

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('Pensando....')
time.sleep(1)
print('Pronto')
print('-=-' * 20)

while esc != num:
    num = random.randint(0, 10)
    # print(num)
    esc = int(input('Qual número o computador pensou? '))
    if esc > 10:
        print('Número inválido. Tente novamente.')
    else:
        tentativa += 1
        if esc == num:
            print('Parabéns!!! Você me venceu. Eu pensei no {} e você escolheu o {}.'.format(num, esc))
        else:
            print('Não foi dessa vez. Eu pensei no {} e você escolheu o {}.'.format(num, esc))
            print('Pensando....')
            time.sleep(1)
            print('Pronto')

print('Você precisou de {} tentativas para me vencer.'.format(tentativa))
