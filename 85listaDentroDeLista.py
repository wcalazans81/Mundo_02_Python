parimpar = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 ==0:
        parimpar[0].append(n)
    if n % 2 == 1:
        parimpar[1].append(n)
parimpar.sort()
print(f'Todos os valores {parimpar}')
parimpar[0].sort()
print(f'O múmeros pares digitados foram {parimpar[0]}.')
parimpar[1].sort()
print(f'O múmeros impares digitados foram {parimpar[1]}.')