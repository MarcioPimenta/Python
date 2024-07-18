def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, acres=0):
    aum = n + ((n * acres) / 100)
    return aum


def diminuir(n=0, decresc=0):
    dim = n - ((n * decresc) / 100)
    return dim


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
