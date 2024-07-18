s = 0
i = 0
p = []
for c in range(1, 7):
    n = int(input('{}. Digite um valor: '.format(c)))
    if n % 2 == 0:
        s += n
        i += 1
        p.append(n)
print('Foram informados {} valores pares, e soma deles é {}.'.format(i, s))
print('Os valores pares são {}.'.format(p))
