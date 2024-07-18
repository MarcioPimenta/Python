#feito certo completo

nome = str(input('Digite o nome completo: ')).strip()

nomeC = nome.split()
#print(nome)
#print(nomeC)

primeiro = nomeC[0]
ultimo = nomeC[-1]
#ultimo = nomeC[len(nome) -1 ] // irá fazer o mesmo que na linha de cima
print('primeiro nome = {}'.format(primeiro))
print('ultimo nome = {}'.format(ultimo))
