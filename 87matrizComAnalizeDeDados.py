from time import sleep
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = menor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
print('\033[35m=0\033[m'* 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('\033[31mANALIZAR DADOS DA MATRIZ! PROCESSANDO....\033[m') 
sleep(3)
print('\033[35m=0\033[m'* 30)
print(f'A soma de todos os numeros pares da matriz é \033[36m{somapar}\033[m')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma de todos os numeros da 3ª coluna é \033[34m{somacol}\033[m')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
        menor = matriz[2][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
    elif matriz[2][c] < menor:
        menor = matriz[2][c]
print(f'O maior número da 2ª linha é \033[33m{maior}\033[m')
print(f'O menor número da 3ª linha é \033[31m{menor}\033[m')
