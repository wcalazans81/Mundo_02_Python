r = 'S'
s = q = m = maior = menor = 0
while r in 'Ss':
    num = int(input('Digite um número: '))
    s += num
    q += 1
    if q == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = s / q
print('Você digitou {} números e a média foi {}'.format(q, m))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))