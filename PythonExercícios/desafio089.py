import time

aluno = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
        if res in 'SN':
            break
    if res == 'N':
        break
print('-='*20)
#print(aluno)
print(f'{'Nº':<5}{'NOME':<15}{'MÉDIA':>8}')
print('-' * 40)
for a in range(len(aluno)):
    print(f'{a:<5}', f'{aluno[a][0]:<15}', f'{aluno[a][2]:>8.1f}')
time.sleep(2)
while True:
    print('-' * 40)
    e = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if e == 999:
        print('FINALIZANDO...')
        break
    if e >= len(aluno):
        print('Escolha um aluno válido!!!')
    else:
        print(f'Notas de {aluno[e][0]} são {aluno[e][1]}.')
print(f'<<<VOLTE SEMPRE>>>')
