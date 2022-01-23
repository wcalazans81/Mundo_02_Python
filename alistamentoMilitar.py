from datetime import date
atual = date.today().year
nasc = int(input('Qual é seu ano de nascimento? '))
idade = atual - nasc
temp = idade - 18
ano = 18 - idade
print('Quem nasceu no ano de {} tem {} de idade, no ano {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você não está na idade de se apresntar ao serviço militar. Faltam {} anos '.format(ano))
elif idade == 18 or idade <= 60:
    print('Você ja possou do tempo do seu alistamento militar. Você está com {} anos de atraso!'.format(temp))
else:
    print('Você esta dispençado do serviço militar por idade.')
