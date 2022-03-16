from random import randint

win = 0
while True:
    cpu = randint(0, 10)
    print('{:^40}'.format('\33[1;33mPAR OU ÍMPAR\33[m'))
    esc = input('Você quer ser Par ou Ímpar? [P/I] ').upper()
    p1 = int(input('Escolha um número: '))
    win += 1
    if esc == 'P':
        if (cpu + p1) % 2 != 0:
            result = 'Ímpar'
            break
    if esc == 'I':
        if (cpu + p1) % 2 == 0:
            result = 'Par'
            break
    print('\33[;32mWIN\33[m')
    print(f'Vitórias: {win}')
print('\33[;31mGAME OVER\33[m')
print(f'{p1} + \33[;33m{cpu}\33[m = {p1+cpu}', end=' ')
print(f'➝ {result}')
print(f'Total de vitórias: {win-1}/{win}')