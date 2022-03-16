cont_fem = cont_masc = cont = 0
lista_maior_idade = lista_masc = lista_fem = ''

while True:
    nome = input('Digite seu nome: ').capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M/F]: ').upper()
    print('-' *40)
    if idade >= 18:
        cont += 1
        lista_maior_idade += nome + ' | '
    if sexo == 'M':
        cont_masc += 1
        lista_masc += nome + ' | '
    if sexo == 'F' and idade <= 20:
        cont_fem += 1
        lista_fem += nome + ' | '
    perg = input('Deseja continuar? [S/N]\n➝ ').upper()
    while perg not in 'SN':
        print('\33[;31mRESPOSTA INVÁLIDA!\33[m')
        perg = input('Deseja continuar? [S/N]\n➝ ').upper()
    if perg == 'N':
        break

print(f'Total de pessoas maiores de idade: \33[;33m{cont}\33[m ➝ {lista_maior_idade}')
print(f'Total de Homens: \33[;33m{cont_masc}\33[m ➝ {lista_masc}')
print(f'Total de Mulheres com menos de 20 anos: \33[;33m{cont_fem}\33[m ➝ {lista_fem}')
