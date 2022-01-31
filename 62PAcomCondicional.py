
i = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a Razão da PA: '))
termo = i
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA!!!')
    mais = int(input('\033[36mQuantos termos da PA você quer mostrar a mais? \033[m'))
print('Progressão finalizada com \033[33m{}\033[m termos mostrados'.format(total))
print('FIM!!!')