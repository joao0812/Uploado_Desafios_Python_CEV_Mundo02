peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura atual em centímetro: '))

imc = peso/((altura/100)**2)

if imc < 18.5:
    print('\33[1;31mATENÇÃO\33[m')
    print('Você está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('\33[;32mTudo OK\33[m')
    print('Você no peso ideal')
elif 25 <= imc < 30:
    print('\33[;33mNotificação\33[m')
    print('Você está em sobrepeso')
elif 30<= imc < 40:
    print('\33[;33mCUIDADO\33[m')
    print('Você está em obesidade')
elif imc > 40:
    print('\33[1;31mATENÇÃO!\33[m')
    print('Você está em obesidade mórbida')
