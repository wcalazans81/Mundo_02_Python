from time import sleep

print('\033[36m0=\033[m' * 27)
print('Analizando seu índice de massa corporal!!!')
print('\033[36m0=\033[m' * 27)
alt = float(input('Qual é sua altura? (m) '))
p = float(input('Qual é seu peso? (kg) '))
ma = p / (alt ** 2)
print('\033[31mPROCESSANDO...\033[m')
sleep(3)
print('Seu indice de massa corporal é {:.1f}'.format(ma))
if ma <= 18.5:
    print('Cuidado você está abaixo do peso precisa se cuidar!')
elif ma >= 18.5 and ma < 25:
# maneira tradicional de escrever a syntax
    print('Parabéns você está com o peso IDEAL!')
elif 25 <= ma < 30:
# maneira simplificada de escrever a syntax
    print('Cuidado você está com SOBREPESO')
elif 30 <= ma < 40:
    print('O alerta foi ligado você está com OBESIDADE!')
else:
    print(
        'O alerta vermelho foi ligado você está com OBESIDADE  MÓRBIDA \n\033[31mprocure o seviço de saúde imediatamente\033[m')
