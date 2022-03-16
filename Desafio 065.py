cond = True
aux = 0
maior = 0
menor = 0
soma = 0

while cond == True:
    n1 = int(input('Digite um número: '))
    if aux == 0:
        maior = n1
        menor = n1
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
    soma = soma + n1
    perg = input('Deseja continuar? [S/N]: ').upper().strip()
    while perg not in 'NS':
        print('{:^40}'.format('\33[;31mCOMANDO INVÁLIDO!\33[m,\nTente novamente'))
        perg = input('Deseja continuar? [S/N]: ').upper().strip()
    if perg == 'N':
        cond = False
    aux += 1
print('Média dos números: {}'.format(soma/aux))
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))