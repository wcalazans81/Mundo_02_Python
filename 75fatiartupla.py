n = (int(input(f'Digite o 1º número: ')),
     int(input(f'Digite o 2º número: ')),
     int(input(f'Digite o 3º número: ')),
     int(input(f'Digite o 4º número: ')))
print(f'Você digitou os números {n}')
print(f'O número 9 foi digitado {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 está na {n.count(3)+1} posição.')
for t in n:
    if t % 2 == 0:
        print(f'pares são {t}')
if t % 2 == 1:
    print('Você não digitou nenhum número par!')
print('Fim!!!')

