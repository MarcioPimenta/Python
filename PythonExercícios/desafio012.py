preco = float(input('Qual o preço do produto? R$'))
npreco = 0.95 * preco
print('O produto de R${:.2f}, está na promoção por R${:.2f}.'.format(preco, npreco))