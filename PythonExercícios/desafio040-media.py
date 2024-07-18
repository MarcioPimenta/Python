#feito
n1 = float(input('Nota 1ª prova: '))
n2 = float(input('Nota 2ª prova: '))
media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO!!! Média: {:.1f}.'.format(media))
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO!!! Média: {:.1f}.\nEstude Mais.'.format(media))
elif media >= 7:
    print('APROVADO!!! BOAS FÉRIAS. Média: {:.1f}'.format(media))
