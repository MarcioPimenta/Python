# feito
n1 = int(input('1º valor: '))
n2 = int(input('2° valor: '))

if n1 > n2:
    print('O 1° valor é o maior. {} > {}'.format(n1, n2))
elif n2 > n1:
    print('O 2° valor valor é o maior. {} > {}'.format(n2, n1))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais. {} = {}'.format(n1, n2))
