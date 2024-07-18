valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {c}: ')))

print('=-' * 30)
print(f'Você digitou os valores {valores}')

maior = max(valores)
print(f'O maior valor foi {maior}, que apareceu na(s) posição(ões) ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()

menor = min(valores)
print(f'O menor valor foi {menor}, que apareceu na(s) posição(ões) ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
