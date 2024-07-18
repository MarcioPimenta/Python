# não fiz/ feito com a correção
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] converter para Binário\n[2] converter para Octal\n[3] converter para Hexadecimal')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    octal = oct(num)
    print('{} convertido para OCTAL é {}.'.format(num, octal[2:]))
elif opcao == 3:
    hexadecimal = hex(num)
    print('{} convertido para HEXADECIMAL é {}.'.format(num, hexadecimal[2:]))
else:
    print('Opção Inválida! Tente novamente.')
