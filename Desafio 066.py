cont = soma = 0
while True:
    n1 = int(input('Digite um número[999 p/ parar]: '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'Números digitados: {cont}\nSoma total: {soma}')
