def titulo(txt):
    print('~' * len(txt))
    print(f'{txt}')
    print('=' * len(txt))


# função com parametros espesíficos se 02 ou mais a função só funciona com o total de parametros espcificados 
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# função sem especificação de quantidade de paramtros
def cont(*num):
    for valor in num:
        print(valor, end=' -> ')
    print('FIM!!!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


def soma1(*valor):
    s = 0
    for n in valor:
        s += n
    print(f'Somando os valores {valor} temos o resultado {s}')

# trabalhando com listas e dicionários usando funções
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


# código principal
valores = [6, 3, 9, 0, 1, 2]
titulo('    Curso em Video            ')
titulo('    PyThon Mundo 03           ')
titulo('Com o extraordinário Professor')
titulo('    Gustavo Guanabara!!!      ')
soma(b=4, a=5)
soma(7, 2)
cont(5, 7, 2)
cont(8, 0)
cont(2, 4, 6, 7, 9)
dobra(valores)
print(valores)
soma1(5, 2)
soma1(2, 9, 4)