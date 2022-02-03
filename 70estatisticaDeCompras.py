print('\033[32m=-\033[m'*19)
print('''LOJAS BARATÃO DO CURSO EM VÍDEO
    AQUI SEMPRE É MAIS BARATO
        \033[33mVAMOS AS COMPRAS\033[m?''' )
print('\033[32m=-\033[m'*19)
c = s = smil =0
barato = ''
while True:    
    pro = str(input('Nome do produto: '))
    pre = float(input('Preço do produto: R$ '))
    c += 1
    s += pre
    if pre > 1000:
        smil += 1
    if c == 1:
        menor = pre
        barato = pro
    else:
        if pre < menor:
            menor = pre
            barato = pro    
    r = ' '    
    while r not in "SN":
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA!!!'))
print(f'O total da compra foi R${s:.2f}')
print(f'Temos {smil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')