from random import randint
tot = 0
while True:
    computador = randint(0, 10)
    print('\033[33m=-\033[m'*19)
    print('VAMOS JOGAR PAR OU IMPAR!!!')
    print('\033[33m=-\033[m'*19)
    jogador = int(input('Escolha um número para comaçar: '))
    s = computador + jogador
    print('\033[34m=-\033[m'*19)
    escolha = int(input('Faça sua escolha \033[32m[1] PAR\033[m E \033[33m[2] IMPAR\033[m '))
    print('\033[34m=-\033[m'*19)
    if escolha == 1 and s % 2 == 0:
        print(f'O computador jogou \033[36m{computador}\033[m você jogou \033[35m{jogador}\033[m')
        print(f'Deu \033[32m{s}\033[m PAR  \033[33mVoce GANHOU!!!\033[m')
    elif escolha == 1 and s % 2 == 1:
        print(f'O computador jogou \033[36m{computador}\033[m e você jogou \033[35m{jogador}\033[m')
        print(f'Deu \033[33m{s}\033[m IMPAR  \033[31mVoce PERDEU!!!\033[m')
        break
    elif escolha == 2 and s % 2 == 0:
        print(f'O computador jogou \033[36m{computador}\033[m e você jogou \033[35m{jogador}\033[m')
        print(f'Deu \033[33m{s}\033[m PAR  \033[31mVoce PERDEU!!!\033[m')
        break
    elif escolha == 2 and s % 2 == 1:
        print(f'O computador jogou \033[36m{computador}\033[me você jogou \033[35m{jogador}\033[m')
        print(f'Deu \033[32m{s}\033[m IMPAR  \033[33mVoce GANHOU!!!\033[m')
    tot += 1   
if tot <= 3 :
    print(f'Você teve {tot} vitórias. \033[31mVOCÊ PODE SER MELHOR QUE ISSO TETE ME VENCER MAIS VEZES!!!\033[m')
else:
    print(f'\033[33mVocê venceu {tot} PARABÉNS VOCÊ É O(a) MELHOR\033[m!!!!!!')