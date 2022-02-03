while True:
    print('Para interromper o programa digite [-1]')
    print('\033[34m=-\033[m'*19)
    n = int(input('Digite um número para ver sua taboada: '))
    for t in range(1, 11):
        print(f'{n} + {t:2} = {n+t}')
    print('\033[35m=-\033[m'*6)
    for t in range(1, 11):
        print(f'{n} X {t:2} = {n*t}')
    print('\033[36m=-\033[m'*6)
    if n == -1:
        break
print('\033[31mFIM DO PROGRAMA!!!\033[m')