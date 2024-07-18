num = int(input('Digite um valor que deseja saber o fatorial: '))
fat = 1
print('Calculando {}! = '.format(num), end='')
for c in range(num, 0, -1):
    fat *= c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
print(fat)
