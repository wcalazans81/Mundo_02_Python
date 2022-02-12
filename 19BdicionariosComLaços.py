# mostrar chaves de um dicionário com laço de repetição
pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
# comando para adicionar itens ao dicionário
pessoas['peso'] = 98.5
pessoas['ano de nascimento'] = 1975
for k in pessoas.keys():
    print(k, end='-> ')
# mostrar valores de um dicionário com laço de repetição
for k in pessoas.values():
    print(k, end=' -> ')
print()
#comando para substituir um valor em um dicionário
pessoas['nome'] = 'Wellington'
pessoas['Idade'] = 47
# mostrar chaves e valores de um dicionário com laço de repetição
for k, v in pessoas.items():
    print(f'{k} = {v}')