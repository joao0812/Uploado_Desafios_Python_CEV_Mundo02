n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))

if n1 > n2:
    print('O Primeiro número {} é maior que o segundo {}'.format(n1, n2))
elif n1 < n2:
    print('O Primeiro número {} é menor que o segundo {}'.format(n1, n2))
elif n1 == n2:
    print('O Primeiro número é igual ao segundo {}'.format(n1))

