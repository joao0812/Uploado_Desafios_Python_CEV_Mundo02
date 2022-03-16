#MELHORAR CONTROLE
aux = True
aux2 = True
while aux == True:
    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Digite o 2° número: '))
    print('{:^40}'.format('\33[;34mEscolha a operação:\33[m'))
    ope = int(input('''        [1] Soma
        [2] Multiplicação
        [3] Achar o maior número
        [4] Para escolher novos números
        [5] para sair do programa
        ➔ '''))
    if ope == 1:
        print('{:.2f} + {:.2f} = \33[;33m{:.2f}\33[m'.format(n1, n2, n1+n2))
        perg = input('Gostaria de utilizar o software novamente? [S/N]: ').upper().strip()
        while perg not in 'SN':
            print('{:^40}'.format('\33[;31mCOMANDO INVÁLIDO!\33[m,\nTente novamente'))
            perg = input('Gostaria de utilizar o software novamente? [S/N]: ').upper().strip()
        if perg == 'N':
            aux = False
    elif ope == 2:
        print('{:.2f} * {:.2f} = \33[;33m{:.2f}\33[m'.format(n1, n2, n1 * n2))
        perg = input('Gostaria de utilizar o software novamente? [S/N]: ').upper().strip()
        while perg not in 'SN':
            print('{:^40}'.format('\33[;31mCOMANDO INVÁLIDO!\33[m,\nTente novamente'))
            perg = input('Gostaria de utilizar o software novamente? [S/N]: ').upper().strip()
        if perg == 'N':
            aux = False
    elif ope == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
            aux = False
        elif n1 == n2:
            print('{} = {}'.format(n1, n2))
        else:
            print('{} < {}'.format(n1, n2))
        perg = input('Gostaria de utilizar o software novamente? [S/N]: ').upper().strip()
        while perg not in 'SN':
            print('{:^40}'.format('\33[;31mCOMANDO INVÁLIDO!\33[m,\nTente novamente'))
            perg = input('Gostaria de utilizar o software novamente? [S/N]: ').upper().strip()
        if perg == 'N':
            aux = False
    elif ope == 4:
        print('Escolha outros valores: ')
    elif ope == 5:
        print('\33[;33mPROCESSO ENCERRADO\33[m')
        aux = False
        aux2 = False
    else:
        print('{:^40}'.format('\33[;31mDIGITO INVALIDO\33[m\nTente novamente'))
if aux2 == True:
    print('{:^40}'.format('\33[;32mConcluído\33[m\nProcesso incerrado!'))


