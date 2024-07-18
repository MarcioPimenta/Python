print('=*=' * 20)
p = int(input('1º termo: '))
r = int(input('Passo: '))
d = p + (10 * r)
print('=*=' * 20)


for c in range(p, d, r):
    print(c, end='-> ')
print('Fim')
