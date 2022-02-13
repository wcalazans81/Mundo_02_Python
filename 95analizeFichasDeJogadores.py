from time import sleep
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear
    jogador['nome'] = str(input('Nome do jogador '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f'  Quantos gols na {c}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[31mOPÇÃO INVÁLIDA\033[m! Por favor digite [S/N]')
    if resp == 'N':
        break
print('\033[34m=0\033[m'* 30) 
print('Cod -', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('\033[32m=0\033[m'* 30) 
for k, v in enumerate(time):
    sleep(1)
    print(f'{k:>3}', end='->')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('\033[33m=0\033[m'* 30) 
while True:
    busca = int(input('Mostar dados de qual jogador? (999 para interromper) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\033[31mERRO\033[m! Não existe jogador com código {busca}')
    else:
        print(f'>>>> LEVANTAMENTO DE APROVEITAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            sleep(1)
            print(f'     No jogo {i+1} fez {g} gols.')
print('\033[35m=0\033[m'* 30) 
print('=====>>>>> VOLTE SEMPRE <<<<<=====')
print('\033[36m=0\033[m'* 30) 