num = int(input('Digite um número: '))
raz = int(input('Digite a razão: '))
termo = int(input('Digite quantos termos quer mostrar: '))
fim = num + (termo * raz)
valor = num

while valor < fim:
    print(valor, end='-> ')
    num += raz
    valor = num
print('Fim')
