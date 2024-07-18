matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = coluna3 = maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para {i, j}: '))
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            coluna3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior valor da segunda linha é {maior}.')
