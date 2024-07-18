#feito parcialmente certo
frase = str(input('Digite sua frase: ')).strip()

print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('O 1º "A" aparece na posição {}'.format(frase.upper().find('A') + 1))
print('O último "A" aparece na posição {}'.format(frase.upper().rfind('A') + 1))
