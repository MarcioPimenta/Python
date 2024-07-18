num = int(input('Digite um número: '))
raz = int(input('Digite a razão: '))
fim = num + (10 * raz)
termo = num

while termo < fim:
    print(termo, end='-> ')
    num += raz
    termo = num
print('Fim')
