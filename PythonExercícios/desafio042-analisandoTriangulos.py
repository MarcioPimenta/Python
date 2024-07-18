#feito
r1 = float(input('1ª reta: '))
r2 = float(input('2ª reta: '))
r3 = float(input('3ª reta: '))

maior = r1

if r2 > r1 and r2 > r3:
    maior = r2
elif r3 > r1 and r3 > r2:
    maior = r3

print('O maior lado é {}.'.format(maior))

if maior < r1 + r2 + r3 - maior:
    print('Forma triângulo. ', end='')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('É um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo isósceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('É um triângulo escaleno.')
else:
    print('Não forma triângulo.')
