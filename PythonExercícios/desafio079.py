valores = []
c = 0

while True:
    c += 1
    while True:
        num = (int(input(f'Digite o {c} valor: ')))
        if num not in valores:
            break
    valores.append(num)
    print('Valor adicionado com sucesso...')
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
valores.sort()
print('-=' * 30)
print(f'Você digitou os valores {valores}')
