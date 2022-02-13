from datetime import date
fich = dict()
fich['nome'] = str(input('Nome: '))
nasc = int(input('Ano do nascimento: '))
idade = date.today().year - nasc 
fich['idade'] = idade
ct = int(input('Nº: Carteira de Trrabalho (0 não tem): '))
if ct != 0:    
    fich['ctps'] = ct
    n = int(input('Ano da contratação: '))
    fich['contratação'] = n
    fich['salárrio'] = float(input('Salário: '))
    c = date.today().year - n
    idaapo = 49 - c + idade
    fich['Aposentadoria'] = idaapo
print(fich)
print('\033[36m=0\033[m'* 30)   
for k, v in fich.items():
    print(f'{k} tem o valor {v}.')     