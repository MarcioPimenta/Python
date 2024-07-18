numeros = list()

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° valor: '))
    numeros.append(num)

numeros.sort()
print('-='*30)
print(numeros)
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=', ')
print()
print(f'Os valores ímpares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 1:
        print(n, end=', ')
print()
