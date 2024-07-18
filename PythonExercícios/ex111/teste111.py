from ex111.utilidadescev import moeda
from ex111.utilidadescev import dado
# from ex111.utilidadescev import moeda, dado

p = float(input('Digite o preço: R$'))
aum = float(input('Deseja aumentar qual porcentagem? '))
dim = float(input('Deseja diminuir qual porcentagem? '))
moeda.resumo(p, aum, dim)
