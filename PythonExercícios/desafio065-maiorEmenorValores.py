r = 'S'
soma = 0
c = 0
maior = 0
menor = 0

while r != 'N':
    c += 1
    num = int(input('Digite um valor: '))
    soma += num
    if c == 1:
        maior = num
        menor = maior
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = soma / c
print('A soma entre todos os valores é {}.'.format(soma))
print('Foram digitados {} valores.'.format(c))
print('{} é a média entre os valores.'.format(media))
print('{} foi o maior valor e {} o menor.'.format(maior, menor))
