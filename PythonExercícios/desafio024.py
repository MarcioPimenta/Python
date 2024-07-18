#feito certo completo
cidade = str(input('Digite o nome da sua cidade: ')).strip()
inicia = cidade.upper()
Inicia = inicia.split()

if 'SANTO' in Inicia[0]:
    print('Sua cidade tem o nome iniciado por "Santo".')
else:
    print('Sua cidade não tem o nome iniciado por "Santo".')