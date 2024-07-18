def metade(n=0, formato=False):
    """
    :param n: valor informado pelo usuário
    :param formato: se deseja formatação monetária
    :return: retorna o valor da metade do valor informado, podendo estar formatado ou não.
    """
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    """
    :param n: valor informado pelo usuário
    :param formato: se deseja ou não formatação monetária
    :return: retorna o dobro do valor informado, podendo ou não estar formatado
    """
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, acres=0, formato=False):
    """
    :param n: valor informado pelo usuário
    :param acres: porcentagem a ser acrescida sobre o valor informado
    :param formato: se deseja ou não formatação monetária
    :return: retorna o valor acrescido da porcentagem escolhida, podendo ou não estar formatado
    """
    aum = n + ((n * acres) / 100)
    return aum if formato is False else moeda(aum)


def diminuir(n=0, decresc=0, formato=False):
    """
    :param n: valor informado pelo usuário
    :param decresc: porcentagem a ser diminuida sobre o valor informado
    :param formato: se deseja ou não formatação monetária
    :return: retorna o valor decrescido da porcentagem escolhida, podendo ou não estar formatado
    """
    dim = n - ((n * decresc) / 100)
    return dim if not formato else moeda(dim)


def moeda(preco=0, moeda='R$'):
    """
    :param preco: valor informado pelo usuário
    :param moeda: representação da moeda escolhida
    :return: retorna o valor informado com a formatação monetária escolhida
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(n=0, aum=0, dim=0):
    print('-'*50)
    print(f'{'RESUMO DO VALOR':^50}')
    print('-'*50)
    print(f'Preço analisado: \t{moeda(n)}') # \t pra tabular, assim aparece de maneira mais bonita
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(n, dim, True)}')
    print('-'*50)
