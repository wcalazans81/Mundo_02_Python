print('\033[34m^=\033[m' * 27)
print('Conversor de decimal para binário, octol e hexadecimal')
print('\033[34m=^\033[m' * 27)
print("""Opção [1] Binário
Opção [2] Octal
Opção [3] Hexadecimal""")
print('\033[34m^=\033[m' * 27)
num = int(input('Digite o valor que deseja converter: '))
op = int(input('Digite a opção de conversão que deseja: '))
if op == 1:
    print('O número {} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida tente novamente !!!\033[m')
