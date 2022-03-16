# Variáveis auxiliares (ta bugado, o programa ta lendo x e y como Str, por isso no código tive que converter
# ele para Int
media = 0
x = 0
y = 0
valor = 0
# Array para juntar cada, nome, idade e sexo respectivamente
nome_lista = ' '
idade_lista = ' '
sexo_lista = ' '
menor_idade = ' '
# Leitura de 4 nomes, idades e sexo
for i in range(1, 5):
    print('----- {}ª Pessoa -----'.format(i))
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    sexo = input('Digite o sexo que você se considera (M/F): ')
# Somatório das idades para dividir pela qunatidade de pessoas, 4, no saída do for
    media = (media + int(idade))
# Conjunto de if para determinar a meior e menor idade digitada
    if int(idade) > int(x):
        maior = idade
        x = idade
        velho = nome
        if sexo. upper() == 'MASCULINO' or sexo.upper() == 'M':
            homem_velho = nome
            homem_velho_idade = idade
    if int(y) == 0:
        menor = idade
        y = idade
        novo = nome
    elif int(idade) <= int(y):
        menor = idade
        y = idade
        novo = nome
# Verificadno quantas e quem é mulher com menos de 20 anos
    if int(idade) <= 20 and (sexo.upper() == 'F' or sexo.upper() == 'FEMININO'):
        menor_idade = menor_idade + nome.capitalize() + ' '
        valor = valor + 1
# Juntando os nomes, idades e sexos em uma lista com espaços para, ao recebrem split(), separem as palavras não as letras
    nome_lista = nome_lista + nome.capitalize() + ' '
    idade_lista = idade_lista + idade + ' '
    sexo_lista = sexo_lista + sexo.upper() + ' '

media = media/4

# zipper = zip(nome_lista.split(), idade_lista.split(), sexo_lista.split())
# print(list(zipper))

print('Nome: {}'.format(nome_lista.split()))
print('Idade: {}'.format(idade_lista.split()))
print('Sexo: {}'.format(sexo_lista.split()))
print('Pessoa mais velha é \33[;33m{}\33[m com \33[;33m{}\33[m anos'.format(velho.capitalize(), maior))
print('Pessoa mais nova é \33[;33m{}\33[m com \33[;33m{}\33[m anos'.format(novo.capitalize(), menor))
print('Homem mais velho: \33[;33m{}\33[m com \33[;33m{}\33[m anos'.format(homem_velho, homem_velho_idade))
print('Média de idade: \33[;33m{}\33[m anos'.format(media))
print('A qunatidade de mulheres com menos de 20 anos: \33[;33m{}\33[m'.format(valor))
print('Mulheres com menos de 20 anos: \33[;33m{}\33[m'.format(menor_idade.split()))
