from time import sleep
n = int(input('Digite o 1º número: '))
n1 = int(input('Digite o 2º número: '))
op = 0
while op != 6:
    print('\033[36m=0=\033[m' * 16)
    print('''[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Divisão
[6] Sair do programa''')
    op = int(input('Qual é a sua opção? '))
    if  op == 1:
        s = n + n1
        print('A soma entre \033[33m{} e {}\033[m é iqual a \033[34m{}\033[m'.format(n, n1, s))
    if op == 2:
        m = n * n1
        print('O produto da multiplicação entre \033[33m{} e {}\033[m é iqual a \033[32m{}\033[m'.format(n, n1, m))
    if op == 5:
        d = n / n1
        print('A divisão entre \033[36m{} e {}\033[m é iqual a \033[37m{}\033[m'.format(n, n1, d))
    if op == 3:
        maior = n
        if n > n1:
            maior = n
        if n1 > n:
            maior = n1
        print('O maior número entre \033[33m{} e {}\033[m é \033[31m{}\033[m'.format(n, n1, maior))
        if n == n1:
            print('\033[31mOs dois números são iquais.\033[m')
    if op == 4:
        n = int(input('Digite o 1º número: '))
        n1 = int(input('Digite o 2º número: '))
    if op >= 7:
        print('\033[31mOpção inválida! digite um opçõa válida\033[m:')
print('\033[35mFinalizando...\033[m')
sleep(3)
print('\033[32mFim do programa volte sempre!!!\033[m')
