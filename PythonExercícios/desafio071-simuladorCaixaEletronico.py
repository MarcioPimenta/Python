print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = int(input('Qual valor deseja sacar? '))
nota = 50
while True:
    if saque >= nota:
        notas = saque // nota
        saque = saque % nota
        print(f'Total de {notas} cédulas de R${nota}.')
    else:
        nota = 20
        if saque >= nota:
            notas = saque // nota
            saque = saque % nota
            print(f'Total de {notas} cédulas de R${nota}.')
        else:
            nota = 10
            if saque >= nota:
                notas = saque // nota
                saque = saque % nota
                print(f'Total de {notas} cédulas de R${nota}.')
            else:
                nota = 1
                if saque >= nota:
                    notas = saque // nota
                    saque = saque % nota
                    print(f'Total de {notas} cédulas de R${nota}.')
    if saque == 0:
        break
print('=' * 30)
print('Volte sempre! Tenha um bom dia!')
