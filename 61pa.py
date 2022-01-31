i = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a Razão da PA: '))
decimo = i + (10 - 1) * r
c = i - r
while c < decimo:
    c += r
    print('{} -> '.format(c), end='')
print('FIM!!!')
# solução do guanabara
i = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a Razão da PA: '))
termo = i
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM!!!')