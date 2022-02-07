# tuplas são imutáveis este comando não é possível. Este comando só é possível em listas.
# Relembrando representações () tuplas, [] listas e {} dicionarios
# num = (1, 9, 3, 5)
# num[2] = 4
# comando para mudar item de uma lista
num = [1, 9, 3, 5]
num[2] = 4
# comando para adicionar itens adicionando mais um indice no final da lisa
num.append(7)
print(num)
print('\033[34m=-\033[m'*10)
# função para inserir um item na lista numa posição espesífica
num.insert(2, 7)
print(num)
print('\033[34m=-\033[m'*10)
# comando para colocar a lista em ordem cresente
num.sort()
print(num)
print('\033[34m=-\033[m'*10)
# comando para colocar a lista em ordem decresente
num.sort(reverse=True)
print(num)
print('\033[34m=-\033[m'*10)
# função pop sem parametro elimina o utimo item da lista
num.pop()
num.pop(1)
print(num)
print('\033[34m=-\033[m'*10)
# função para ver o comprimento da lista
print(f'Essa lista tem {len(num)} itens.')
print('\033[34m=-\033[m'*10)

