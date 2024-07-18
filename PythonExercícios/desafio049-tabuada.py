n = int(input('Número que deseja saber a tabuada: '))
for c in range(1, 11):
    print('{:2} x {:2} = {:3}'.format(n, c, n*c))
print('Fim')