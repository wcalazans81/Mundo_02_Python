from time import sleep
print('\033[35m0=\033[m'*21)
print('{:-^40}'.format('BANCO DO CURSO EM VÍDEO'))
print('\033[35m0=\033[m'*21)
n = int(input('Quanto você quer sacar? '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('\033[31mPROCESSANDO....\033[m')
sleep(3)
if m >= 0 and c >= 0:
    print('Você vai sacar \033[32m{}\033[m notas de R$ 50,00'.format(m * 20 + c * 2))
if d % 2 == 0 and u > 0:
    print(f'Você vai sacar \033[33m{d / 2:.0f}\033[m notas de R$ 20,00 e \033[34m{u}\033[m notas de R$ 1,00')
if d % 2 == 1 and u > 0:
    print(f'Você vai sacar \033[35m{d}\033[m notas de R$ 10,00 e \033[31m{u}\033[m notas de R$ 1,00')
print('\033[33m0=\033[m'*30)
print('Obrigado por usar o banco do Curso em Vídeo VOLTE SEMPRE!!!')
