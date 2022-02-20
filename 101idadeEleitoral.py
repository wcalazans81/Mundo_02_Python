def voto(ano):
    """
    -> Função recebe o ano de nascimento do usuário .
    :return: A idade e a verificação se o usuário está em idade eleitoral.
    """
    from datetime import date
    atual = date.today().year
    idade = atual - anonasc
    if idade < 16:
        return f'Você tem {idade} e não voto'
    elif 16 <= idade <= 18:
        return f'Você tem {idade} e o voto é não é opcional'
    elif 18 <= idade <= 60:
        return f'Você tem {idade} anos e o vote é obrigatório'
    else:
        return f'Você tem {idade} anos e o vote é opcional'


anonasc = int(input('Qual é o ano do seu nascimento? '))
print(voto(anonasc))
