pessoas = list()
dado = []
gordo = []
magro = []
pesado = leve = 0
c = 0

while True:
    c += 1
    dado.append(str(input(f'Qual o nome da {c}ª pessoa? ')))
    dado.append(float(input(f'Qual o peso da {c}ª pessoa em KG? ')))
    if c == 1:
        pesado = dado[:][1]
        leve = dado[:][1]
    else:
        if dado[:][1] > pesado:
            pesado = dado[:][1]
        if dado[:][1] < leve:
            leve = dado[:][1]
    pessoas.append(dado[:])
    dado.clear()
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break

print(pessoas)
print('-='*30)
print(f'O total de pessoas cadastradas é {c}.')
for p in pessoas:
    if p[1] == pesado:
        gordo.append(p[:][0])
print(f'O maior peso foi de {pesado:1}Kg. Peso de {gordo}')
for p in pessoas:
    if p[1] == leve:
        magro.append(p[:][0])
print(f'O menor peso foi de {leve:1}Kg. Peso de {magro}')
