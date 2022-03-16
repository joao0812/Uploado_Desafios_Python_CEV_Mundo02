n1 = int(input('Digite um número: '))

if n1 == 2 or n1 == 3 or n1 == 5:
    print('O número {} é Primo!'.format(n1))
elif n1%2 == 0 or n1%3 == 0 or n1%5 == 0:
    print('O número {} não é Primo'.format(n1))
else:
    print('O número {} é Primo!'.format(n1))
