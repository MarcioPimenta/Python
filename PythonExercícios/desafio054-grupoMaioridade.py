import datetime

atual = datetime.date.today().year
maior = []
menor = []
m = 0
n = 0

for c in range(1, 8):
    nome = str(input('{}. Nome: '.format(c)))
    nasc = int(input('Ano de nascimento: '))
    if atual - nasc >= 21:
        maior.append(nome)
        m += 1
    elif atual - nasc < 21:
        menor.append(nome)
        n += 1
print('Dessas 7 pessoas {} são maiores de 21 anos.'.format(m))
print('São elas: ')
print(maior)
print('Menores de 21 anos são {}.'.format(n))
print('E são elas: ')
print(menor)
