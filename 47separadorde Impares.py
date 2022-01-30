print('\033[31m=0\033[m'*27)
print('Programa separador de números IMPARES!!!')
print('\033[31m=0\033[m'*27)
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('Existem {} números multiplos de 3 entre os impares e a soma dos número é iqual a {}'.format(cont, s))