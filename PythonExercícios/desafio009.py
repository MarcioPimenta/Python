x = int(input('Digite o valor da tabuada que deseja saber: '))
print('-'*12)

for i in range(1, 11):
    print('{} X {:2} = {}'.format(x, i, x*i))

print('-'*12)
