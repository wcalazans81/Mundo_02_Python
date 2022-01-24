r1 = float(input('Digite o 1º segmento de reta: '))
r2 = float(input('Digite o 2º segmento de reta: '))
r3 = float(input('Digite o 3º segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos de reta digitados  podem formar um TRIÂNGULO', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os 03 segmentos de reta digitado não formam um Triângulo ')
