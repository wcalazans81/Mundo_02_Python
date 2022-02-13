ficha = dict()
g = list()
ficha['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas o {ficha["nome"]} jogou? '))
c = s = 0
while c < quant:
    c += 1
    gols = int(input(f'Quantos gols o jogador {ficha["nome"]} marcou na partida {c}ª: '))
    g.append(gols)
    s += gols
ficha['gols'] = g
ficha['total de gols'] = s
print(ficha)
print('\033[36m=0\033[m'* 30) 
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
print('\033[36m=0\033[m'* 30) 
print(f'O jogador {ficha["nome"]} jogou {quant} partidas.')
for i, v in enumerate(g):
    print(f' => Na partida {i+1}ª, fez {v} gols.')
print(f'Foi um total de {s}.')
print('\033[36m=0\033[m'* 30) 