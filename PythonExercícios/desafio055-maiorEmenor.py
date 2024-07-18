maior = 0
menor = 0
pesado = ''
leve = ''

for c in range(1, 6):
    nome = input('{}. Nome: '.format(c))
    peso = float(input('Peso: (Kg) '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            pesado = nome
        if peso < menor:
            menor = peso
            leve = nome
print('O(A) mais pesado(a) é {}, pesando {}Kg.'.format(pesado.capitalize(), maior))
print('O(A) menos pesado(a) é {}, pesando {}Kg.'.format(leve.capitalize(), menor))
