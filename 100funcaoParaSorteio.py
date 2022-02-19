from time import sleep
from random import randint
num = list()
par = []
numeros = []
def somapar():
    c = s = 0
    while c < 9:      
        n = randint(0, 100)
        num.append(n)
        c += 1
        if n % 2 == 0:
            par.append(n)
            s += n
    print(f'Os números sorteados foram {num}')
    print(f'Os números pares sorteados foram {par} e a soma dos números pares é {s}')


#solução do Guanabara
def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for cont in range(0, 5):
        e = randint(1, 10)
        numeros.append(e)
        print(f'{e} ',end='',flush=True)
        sleep(0.5)
    print('PRONTO!')

def spar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
somapar()
sorteia(numeros)
spar(numeros)
