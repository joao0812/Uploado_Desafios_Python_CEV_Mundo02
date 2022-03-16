while True:
    print('-'*40)
    n1 = int(input('Quer ver a tabuada de qual valor?\n➝ '))
    if n1 < 0:
        break
    print('-' * 40)
    for i in range(0, 11):
        print(f'{n1} x {i} = {n1*i}')
print('\33[;32mConcluído\33[m')