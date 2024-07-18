# feito
valor = float(input('Qual o valor da casa que você quer comprar? R$'))
sal = float(input("Qual o seu salário? R$"))
anos = int(input('Deseja parcelar em quantos anos? '))

prestacao = valor / (anos * 12)

if prestacao <= (sal * 0.3):
    print('Empréstimo aprovado!!!\nSerão {} parcelas de R${:.2f}.'.format(anos * 12, prestacao))
else:
    print('Empréstimo recusado.\nInfelizmente o valor da parcela é maior que 30% do seu salário.\nSalário: R${:.2f}.\nParcela: R${:.2f}'.format(sal, prestacao))

#print('{:.2f}'.format(prestacao))
