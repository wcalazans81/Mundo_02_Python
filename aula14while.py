c = 1
r = 'S'
totpar = totimpar = 0
while c < 10:
    print(c, end=' - ')
    c += 1
print('fim')
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Digite [S/N] para continuar: ')).upper()
    if n % 2 == 0:
        totpar += 1
    if n % 2 == 1:
        totimpar += 1
    if r in 'N':
        break
print('foram digitados {} números pares e {} números impares'.format(totpar, totimpar))

