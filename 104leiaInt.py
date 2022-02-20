def leiaInt(msg):
    """
    -> Função que válida a entrada de dado de um número inteiro.
    :param msg: Verifica de o dado digitado pelo usuário é de fato um número inteiro
    :return: O valor se for um número inteiro se não for um número inteiro retorna msg de erro.
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO!!! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
