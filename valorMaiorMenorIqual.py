a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
maior = a
if a > b:
    maior = a
    print('O 1º número {} é MAIOR'.format(maior))
elif b > a:
    maior = b
    print('O 2º número {} é MAIOR'.format(maior))
menor = b
if b < a:
    menor = b
    print('O 2º número {} é MENOR'.format(menor))
elif a < b:
    menor = a
    print('O 1º número {} é MENOR'.format(menor))
else:
    print('Os números {} e {} são iquais.'.format(a, b))
print('fim')
# resolução do guanabara
if a > b:
    print('O 1º número é maior')
elif b > a:
    print('O 2º número é maior')
else:
    print('Os números são iquais.')