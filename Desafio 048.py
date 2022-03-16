soma = 0

for i in range(1, 501):
    if i%2 != 0 and i%3 == 0:
        print(i)
        soma = soma + i
#       print('VALOR ANTIGO: {}'.format(i_ant))
#       print('SOMA: {}'.format(soma))

print('A soma total dos números selecionados da: \33[;33m{}\33[m'.format(soma))

