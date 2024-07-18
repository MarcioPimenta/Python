trabalhador = dict()

trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['carteira'] != 0:
    trabalhador['contratacao'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['contratacao'] + 35 - trabalhador['nascimento']

print('-=' * 30)
for k, v in trabalhador.items():
    print(f'  -{k} tem o valor {v}.')
