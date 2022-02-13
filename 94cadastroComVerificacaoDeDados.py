pessoas = list()  
temp = dict()
c = s = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo not in 'MmFf':
        sexo = str(input('Sexo inválido por favor digite: [M/F] ')).strip().upper()[0]
    idade = int(input('Idade: '))
    resp = str(input('Quer continuar? [S/N]: '))
    temp['nome'] = nome
    temp['sexo'] = sexo
    temp['idade'] = idade 
    pessoas.append(temp.copy())
    temp.clear()
    c += 1
    s += idade
    media = s / c
    if resp in 'Nn':
        break
    if resp not in 'Ss':
        resp = str(input('Resposta inválida! Quer continuar? [S/N]: '))
print('\033[36m=0\033[m'* 30) 
print(f'A) Ao todo foram cadastradas {c} pessoas.')
print('\033[36m=0\033[m'* 30) 
print(f'B) Amédia de idade é de {media:.1f} anos.')
print('\033[36m=0\033[m'* 30) 
print(f'C) As mulheres cadastradas foram', end=' ')
for i, k in enumerate(pessoas):
    if pessoas[i]["sexo"] in 'F':
        fem = pessoas[i]["nome"]
        print(f'{fem}', end=' -> ')
    if pessoas[i]["idade"] > media:
        pam = k
print()
print('\033[36m=0\033[m'* 30) 
print('D) Listas de pessoas que estão acima da média de idade:')
print(k)
