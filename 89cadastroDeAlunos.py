alunos = []

while True:
    nome = str(input('Nome: '))
    n = float(input(f'Digite a 1ª nota: '))
    n1 = float(input(f'Digite a 2ª nota: '))
    média = (n + n1) / 2
    alunos.append([nome, [n, n1], média])
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print('\033[33m=0\033[m'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('\033[35m=0\033[m'*30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('\033[35m=0\033[m'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('<<< VOLTE SEMPRE >>>')



