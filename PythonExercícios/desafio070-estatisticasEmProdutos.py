c = soma = prodcaro = precobarato = preco = 0
prodbarato = ''
print('-' * 40)
print('{:^40}'.format('PIMENTA ATACADISTA'))
print('-' * 40)
while True:
    c += 1
    prod = str(input(f'Nome do {c}º produto: ')).strip().upper()
    preco = float(input(f'Valor do {c}º produto: R$'))
    soma += preco
    if c == 1 or preco < precobarato:
        precobarato = preco
        prodbarato = prod.capitalize()
    """else:
        if preco < precobarato:
            precobarato = preco
            prodbarato = prod.capitalize()
    """
    if preco > 1000:
        prodcaro += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi R${soma:.2f}.')
print(f'{prodcaro} produto(s) custou(aram) mais de R$1000,00.')
print(f'O produto mais barato foi o {prodbarato}, que custa R${precobarato:.2f}.')
