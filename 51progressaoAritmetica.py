i = int(input('Digite um número para ver sua progressão aritmética: '))
r = int(input('Digite a razão que deseja para PA do número digitado: '))
decimo = i + (10 - 1) * r
for c in range(i , decimo + r, r):
    print(c, end='-> ')
print('ACABOU')