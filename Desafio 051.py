n1 = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
soma = 0
dec = n1 + (10 - 1) * razao
for i in range(n1, dec + razao, razao):

    print('{}'.format(i), end=' \33[;31m→\33[m ')
print('FIM')