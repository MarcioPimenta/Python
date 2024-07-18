num = int(input('Digite um número: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        div += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido por {} vezes.'.format(num, div))
if div == 2:
    print('Portanto é primo.')
else:
    print('Portanto não é primo.')