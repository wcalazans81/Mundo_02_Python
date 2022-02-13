galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite seu nome: '))
    while True:
        pessoa['sexo'] = str(input('Qual é seu sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('\033[31mSEXO INVÁLIDO\033[m! por favor digite [M/F]')
    pessoa['idade'] = int(input('Qual é a sua idade? '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[31mSEXO INVÁLIDO\033[m! por favor digite [S/N]')
    if resp == 'N':
        break
print('\033[36m=0\033[m'* 30) 
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas')
print('\033[35m=0\033[m'* 30)
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('\033[34m=0\033[m'* 30)
print('C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' -> ')
print()
print('\033[33m=0\033[m'* 30)
print('D) Lista de pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\033[32m=0\033[m'* 30)
print('<<<<<=====ENCERRADO!!!=====>>>>>')
