
n1 = int(input('Digite um número: '))
conve = int(input('1 para Binário\n2 para Octal\n3 para Hexadecimal\nDigite o número correspondente para a operação que deseja realizar: '))
aux = True

while aux == True:
    if conve == 1:
        print('O valor {} em Binário fica: {}'.format(n1, bin(n1)[2:]))
        aux = False
    elif conve == 2:
        print('O valor {} em Octal fica: {}'.format(n1, oct(n1)[2:]))
        aux = False
    elif conve == 3:
        print('O valor {} em Hexadecimal fica: {}'.format(n1, hex(n1)[2:]))
        aux = False
    else:
        print('\33[1;31mERRO!\33[m')
        conve = int(input('Digite um número presente nas opções\n1 para Binário\n2 para Octal\n3 para Hexadecimal\nTente novamente: '))

print('\33[1;33mFIM DA OPERAÇÂO\33[m')
