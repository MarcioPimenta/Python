print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('1° termo: '))
raz = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    cont += 1
print('Fim')
