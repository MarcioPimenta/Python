num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
par = ' '
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
for n in num:
    if n % 2 == 0:
      par += str(n)
if par != ' ':
    print(f'Os valores pares digitados foram: ')
    for c in range(len(par)):
        print(par[c], end=' - ')