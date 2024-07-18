num = int(input('Digite um valor que deseja saber o fatorial: '))
n = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fat *= n
    n -= 1
print(fat)
print('{}! é {}'.format(num, fat))
