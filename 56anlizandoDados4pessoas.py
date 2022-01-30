sidade = 0
midade = 0
maioridadehoomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('------ {}ª ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    sidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehoomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehoomem:
        maioridadehoomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
midade = sidade / 4
print('A média de idade do grupo é de {} anos'.format(midade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehoomem, nomevelho))
print('As mulheres com mais de 20 anos de idade são {}'.format(totmulher))