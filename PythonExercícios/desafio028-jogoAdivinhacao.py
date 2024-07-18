import random
#from random import randint
import time
#from time import sleep

num = random.randint(0, 5)#faz o computador 'pensar'(sortear um número)
#print(num)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('Pensando....')
time.sleep(2)
print('Pronto!')
print('-=-' * 20)

esc = int(input('Qual valor de 0 a 5 o computar pensou? '))#jogador tenta adivinhar
if esc > 5:
    print('Número inválido.')
else:
    if esc == num:
        print('PARABÉNS! Você conseguiu me vencer!\nEu pensei no {} e você escolheu o {}'.format(num, esc))
    else:
        print('GANHEI!!! \nTente novamente... \nEu pensei no número {} e não no {}!'.format(num, esc))
