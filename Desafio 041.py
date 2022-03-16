from datetime import date
ano = int(input('Digite o ano em que nasceu: '))

if ano < 9:
    print('O atleta tem: {} anos'.format(date.today().year - ano))
    print('Categoria: \33[;33mMIRIM\33[m')
elif 9 < ano <= 14:
    print('O atleta tem: {} anos'.format(date.today().year - ano))
    print('Categoria: \33[;33mINFANTIL\33[m')
elif 14 < ano <= 19:
    print('O atleta tem: {} anos'.format(date.today().year - ano))
    print('Categoria: \33[;33mJÚNIOR\33[m')
elif 19 < ano <= 25:
    print('O atleta tem: {} anos'.format(date.today().year - ano))
    print('Categoria: \33[;33mSÊNIOR\33[m')
elif ano > 25:
    print('O atleta tem: {} anos'.format(date.today().year - ano))
    print('Categoria: \33[;33mMASTER\33[m')