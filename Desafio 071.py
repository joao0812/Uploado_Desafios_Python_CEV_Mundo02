from math import trunc
n1 = int(input('Quantida a ser sacada: R$'))
nota_50 = nota_20 = nota_10 = nota_1 = 0
sobra = 0
if n1 > 50:
    nota_50 = trunc(n1/50)
    sobra = n1 - (nota_50 * 50)
if sobra > 20 or 20 <= n1 < 50:
    if n1 < 50:
        nota_20 = trunc(n1/ 20)
        sobra = n1 - (nota_20 * 20)
    else:
        nota_20 = trunc(sobra/20)
        sobra = sobra - (nota_20 * 20)
if sobra > 10 or 10 <= n1 < 20:
    if n1 < 20:
        nota_20 = trunc(n1/ 10)
        sobra = n1 - (nota_20 * 10)
    else:
        nota_20 = trunc(sobra/10)
        sobra = sobra - (nota_20 * 10)
if sobra >= 1 or 1 <= n1 < 10:
    if n1 < 10:
        nota_1 = trunc(n1/ 1)
        sobra = n1 - (nota_20 * 1)
    else:
        nota_1 = trunc(sobra/1)
        sobra = sobra - (nota_20 * 1)
print('='*50)
if nota_50 > 0:
    print(f'Total de {nota_50} notas de R$50,00')
if nota_20 > 0:
    print(f'Total de {nota_20} notas de R$20,00')
if nota_10 > 0:
    print(f'Total de {nota_10} notas de R$10,00')
if nota_1 > 0:
    print(f'Total de {nota_1} notas de R$1,00')
print('='*50)