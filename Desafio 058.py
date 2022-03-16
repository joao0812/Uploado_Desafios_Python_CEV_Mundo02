from random import randint
aux = True
total = 0

while aux == True:
    cpu = randint(0, 10)
    p1 = int(input('Digite um número de 0 a 10: '))
    if p1 > 10 or p1 < 0:
        print('{:-^40}'.format('\33[;31mNÚMERO INVALIDO\33[m'))
        print('{:^40}'.format('Digite um número entre 0 e 10'))
    elif cpu == p1:
        aux = False
    else:
        print('{:^40}'.format('\33[;31mERROU!\33[m'))
        print('{:^40}'.format('\33[;33mTENTE NOVAMENTE\33[m'))
    total += 1
print('{:-^40}'.format('\33[;32mWIN\33[m'))
print('Total de jogadas: \33[;33m{}\33[m'.format(total))