num = int(input('Digite um número: '))
print('Digite 999 caso queira parar.')
soma = 0
c = 0

while num != 999:
    if num != 999:
        soma += num
        c += 1
        num = int(input('Digite outro número: '))
print('Foram digitados {} números, e sua soma é {}.'.format(c, soma))
