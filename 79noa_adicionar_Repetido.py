num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado! Não adicionado')
    r = str(input('Quer continuar? [S/N] ' ))
    if r in 'Nn':
        break
num.sort()
print(f'Você digitou os números {num}')