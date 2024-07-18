#feito
import datetime

nasc = int(input('Qual o ano de nascimento do atleta? '))
hoje = datetime.date.today().year
idade = hoje - nasc

if idade < 10:
    print('IDADE: {} anos. CATEGORIA MIRIM.'.format(idade))
elif idade < 15:
    print('IDADE: {} anos. CATEGORIA INFANTIL.'.format(idade))
elif idade < 20:
    print('IDADE: {} anos. CATEGORIA JUNIOR.'.format(idade))
elif idade < 21:
    print('IDADE: {} anos. CATEGORIA SÊNIOR.'.format(idade))
else:
    print('IDADE: {} anos. CATEGORIA MASTER.'.format(idade))
