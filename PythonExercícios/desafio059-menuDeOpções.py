from time import sleep
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))

r = 0

while r != 5:
    print('=-=' * 10)
    r = int(input('''Opções:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    >>>> Opção escolhida: '''))
    if r > 5:
        print('Opção inválida!\nEscolha uma opção válida.')
    else:
        if r == 1:
            print('{} + {} = {}'.format(n1, n2, n1 + n2))
        if r == 2:
            print('{} x {} = {}'.format(n1, n2, n1 * n2))
        if r == 3:
            if n1 == n2:
                print('Não tem maior, ambos tem o mesmo valor.')
            elif n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
            else:
                print('{} é maior que {}.'.format(n2, n1))
        if r == 4:
            n1 = int(input('Digite um novo 1° valor: '))
            n2 = int(input('Digite um novo 2° valor: '))
        if r == 5:
            print('Saindo...')
            print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
