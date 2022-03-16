ano_nascimento = int(input('Digite o ano em que você nasceu: '))

idade = 2022 - ano_nascimento

if idade > 18:
    print('\33[;31mATENÇÃO\33[m')
    print('Você perdeu o prazo de alistamento')
    print('Seu alistamento era pra ter sido no ano de \33[;33m{}\33[m há \33[;33m{}\33[m anos'.format(ano_nascimento + 18, 2022 - (ano_nascimento + 18)))
elif idade < 18:
    print('Ainda não está no período de alistamento')
    print('Seu alistamento está programado para ocorrer no ano de \33[;33m{}\33[m, ainda faltam \33[;33m{}\33[m ano,'.format(ano_nascimento + 18, (ano_nascimento + 18) - 2022))
elif idade == 18:
    print('\33[1;32mAPTO PARA ALISTAMENTO\33[m')

