#não feito
num = int(input('Informe um número: '))

print('Analisando o número {}'.format(num))
un = num // 1 % 10
dz = num // 10 % 10
ct = num // 100 % 10
mi = num // 1000 % 10
print('Unidade: {}'.format(un))
print('Dezena: {}'.format(dz))
print('Centena: {}'.format(ct))
print('Milhar: {}'.format(mi))
