from time import sleep

def ajuda(str):
        print(f'\033[30;44m~'*40)
        print(f'{f"Acessando o manual do comando '{resp}'":^40}')
        print(f'~'*40)
        print(f'\033[30;47m')
        sleep(1)
        return help(resp)


# programa principal
while True:
    print('\033[30;43m~'*30)
    print(f'{'SISTEMA DE AJUDA PYHELP':^30}')
    print(f'~'*30)
    resp = str(input('\033[mFunção ou Biblioteca (fim p/ sair) > '))
    sleep(1)
    if resp.upper() == 'FIM':
        print(f'\033[30;41m~'*20)
        print(f'{'ATÉ LOGO!':^20}')
        print(f'~'*20)
        break
    else:
        print(ajuda(resp))
