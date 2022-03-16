soma = 0
desc = ' '

for i in range(0, 6):
    n1 = int(input('Digite um número: '))
    if n1%2 == 0:
        soma = soma + n1
    else:
        desc = desc + str(n1) + ' '
        lista = desc.split()

print('A soma total dos números páres: {}'.format(soma))
print('Números descartados na soma: {}'.format(lista))