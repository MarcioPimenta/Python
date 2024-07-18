expr = str(input('Digite sua expressão: '))
parenteses = []

for simbolo in expr:
    if simbolo == '(':
        parenteses.append('(')
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
print(parenteses)
if len(parenteses) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
