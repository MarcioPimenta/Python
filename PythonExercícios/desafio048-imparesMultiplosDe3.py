s = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        s += c
        cont += 1
        # print(c)
print('Foram somados {} valores ímpares e múltiplos de 3, e o valor da sua soma é {}.'.format(cont, s))

""" para otimizar o código
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        #print(c, end=' ')
        soma += c
print('A soma de todos os valores solicitados é {}.'.format(soma))
"""
