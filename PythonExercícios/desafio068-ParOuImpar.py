from random import randint
c = 0
while True:
    esc = int(input('Par[0] ou Ímpar[1]? '))
    if esc > 1:
        print('Valor inválido!')
    else:
        comp = randint(0, 5)
        pessoa = int(input('Digite um valor até 5: '))
        if pessoa > 5:
            print('Escolha um valor no intervalo informado.')
        else:
            soma = pessoa + comp
            res = soma % 2
            if res == 0:
                aposta = 'par'
            else:
                aposta = 'ímpar'
            if esc != res:
                print(f'Você perdeu! Você jogou {pessoa} e o computador {comp}. Total de {soma}, que é {aposta}.')
                break
            else:
                c += 1
                print(f'Você venceu! Você jogou {pessoa} e o computador {comp}. Total de {soma} que é {aposta}.')
print(f'Foram {c} vitórias seguidas.')
