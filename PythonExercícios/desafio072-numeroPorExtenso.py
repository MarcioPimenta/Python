extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
r = 'S'
c = 0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}.')
    c += 1
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print(f'Programa encerrado. Você leu {c} numeros.')
