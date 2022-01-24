from time import sleep
a = float(input('Digite a 1º nota do aluno: '))
b = float(input('Digite a 2º nota do aluno: '))
media = (a + b) / 2
print('\033[31mPROCESSANDO....\033[m')
sleep(3)
if media >= 7:
    print('A média do aluno foi {:.1f} \033[36mparabéns você está APROVADO!!!\033[m'.format(media))
elif media > 5 or media == 6.9:
    print('A média do aluno foi {:.1f} \033[33mvocê está de RECUPERAÇÃO.\033[m'.format(media))
elif media <= 5:
    print('A média do aluno foi {:.1f} \033[31mREPROVADO ESTUDE MAIS!!!\033[m'.format(media))
print('FIM!!!')
