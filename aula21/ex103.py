def jogador(j='<desconhecido>', g=0):
    print(f'O jogador {j} fez {g} gol(s) no campeonato.')


j = str(input("Nome do Jogador: ")).strip()
g = str(input("Número de Gols: ")).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j == '':
    jogador(g=g)
else:
    jogador(j, g)


