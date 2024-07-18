pessoas = list()
pessoa = dict()
mulheres = list()
totidade = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        if sexo in 'MF':
            break
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    totidade += pessoa['idade']
    pessoas.append(pessoa.copy())
    if sexo == 'F':
        mulheres.append(pessoa.copy())
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
        if res not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        if res in 'SN':
            break
    pessoa.clear()
    if res == 'N':
        break
print(pessoas)
print('-='*30)
print(f'A) Foram cadastradas {len(pessoas)} pessoa(s).')
media = totidade / len(pessoas)
print(f'B) A média de idade do grupo é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas na lista foram ', end='')
'''for p in pessoas: #assim não é preciso criar a lista mulheres como fiz na minha solução
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()'''
for p in mulheres:
    print(f'{p["nome"]} ', end='')
print('.')
print('D) Lista das pessoas que estão acima da média de idade:')
for p in pessoas:
    if p['idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ;', end='')
        print()
print()
print('<< Encerrado >>')
