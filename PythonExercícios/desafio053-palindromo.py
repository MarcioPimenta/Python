frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # macete do fatiamento que só funciona em python
'''
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('Temos um Palíndromo!')
else:
    print('A frase não é palíndromo!')
