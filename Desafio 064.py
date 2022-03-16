n1 = 0
aux = 0
soma = 0
lista = ' '

while n1 != 999:
    n1 = int(input('Digite um número [999 para parar]: '))
    lista = lista + str(n1) + ' '
    aux += 1
    soma = soma + n1

lista = lista.split()
lista.remove('999')
print('Números digitados: \33[;33m{}\33[m números\nSoma entre os valores digitados: \33[;33m{}\33[m'.format(aux-1, soma-999))
print('Números digitados: {}'.format(lista))