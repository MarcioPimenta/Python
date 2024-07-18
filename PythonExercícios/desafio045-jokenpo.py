# feito
import random
import time

print('-=-' * 10)
print('{:^30}'.format('JOKENPÔ'))
print('-=-' * 10)

comp = random.randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
# print(comp)
voce = int(input('Escolha um opção:\n0 - PEDRA\n1 - PAPEL\n2 - TESOURA\n'))
print('JO')
time.sleep(0.4)
print('KEN')
time.sleep(0.4)
print('PÔ')
time.sleep(1)

print('+-'*20)
if comp == voce:
    print('\033[7;30mEMPATE!\033[m')
elif comp == 0 and voce == 1 or comp == 1 and voce == 2 or comp == 2 and voce == 0:
    print('\033[1;30;42mVocê ganhou!!!\033[m')
elif comp == 0 and voce == 2 or comp == 1 and voce == 0 or comp == 2 and voce == 1:
    print('\033[4;30;41mVocê perdeu!!!\033[m')
else:
    print('\033[7;30;41mOpção inválida. Escolha uma das opções!!!\033[m')

print('Você escolheu {} e o computador {}.'.format(itens[voce], itens[comp]))
print('+-'*20)
