#feito
import datetime

sexo = int(input('Sexo:\n[1] MASCULINO\n[2] FEMININO\n'))

if sexo == 1:
    nasc = int(input('Em que ano você nasceu? '))
    hoje = datetime.date.today().year
    idade = hoje - nasc
    alist = nasc + 18

    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, hoje))

    if idade < 18:
        print('Você ainda vai se alistar ao completar 18 anos. Em {} ano(s).'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(alist))
    elif idade == 18:
        print('É hora de se alistar. Você tem 18 anos.')
    else:
        print('Sua data de alistamento já passou. Você deveria ter se alistado há {} ano(s).'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(alist))
else:
    print('Mulheres não tem alistamento militar obrigatório.')
