from random import randint
computador = randint(1, 10)
jogador = int(input('Digite um valor: '))
cont = 1
while jogador != computador:
    if jogador > computador:
        print('Menos!')
    if jogador < computador:
        print('Mais!')
    jogador = int(input('Tente mais um vez: '))
    cont += 1
print('O computador escolheu o número {} e você adivinhou com {} tentativas'.format(computador, cont))