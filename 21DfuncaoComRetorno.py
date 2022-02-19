def soma(a=0, b=0, c=0):
    """
    -> Faza soma de três valores e mostra o resultado na tela.
    :param a: O 1º valor
    :param b: O 2º valor
    :param c: O 3º valor
    :return: s
    """
    s = a + b + c
    return s


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        print('É par!')
        return True  
    else:
        print('Não é par')
        return False


r1 = soma(4, 5, 1)
r2 = soma(3, 5, 1)
r3 = soma(2, 5)
print(f'A soma dos valores apresentados são {r1}, {r2}, {r3}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')
p = int(input('Digite um número: '))
print(par(p))

