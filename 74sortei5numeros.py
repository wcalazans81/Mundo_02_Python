from random import randrange
menor = maior = 0
cont = 0
while cont < 5:
    cont += 1
    n = randrange(0, 101)
    print(f'{n}', end=' ->')
    if cont == 1:
        menor = n
    if n < menor:
        menor = n
    if cont == 1:
        maior = n
    if n > maior:
        maior = n
print('Fim!!!')
print(f'Dos números soteados o MAIOR É \033[33m{maior}\033[m e o MENOR É \033[34m{menor}\033[m')
