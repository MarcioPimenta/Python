# não funcionou, loop infinito, não para mesmo com a resposta desejada
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite seu sexo: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso.')
else:
    print('Sexo Feminino registrado com sucesso.')
