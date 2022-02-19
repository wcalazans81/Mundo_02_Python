def titulo(msg):
    print('~' * len(msg))
    print(f'{msg}')
    print('=' * len(msg))


def medida(l, c):
    area = l * c
    print(f'A área de um terreno {l} X {c} é de {area}m².')


# Programa principal
titulo('\033[33m=====>>>>>>>>Controle de terrenos<<<<<<<<=====\033[m')
n = float(input('LARGURA: '))
n1 = float(input('COMPRIMENTO: '))
medida(n, n1)