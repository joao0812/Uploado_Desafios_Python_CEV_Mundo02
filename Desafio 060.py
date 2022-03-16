n1 = int(input('Digite um número: '))
fatorial = 1
aux = 0
while n1 != 0:
    fatorial = fatorial * (n1)
#   print(fatorial)
#   print(aux)
    n1 = n1 - 1
    aux += 1
print('O fatorial de \33[;33m{}\33[m vale: \33[;33m{}\33[m'.format(aux, fatorial))