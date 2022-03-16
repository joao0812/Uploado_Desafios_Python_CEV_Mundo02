from time import sleep
from random import choice
aux = True
lista = ['Pedra', 'Papel', 'Tesoura']

while aux == True:
    cpu = choice(lista)
    print(cpu)
    p1 = input('Digite sua jogada (Pedra, Papel ou Tesoura): ')
    print('PEDRA...')
    sleep(1)
    print('PAPEL...')
    sleep(1)
    print('TESOURA...')
    sleep(1)
    if (cpu.upper() == 'PEDRA' and p1.upper() == 'PAPEL') or (cpu.upper() == 'TESOURA' and p1.upper() == 'PEDRA') or (cpu.upper() == 'PAPEL' and p1.upper() == 'TESOURA'):
        print('\33[1;32mVOCÊ GANHOU!\33[m')
        print('Eu escolhi \33[;33m{}\33[m'.format(cpu))
        aux = False
    elif cpu.upper() == p1.upper():
        print('\33[;33mEMPATE!\nTente novamente\33[m')
        print('Eu também escolhi \33[;33m{}\33[m'.format(cpu))
    else:
        print('\33[1;31mGAME OVER\33[m')
        print('Eu escolhi \33[;33m{}\33[m'.format(cpu))
        novo_jogo = input('\33[;33mTentar novamente?\33[m ')
        if novo_jogo.upper() == 'NÃO' or novo_jogo.upper() == 'NAO':
            aux = False


