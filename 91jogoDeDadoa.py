from time import sleep
from random import randint
from operator import itemgetter
jog = {'Jogador1': 0, 'Jogador2': 0, 'Jogador3': 0, 'Jogador4': 0}
ranking = list()
sort = []
c = 0
while True:  
    n = randint(1, 6)
    if n not in sort:
        sort.append(n)
        c += 1         
    if c >= 4:
        break
for i, v in enumerate(sort):
    print(f'O {i+1}º jogador jogou o dado e tirou {v}.')
    sleep(1)
print(sort)
print('\033[36m=0\033[m'* 30)
jog['Jogador1'] = sort[0]
jog['Jogador2'] = sort[1]
jog['Jogador3'] = sort[2]
jog['Jogador4'] = sort[3]
print(jog)
for k, v in jog.items():
    print(f'{k} = {v}')
    sleep(1)
print('\033[36m=0\033[m'* 30)
print('<<<<<===== RANKING DOS JOGADORES =====>>>>>')
# depois que o dicionário passa por esse processo ele se transfoma em lista
ranking = sorted(jog.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'Em {i+1}º lugar {v[0]} com {v[1]} pontos')
    sleep(1)
print(ranking)