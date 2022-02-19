from random import randint
v = []
from time import sleep
def analizador(*num):    
    print('-=' * 20)
    print('        ANALIZADOR DE NÚMEROS')
    print('=-' * 20)
    print('Analizando os valores passados.....')
    c = s = maior = 0
    while c < len(num):
        for n in num:
            print(f'{n}',end=' ',  flush=True) 
            sleep(0.5)
            c += 1
            s += n
            if c == 1:
                maior = n
            if n > maior:
                maior = n         
    print(f'Foram informados {len(num)} valores ao todo.')    
    print(f'O maior valor informado foi o número {maior}. ')
    print(f'A soma de todos os valores passados foi {s}')
    print('=-' * 20)


# Programa principal
analizador(2, 9, 4, 5, 7, 1)
analizador(4, 7, 0)
analizador(6)
analizador()
