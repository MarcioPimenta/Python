# feito
peso = float(input('Qual o seu peso? (Kg) '))
alt = float(input('Qual sua altura? (m) '))
imc = float(peso / (alt ** 2))

print('O seu IMC é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25: # poderia ter colocado apenas if imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade Mórbida.')
