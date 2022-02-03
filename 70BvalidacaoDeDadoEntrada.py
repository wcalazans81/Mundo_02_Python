from time import sleep
from datetime import date
atual = date.today().year
nomevelho = ''
sexo = ''
cont = tothomem = totmulher = maior = soma = totmulher20 = media = 0
while True:
    cont += 1
    op = ' '
    nome = str(input('Qual é seu Nome? ')).strip()
    ano = int(input('Qual é o ano do seu nascimento? '))
    id = atual - ano
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    soma += id
    media = soma / cont
    if sexo in 'MF':
        print('Sexo registrado com sucesso')
    elif sexo not in 'MF':
        print('\033[31mSexo inválido\033[m!!! por favor digita [M/F]')
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if cont == 1 and sexo == 'M':
        maior = id
        nomevelho = nome
    else:
        if id > maior and sexo == 'M':
            maior = id
            nomevelho = nome
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F':
        totmulher += 1
    if id < 20:
        totmulher20 += 1
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('\033[36m0=\033[m' * 27)
        if op not in 'SN':
            print('\033[31mOpção inválida!\033[m Por favor digite [S/N]')
    if op == 'N':
        break
print('\033[36m0=\033[m' * 27)
print('\033[31mPROCESSANDO....\033[m')
sleep(3)
print(f'Foram cadastradas \033[32m{cont}\033[m pessoas e foram \033[33m{tothomem}\033[m homens e \033[34m{totmulher}\033[m mulheres.')
print(f'O homem mais velho tem \033[33m{maior}\033[m anos e seu nome é \033[33m{nomevelho}\033[m')
print(f'A média de idade das pessoas cadastradas é de \033[35m{media:.2f}\033[m anos e tem  \033[36m{totmulher20}\033[m com menos de 20 anos de idade.')
print('\033[36m0=\033[m' * 27)
