aluno = {'nome': '', 'média': ''}
nome = str(input('Digite o nome do aluno(a): ')).strip()
s = 0
for c in range(1, 5):
    n = float(input(f'Digite a nota do {c}º bimestre do aluno(a): '))
    s += n 
m = s / c
aluno['nome'] = nome
aluno['média'] = m
print('\033[36m=0\033[m'* 30)
print(f'Nome é iqual a {aluno["nome"]}')
print(f'Média é iqual a {aluno["média"]}')
if m >= 15:
    print(f'O aluno {nome} finalizou o ano com a média {m} está aprovado')
elif 10 <= m < 15:
    print(f'O aluno {nome} finalizou o ano com a média {m} está em recuperação')
else:
    print(f'O aluno {nome} finalizou o ano com a média {m} está em reprovado') 
print(s, m, aluno)
# solução do Guanabara
alunos = dict()
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
if alunos['Média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['Média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
print('\033[36m=0\033[m'* 30)
for k, v in alunos.items():
    print(f'{k} é iqual a {v}.')
print('\033[36m=0\033[m'* 30)
print(alunos)