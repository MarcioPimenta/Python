def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        if ok:
            break
    return num


def leiaFloat(msg):
    ok = False
    while True:
        n = str(input(msg)).strip()
        if n == '':
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
            num = 0
            ok = True
        else:
            try:
                float(n)
                num = n
                ok = True
            except:
                print(f'\033[31mERRO: por favor, digite um número real válido.\033[m')
                continue
        if ok:
            break
    return num


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
