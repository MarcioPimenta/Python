n = int(input('Digite um valor:'))
d = n*2
t = n*3
r = n**(1/2)
raiz = pow(n, (1/2)) #a função pow() é uma função que nos permite trabalhar com potencias
print('O valor escolhido é {},\nseu dobro é {},\nseu triplo é {} e sua raiz é {:.3f}'.format(n, d, t, r))
print('A raiz é {:.3f}.'.format(raiz))