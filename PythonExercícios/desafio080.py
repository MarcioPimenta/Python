valores = []
maior = menor = 0

for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if c == 0:
        maior = menor = num
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        maior = max(valores)
        menor = min(valores)
        if num > maior:
            valores.append(num)
            print('Adicionado ao final da lista...')
        elif num < menor:
            valores.insert(0, num)
            print('Adicionado no início da lista...')
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
