from math import ceil
aux = True

while aux == True:
    valor_casa = float(input('Digite o valor da casa: '))
    salario = float(input('Digite seu salário: '))
    anos = int(input('Em quantos anos será pago: '))


    mes = valor_casa/(12 * anos)

    if mes >= salario * 0.3:
        print('\33[1;31mNEGADO!\33[m')
        print('Valor da parcela mensal (R${:.2f}), maior que 30% do salário (R${:.2f})'.format(mes, salario*0.3))
        print('Para ser aprovado, tente aumentar a quantidade de anos para no mínimo \33[1;33m{}\33[m anos'.format(ceil(valor_casa/(12 * salario*0.3))))
        resp = input('Gostaria de reajustar a quantiadade de anos? (Sim ou Não) ')
        if resp.upper() == 'NÃO':
            print('Processo encerrado')
            aux = False

    else:
        print('\33[1;32mAPROVADO!\33[m')
        print('Parcela anual: R${:.2f}'.format(valor_casa/anos))
        print('Parcela mensal: R${:.2f}'.format(mes))
        print('Quantidade total de meses: {}'.format(anos*12))
        aux = False