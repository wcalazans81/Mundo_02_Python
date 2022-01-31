print('\033[37m=\033[m' * 34)
print('Sequência de Fibonacci')
print('\033[37m=\033[m' * 34)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('\033[36m~\033[m' * 34)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM!!!')