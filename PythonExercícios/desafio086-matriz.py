matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        pos = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(pos)

print('-='*30)
#print(matriz)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
