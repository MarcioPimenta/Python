# from datetime import date (importando assim, ocupamos o espaço da memória,
# pois o arquivo fica disponível pro programa todo, então é melhor importar diretamente dentro da def
#  que assim utilizamos um espaço menor de memória)


def voto(ano=1900):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: voto negado.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: voto opcional.'
    else:
        return f'Com {idade} anos: voto obrigatório'


# programa principal
print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
