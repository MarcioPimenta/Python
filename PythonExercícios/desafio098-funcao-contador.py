import time


def contador(inicio, fim, passo=1):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        print(f'Não é possível contar com passo 0. Considerei passo igual 1.')
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    time.sleep(1)
    if inicio < fim:
        for n in range(inicio, fim + 1, passo):
            print(f'{n} ', end='', flush=True)
            time.sleep(0.5)
        print('Fim!')
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='', flush=True)
            time.sleep(0.5)
            c -= passo
        print('Fim!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
