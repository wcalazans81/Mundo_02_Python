from datetime import date
atual = date.today().year
nacs = int(input('Digite o ano do seu nascimento '))
idade = atual - nacs
if idade <= 9:
    print('Você tem {} anos de idade e é uma nadadora da classe MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} de idade e é um nadador da classe INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos de idade e é um nadador da classe JUNIOR.'.format(idade))
elif idade == 20:
    print('Você tem {} anos de idade e é um nadador da classe SÊNIOR.'.format(idade))
elif idade > 20:
    print('Você tem {} anos de idade e é um nadador da classe MASTER.'.format(idade))
print('FIM!!!')
