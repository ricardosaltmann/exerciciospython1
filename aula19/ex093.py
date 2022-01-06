"""
Exercício Python 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

campeonato = {}
campeonato["Nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {campeonato['Nome']} jogou? "))
gols = []
total = 0
for i in range(0, partidas):
    gol = int(input(f"    Quantos gols na partida {i}?"))
    gols.append(gol)
    campeonato["gols"] = gols
    total += gol
campeonato["Total"] = total
print('-=' * 40)
print(campeonato)
print('-=' * 40)
for k, v in campeonato.items():
    print(f"O campo {k} tem o valor {v}")
print('-=' * 40)
print(f"O jogador {campeonato['Nome']} jogou {partidas} partidas")
for i in range(0, partidas):
    print(f"=> Na partida {i}, fez {gols[i]}")
print(f"foi um total de {campeonato['Total']} gols")

