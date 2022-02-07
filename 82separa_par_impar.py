num = []
par = list()
impar = []
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if n % 2 == 0:
        par.append(n)
    if n % 2 == 1:
        impar.append(n)
    if r in 'Nn':
        break
print(f'A lista completa é {num}.')
print(f'A lista de números pares é {par}')
print(f'A lista de números impares é {impar}')
# solução do Guanabara
num1 = list()
pares = list()
impares = list()
while True:
    num1.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for indice, v in enumerate(num1):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {num1}.')
print(f'A lista de números pares é {pares}')
print(f'A lista de números impares é {impares}')