dias = float(input('Quantos dias alugados? '))
kms = float(input('Quantos km rodados? '))
dia = dias * 60
km = kms * 0.15
total = dia + km
print('O total a pagar é R${:.2f}'.format(total))