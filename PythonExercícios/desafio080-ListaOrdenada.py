valores = []
maior = menor = 0

for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if c == 0 or num > maior:
        maior = menor = num
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-=' * 20)
print(f'Os valores digitados foram {valores}.')
