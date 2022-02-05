# Solução do Guanabara
from time import sleep
print('\033[35m0=\033[m'*21)
print('{:-^40}'.format('BANCO DO CURSO EM VÍDEO'))
print('\033[35m0=\033[m'*21)
valor = int(input('Quanto você quer sacar? '))
total = valor
ced = 50
totced = 0
print('\033[31mPROCESSANDO....\033[m')
sleep(3)
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\033[33m0=\033[m'*30)
print('Obrigado por usar o banco do Curso em Vídeo VOLTE SEMPRE!!!')