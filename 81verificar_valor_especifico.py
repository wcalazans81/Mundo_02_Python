num = list()
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
num.sort(reverse=True)
print(f'Você digitou {len(num)} elementos')
if 5 in num:
    print('O número 5 faz parte da lista.')
else:
     print('O número não 5 faz parte da lista.')