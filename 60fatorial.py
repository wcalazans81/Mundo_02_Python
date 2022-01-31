from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = factorial(n)
print('{}'.format(f))  