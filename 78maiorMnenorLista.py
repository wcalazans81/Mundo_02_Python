valor = []
valor1 = []
mai = men = 0
for c in range(0,5):
    valor.append(int(input(f'digite um número na posição {c}: ')))
    if c == 0:
        mai = men = valor[c]
    else:
        if valor[c] > mai:
            mai = valor[c]
        if valor[c] < men:
            men = valor[c]
print(f'Você digitou os números {valor}')
print(f'O maior valor foi {mai} nas posições ', end='')
for i, v in enumerate(valor):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {men} nas posições', end='')
for i, v in enumerate(valor):
    if v == men:
        print(f'{i}...', end='')
print()
