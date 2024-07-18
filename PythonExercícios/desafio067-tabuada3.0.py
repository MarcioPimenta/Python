n = 0
while True:
    c = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if n < 0:
        break
    # for c in range(1, 11):
        # print(f'{n} x {c} = {n*c}')
    while c <= 10:
        print(f'{n:2} x {c:2} = {n*c:3}')
        c += 1
    print('-' * 20)
print('Programa Tabuada Encerrado. Volte sempre!')
