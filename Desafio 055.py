x = 0
y = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}° paciente: '.format(i)))
    if peso > x:
        maior = peso
        x = peso
    if y == 0:
        menor = peso
        y = peso
    elif peso <= y:
        menor = peso
        y = peso


print('O maior peso vale: \33[;33m{}\33[mKg'.format(maior))
print('O menor peso vale: \33[;33m{}\33[mKg'.format(menor))


