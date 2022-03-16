n1 = int(input('Digite um número: '))
print('{:=^40}'.format('\33[1;33mTABUADA DO : {}\33[m').format(n1))

for i in range (1, 11):
    print('{} x {} = {}'.format(n1, i, n1*i))

