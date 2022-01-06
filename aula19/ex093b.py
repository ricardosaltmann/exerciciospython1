"""
Exercício Python 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

campeonato = {}
campeonato["Nome"] = str(input("Nome do Jogador: "))
tot= int(input(f"Quantas partidas {campeonato['Nome']} jogou? "))
partidas = []
total = 0
for i in range(1, tot + 1 ):
    partidas.append(int(input(f"    Quantos gols na partida {i}? ")))
campeonato["gols"] = partidas[:]
campeonato["Total"] = sum(partidas)
print('-=' * 40)
print(campeonato)
print('-=' * 40)
for k, v in campeonato.items():
    print(f"O campo {k} tem o valor {v}")
print('-=' * 40)
print(f'O jogador {campeonato["Nome"]} jogou {len(campeonato["gols"])} partidas.')
for i, v in enumerate(campeonato["gols"]):
    print(f"=> Na partida {i + 1}, fez {v} gols.")
print(f"foi um total de {campeonato['Total']} gols")
