cont_caro = cont_barato = soma = maior = menor = 0
prod_caro = prod_barato = prod_menor = prod_maior = ''

while True:
    produto = input('Digite o nome do produto: ').capitalize().strip()
    valor = float(input('Digite o valor do produto: R$'))
    if soma == 0:
        maior = valor
        menor = valor
        prod_maior = produto
        prod_menor = produto
    elif valor > maior:
        maior = valor
        prod_maior = produto
    elif valor < menor:
        menor = valor
        prod_menor = produto
    soma += valor
    if valor >= 1000:
        cont_caro += 1
        prod_caro += produto + ' | '
    else:
        cont_barato += 1
        prod_barato += produto + ' | '
    perg = input('Deseja continuar? [S/N]\n➝ ').upper()
    while perg not in 'SN':
        print('\33[;31mRESPOSTA INVÁLIDA!\33[m')
        perg = input('Deseja continuar? [S/N]\n➝ ').upper()
    if perg == 'N':
        break

print(f'TOTAL: R${soma:.2f}')
print(f'Quantidade de produtos valentdo mais de R$1000,00: {cont_caro} ➝ {prod_caro}')
print(f'Quantidade de produtos valentdo menor de R$1000,00: {cont_barato} ➝ {prod_barato}')
print(f'O produto mais barato foi: R${menor} ➝ {prod_menor}')
print(f'O produto mais caro foi: R${maior} ➝ {prod_maior}')

