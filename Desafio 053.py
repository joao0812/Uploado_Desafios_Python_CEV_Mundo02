frase = input('Digite uma frase: ')
x = 1
# Transforma a palavra em lista para remover os espaços
aux = list(frase.upper())
# Remove os espaços da palavra digitada
for i in range (0, aux.count(' ')):
    aux.remove(' ')

# Compara se a primeira letra até a última é igual a última até a primeira
for i in range(1, len(aux) + 1):
    if aux[i-1] == aux[len(aux)-i]:
        x = x + 1
#       print(aux[i-1], aux[len(aux)-i])
#       print(x)

# print(x, len(aux), aux)

if x == len(aux) + 1:
    print('A palavra \33[4;33m{}\33[m é um Políndromo'.format(frase.capitalize()))
else:
    print('A palavra \33[4;33m{}\33[m Não é um Políndromo'.format(frase.capitalize()))



