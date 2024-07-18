print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
r1 = float(input('Digite o valor da 1ª reta: '))
r2 = float(input('Digite o valor da 2ª reta: '))
r3 = float(input('Digite o valor da 3ª reta: '))

maiorLado = 0

if r1 > maiorLado:
    maiorLado = r1
if r2 > maiorLado:
    maiorLado = r2
if r3 > maiorLado:
    maiorLado = r3

print('O maior lado é {}.'.format(maiorLado))

if maiorLado < r1 + r2 + r3 - maiorLado:
    print('As retas formam um triângulo.')
else:
    print('Não forma triângulo.')
