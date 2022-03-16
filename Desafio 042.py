from math import fabs, hypot
n1 = float(input('Digite o valor de um lado do triângulo: '))
n2 = float(input('Digite o valor do outro lado do triângulo: '))
n3 = float(input('Digite o valor do outro lado do triângulo: '))

if fabs(n3 - n2) < n1 < n2 + n3 and fabs(n3 - n1) < n2 < n1 + n3 and fabs(n1 - n2) < n3 < n2 + n1:
    print('\33[;32mTRIÂNGULO APROVADO\33[m')
    if n1 == n2 == n3:
        print('Tipo do Triângulo: \33[;33mEQUILÁTERO\33[m')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('Tipo do Triângulo: \33[;33mESCALENO\33[m')
        if hypot(n1, n2) == n3 or hypot(n3, n1) == n2 or hypot(n3, n2) == n1:
            print(' Modelo: \33[;33mRETANGULO\33[m')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Tipo do Triângulo: \33[;33mISÓCELES\33[m')

