c = 1
i = homem = mulher = 0
while True:
    idade = int(input(f'Idade {c}ª pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Sexo da {c}ª pessoa: [M/F] ')).strip().upper()[0]
    c += 1
    r = ' '
    if idade >= 18:
        i += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Temos {i} pessoa(s) maiores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
