valores = []
c = 0

while True:
    c += 1
    num = (int(input(f'Digite o {c}º valor: ')))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
valores.sort()
print('-=' * 30)
print(f'Você digitou os valores {valores}')
