print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Deseja saber quantos número da Sequência de Fibonacci? '))
termos = 3
a = 0
b = 1
print('{}-> {}'.format(a, b), end='-> ')

while termos <= n:
    c = a + b
    print(c, end='-> ')
    a = b
    b = c
    termos += 1
print('Fim')
