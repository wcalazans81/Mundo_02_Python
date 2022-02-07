# mostrar itens de um lista com formatação
valores = []
valores.append(9)
valores.append(3)
valores.append(5)
valores.append(8)
for v in valores:
    print(f'{v}...', end='')
print('Fim!!!')
print('\033[34m=-\033[m'*10)
# # mostrar itens de um lista com indice e formatação
for c, v in enumerate(valores):
    print(f'\nNa posição {c+1}ª encontrei o valor {v}!')
print('Cheguei ao final da lista!!!')
print('\033[34m=-\033[m'*10)
# função append(input()) com itens da lista digijtados pelo usario 
valor = []
for cont in range(0, 4):
    valor.append(int(input('Digite um número para adicionar a lista: ')))
for i in valor:
    print(f' {i}...', end='') 
print(f'\nVocê digitou os números {valor}...')
print('\033[34m=-\033[m'*10)