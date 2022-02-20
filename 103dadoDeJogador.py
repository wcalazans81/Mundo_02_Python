def dado(jog='<Desconhcido>', gol=0):
    print(f'O Jogador {jog} fez {gol} gol(s) no campeonato')


n = str(input('Nome do Jogador: ')).strip().upper()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    dado(gol=g)
else:
    dado(n, g)
