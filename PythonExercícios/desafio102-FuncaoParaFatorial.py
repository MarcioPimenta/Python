def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    if show:
        f = 1
        for c in range(num, 0, -1):
            if c == 1:
                print(f'{c}', end='')
                f *= c
            else:
                print(f'{c} X ', end='')
                f *= c
        return f' = {f}.'
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f'{f}.'


# programa principal
fat = int(input('Deseja saber o fatorial de qual número? '))
while True:
    mostrar = str(input('Deseja mostrar a conta? [S/N] ')).strip().upper()[0]
    if mostrar == '':
        mostrar = 'N'
    if mostrar in 'SN':
        break
    print('Escolha somente 0-Não ou 1-Sim')
if mostrar == 'N':
    show = False
else:
    show = True
print(fatorial(fat, show))
help(fatorial)
