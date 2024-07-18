valores = []
c = 0

while True:
    c += 1
    num = int(input(f'Digite o {c}º valor: '))
    valores.append(num)
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
valores.sort(reverse=True)
print('-=' * 20)
print(f'Foram digitados {c} valores.') # em vez de colocar uma variável e ir somando,
# poderia simplesmente mostrar o len(valores)
print(f'Os valores digitados foram: {valores}.')
if 5 in valores:
    print(f'O valor 5 está na lista, na(s) posição(ões) ', end='')
    for i, v in enumerate(valores):
        if v == 5:
            print(f'{i+1}... ', end='')
else:
    print(f'O valor 5 não está na lista.')
print()
