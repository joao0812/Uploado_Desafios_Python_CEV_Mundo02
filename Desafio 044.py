produto = float(input('Digite o valor do produto: '))
pagamento = int(input('1 -À Vista\n2- À Vista no cartão\n3- Em até 2x no cartão\n4- 3x ou mais no cartão\nDigite a forma de pagamento: '))

if pagamento == 1:
    print('Valor do produto: R${:.2f}'.format(produto))
    print('Desconto de 10%: {:.2f}'.format(produto*0.1))
    print('Total: {:.2f}'.format(produto*0.9))
elif pagamento == 2:
    print('Valor do produto: R${:.2f}'.format(produto))
    print('Desconto de 5%: {:.2f}'.format(produto*0.05))
    print('Total: {:.2f}'.format(produto*0.95))
elif pagamento == 3:
    print('Valor do produto: R${:.2f}'.format(produto))
    print('Total: {:.2f}'.format(produto))
    print('Dividido em 2x no cartão: 2x de R${:.2f}'.format(produto/2))
elif pagamento == 4:
    n1 = int(input('Digite quantas vezes deseja dividir o valor do produto: '))
    if n1 >= 3:
        print('Valor do produto: R${:.2f}'.format(produto))
        print('Dividido em {}x no cartão com 20% de Juro: {} parcelas de R${:.2f}'.format(n1, n1,  (produto/n1)*1.2))
        print('Total: R${:.2f}'.format(produto*1.2))
    else:
        print('\33[1;31mERRO\33[m\nTente parcelar em mais de 2x')