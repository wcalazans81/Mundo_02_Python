from random import randint
from time import sleep
temp = list()
jogos = []
print('\033[34m=0\033[m'* 30)
print('      JOGO DA MEGA SENA      ')
print('\033[33m=0\033[m'* 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    tot += 1
print('\033[31mPROCESSANDO.....\033[m')
sleep(3)
print('\033[33m=0\033[m'* 4, f'SOTEANDO \033[32m{quant}\033[m JOGOS', '\033[33m=0\033[m'* 4)    
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('\033[35m==========\033[m BOA SORTE \033[35m==========\033[m')
