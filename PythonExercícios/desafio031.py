km = float(input('Qual a distância da viajem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(km))
'''
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
'''

preco = km * 0.50 if km <= 200 else km*0.45 #if simplificado

print('O valor a ser pago é R${:.2f}.'.format(preco))
