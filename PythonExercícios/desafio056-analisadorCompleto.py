soma = 0
velho = 0
hv = ''
novas = 0

for c in range(0, 4):
    print('_____ {}ª PESSOA _____'.format(c + 1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = int(input('Sexo:\n[1] masculino\n[2] feminino\n'))
    soma += idade
    if idade > velho and sexo == 1:
        velho = idade
        hv = nome
    if idade < 20 and sexo == 2:
        novas += 1

media = soma / 4

print('A média de idade do grupo é de {:.2f} anos.'.format(media))
if velho != 0:
    print('O homem mais velho é {}, com {} anos.'.format(hv.capitalize(), velho))
if novas != 0:
    print('Existe(m) {} mulher(es) abaixo dos 20 anos nesse grupo.'.format(novas))
