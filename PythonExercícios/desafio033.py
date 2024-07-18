n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
men = 0
mai = 0

if n1 < n2 and n1 < n3:
    men = n1
elif n2 < n1 and n2 < n3:
    men = n2
else:
    men = n3

print('O menor valor é {:.1f}.'.format(men))

if n1 > n2 and n1 > n3:
    mai = n1
elif n2 > n1 and n2 > n3:
    mai = n2
else:
    mai = n3

print('O maior valor é {:.1f}.'.format(mai))
