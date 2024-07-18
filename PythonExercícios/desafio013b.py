produto = float(input('Qual o valor do produto escolhido? R$'))
avista = produto * 0.90
parcelado = produto * 1.08
print('O valor do seu produto é R${:.2f}, à vista fica R${:.2f}, parcelado fica por R${:.2f}.'.format(produto, avista, parcelado))
