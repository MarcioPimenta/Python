salario = float(input('Qual o valor do seu salário? R$'))

if salario <= 1250.00:
    nsal = salario * 1.15
else:
    nsal = salario * 1.10

print('Seu salário de R${:.2f}, com aumento passa a ser R${:.2f}.'.format(salario, nsal))
