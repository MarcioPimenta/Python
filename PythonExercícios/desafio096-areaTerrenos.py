def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:3.1f} X {comp:3.1f} é de {a:3.1f}m².')


print('Controle de Terrenos')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
