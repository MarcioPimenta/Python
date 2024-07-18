valores = []
pares = []
impares = []
c = 0

while True:
    c += 1
    num = int(input(f'Digite o {c}° valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
