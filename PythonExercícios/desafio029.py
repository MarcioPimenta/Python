vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Multado! Você excedeu o limite permitido que é de 80km/h.\nO valor da sua multa é R${:.2f}.'.format(multa))
print('Boa Viagem! Dirija com cuidado!!!')
