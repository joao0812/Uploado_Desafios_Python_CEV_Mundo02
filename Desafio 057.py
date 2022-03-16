aux = True
while aux == True:
    sexo = input('Digite sua sexualidade [M/F]: ').upper()
    if sexo == 'F' or sexo == 'M':
        aux = False
    else:
        print('{:^40}'.format('\33[;31mATENÇÃO\33[m'))
        print('{:^40}'.format('Digite M ou F para continuar'))
        print('-----------------------------------------------')

print('\33[;32mConcluído!\33[m')