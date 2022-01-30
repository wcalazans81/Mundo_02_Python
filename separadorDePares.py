print('\033[34m0=\033[m' * 27)
print('Propgrama separador e com somatório de números pares')
print('\033[34m0=\033[m' * 27)
s = 0
num = int(input('Digite um número: '))
for c in range(0, num+1):
    if c % 2 == 0:
        print(c)
        s += c
print('\033[34m0=\033[m' * 27)
print('O somatorio de todos os números pares é iqual a {}'.format(s))