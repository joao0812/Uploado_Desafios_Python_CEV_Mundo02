from datetime import date
maior_idade = 0
menor_idade = 0
maior = ' '
menor = ' '
for i in range(1, 8):
    pessoa = input('Digite seu nome: ')
    ano = int(input('Digite seu ano de nascimento: '))
    if (date.today().year - ano) >= 18:
        maior = maior + pessoa + ' '
        maior_idade = maior_idade + 1
    else:
        menor = menor + pessoa + ' '
        menor_idade = menor_idade + 1

print('''Quantiadade de pessoas maiores de idade: \33[;33m{}\33[m
Pessoas maiores de idade: \33[;33m{}\33[m'''.format(maior_idade, maior.split()))
print('''Quantiadade de pessoas menor de idade: \33[;33m{}\33[m
Pessoas menor de idade: \33[;33m{}\33[m'''.format(menor_idade, menor.split()))
