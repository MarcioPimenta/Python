#feito
print('{:=^40}'.format(' LOJAS PIMENTA '))
preco = float(input('Qual o valor do(s) produto(s)? R$'))
pagamento = int(input('Qual a condição de pagamento?\n0 - À vista\n1 - cartão em 1x\n2 - cartão em 2x\n3 - cartão +3x\n'))

if pagamento == 0:
    valor = preco * 0.90
    print('O valor é R${:.2f}, você obteve um desconto de 10%.'.format(valor))
elif pagamento == 1:
    valor = preco * 0.95
    print('O valor é R${:.2f}, você obteve 5% de desconto.'.format(valor))
elif pagamento == 2:
    parcelas = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcelas))
    print('O valor total é R${:.2f}.'.format(preco))
elif pagamento == 3:
    valor = preco * 1.20
    vezes = int(input('Quantas parcelas? '))
    parcelas = valor / vezes
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(vezes, parcelas))
    print('O valor total é R${:.2f}. Com 20% de juros.'.format(valor))
else:
    print('\033[4;30;41mOpção inválida. Escolha um dos métodos de pagamento.\033[m')
