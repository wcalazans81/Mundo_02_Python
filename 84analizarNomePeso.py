from time import sleep
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Qual é o seu peso? ')))
    if len(princ) == 0:
         mai = men = temp[1]      
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar? [S/N] '))   
    if r in 'Nn':
        break
print(princ)  
print('\033[31mANALIZANDO LISTA DE DADOS....\033[m')
sleep(3)  
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi {mai} kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi {men} kg. Peso de ', end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
