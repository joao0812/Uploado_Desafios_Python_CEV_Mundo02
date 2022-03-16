n1 = int(input('Digite um número: '))
razao = int(input('Digite um valor para razão: '))
aux = 1
cont = 0
while aux != 11:
    if aux == 1:
        print('{}° Termo: {}'.format(aux, n1))
        perg = input('Gostaria de saber o próximo termo? [S/N]: ').upper()
        if perg == 'N':
            aux = 10
            print(('\33[;31mPROCESSO ENCERRADO\33[m'))
    else:
        n1 = n1 + razao
        print('{}° Termo: {}'.format(aux, n1))
        if aux != 10:
            perg = input('Gostaria de saber o próximo termo? [S/N]: ').upper()
            if perg == 'N':
                aux = 10
                print(('\33[;31mPROCESSO ENCERRADO\33[m'))
    aux += 1
    cont += 1

if cont == 10:
    print(('\33[;33mPROCESSO CONCLUÍDO\33[m'))


# Da para dimunuir o código utilizando 2 while