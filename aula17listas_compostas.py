galera = []
dado = []
totmai = totmen = 0
for c in range(0, 4):
# lista dado recebe os dados para transferir para a outra lista galera
    dado.append(str(input('Qual é o seu nome? ')))
    dado.append(int(input('Qual é a sua idade ')))
# comando para adicionar uma lista dentro da outra
    galera.append(dado[:])
# comando para limpar uma lista
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')