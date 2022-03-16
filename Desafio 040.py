n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2

if media < 5:
    print('\33[1;31mREPROVADO\33[m')
elif 5 <= media <= 6.9:
    print('\33[1;33mRECUPERAÇÃO\33[m')
elif media >= 7:
    print('\33[1;32mAPROVADO\33[m')
