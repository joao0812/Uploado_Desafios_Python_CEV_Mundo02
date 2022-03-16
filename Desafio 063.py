n1 = int(input('Digite até que termo gostaria de ver da sequência de Fibonacci\n➙ '))
aux = 0

while n1 != 0:
    if aux == 0:
        print('0 ➞', end=' ')
        prim = aux
        seg = 0
        # n1 -= 1
    elif aux == 1:
        print('1 ➞', end=' ')
        prim = 0
        seg = aux
        # n1 -= 1
    else:
        soma = prim + seg
        prim = seg
        seg = soma
        print('{} ➞'.format(soma), end=' ')
    n1 -= 1
    aux += 1
print('\33[32mCONCLUÍDO\33[m')