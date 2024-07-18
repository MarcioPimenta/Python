#feito parcialmente certo
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

nomeC = nome.split()
primeiro = nomeC[0]
total = len(nome) - nome.count(' ')
print('Seu nome tem ao todo {} letras'.format(total))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro, len(primeiro)))
