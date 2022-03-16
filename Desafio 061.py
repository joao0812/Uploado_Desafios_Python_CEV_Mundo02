n1 = int(input('Digite um número: '))
razao = int(input('Digite um valor para razão: '))
aux = 1

while aux != 11:
    if aux == 1:
        print('{}° Termo: {}'.format(aux, n1))
    else:
        n1 = n1 + razao
        print('{}° Termo: {}'.format(aux, n1))

    aux += 1
